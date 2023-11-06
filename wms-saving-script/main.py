import requests

# Define the WMS URL
wms_url = "http://localhost:8080/geoserver/ITE-18-WEBGIS/wms?"

# Define WMS parameters (e.g., layers, bounding box, etc.)
params = {
    "service": "WMS",
    "request": "GetMap",
    "layers": "ITE-18-WEBGIS:projected_soil",
    "format": "image/png",
    "width": 800,
    "height": 600,
    "srs": "EPSG:4326",
    # Add other necessary parameters
}

# Make a GET request to the WMS service
response = requests.get(wms_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Save the WMS response as a local file
    with open("output.png", "wb") as f:
        f.write(response.content)
