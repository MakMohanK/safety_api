from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from process import get_location_info  # Import the function from process.py

app = FastAPI()

# Define the expected JSON format
class LocationInput(BaseModel):
    latitude: float
    longitude: float

@app.post("/predict")  # Use POST for JSON input
def predict_location(data: LocationInput):
    latitude = data.latitude
    longitude = data.longitude

    # Get the processed location data
    result = get_location_info(latitude, longitude)
    print(result)

    return {"data": result}  # Return the processed list

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
