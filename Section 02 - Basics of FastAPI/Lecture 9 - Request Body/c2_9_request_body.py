from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union


app = FastAPI()


# Define a Pydantic model 'SpaceProbe'.
class SpaceProbe(BaseModel):
    identifier: str
    mission: Union[str, None] = None
    velocity: float
    fuel_level: Union[float, None] = None

# Create a route to register a new space probe.
@app.post("/space-probes/")
async def register_probe(probe: SpaceProbe):
    return probe


@app.post("/space-probes/")
async def register_probe(probe: SpaceProbe):
    # Convert the incoming 'probe' data into a dictionary.
    probe_report = probe.dict()
    # Check if the 'fuel_level' field is provided in the probe data.
    if probe.fuel_level:
        # Determine the fuel status based on the 'fuel_level'.
        fuel_status = "Sufficient" if probe.fuel_level > 20 else "Low"
        probe_report.update({"fuel_status": fuel_status})
    return probe_report

# PUT endpoint for updating an existing space probe.
@app.put("/space-probes/{probe_id}")
async def update_probe(probe_id: int, probe: SpaceProbe, q: Union[str, None] = None):
    response = {"probe_id": probe_id, **probe.dict()}
    if q:
        response.update({"additional_query": q})
    return response
