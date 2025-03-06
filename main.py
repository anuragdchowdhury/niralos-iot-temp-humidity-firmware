from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Ensure this folder exists

# IoT settings (dummy values for now)
iot_settings = {
    "sensor_type": "Temperature",
    "sensor_status": "Active",
    "sensor_value": "25°C",
    "sensor_polling_rate": 5,
    "gateway_polling_rate": 10,
    "wifi_ssid": "MyWiFi",
    "wifi_password": "",
}

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request, "settings": iot_settings})

@app.post("/save-settings/")
async def save_settings(
    sensor_polling: int = Form(...),
    gateway_polling: int = Form(...),
    wifi_ssid: str = Form(...),
    wifi_password: str = Form(...),
):
    iot_settings["sensor_polling_rate"] = sensor_polling
    iot_settings["gateway_polling_rate"] = gateway_polling
    iot_settings["wifi_ssid"] = wifi_ssid
    iot_settings["wifi_password"] = wifi_password  # Store securely in production

    return "Settings saved successfully!"