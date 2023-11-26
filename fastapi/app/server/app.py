from fastapi import FastAPI
from server.routes.water import router as WaterRouter
from server.routes.integrate_water import router as IntegrateRouter
from server.routes.mqtt_water import router as IntegrateMQTTRouter
from server.mqtt.sensor_data import router as MqttRouter
from server.mockup.get_mockup import router as MockRouter
from server.mockup.get_2021 import router as Y2021Router
from server.mockup.get_2022 import router as Y2022Router
from server.mockup.get_2023 import router as Y2023Router

app = FastAPI()

####router api part

app.include_router(MqttRouter, tags=["MQTT"],prefix="/khiwqq")
app.include_router(MockRouter, tags=["Mockup"],prefix="/mockup")
# app.include_router(Y2021Router, tags=["Retrieved Data 2021"],prefix="/2021")
# app.include_router(Y2022Router, tags=["Retrieved Data 2022"],prefix="/2022")
# app.include_router(Y2023Router, tags=["Retrieved Data 2023"],prefix="/2023")
# app.include_router(WaterRouter, tags=["Water"], prefix="/water") // EX by AJ

app.include_router(IntegrateMQTTRouter, tags=["Integrate MQTT"], prefix="/integrate/mqtt")
app.include_router(IntegrateRouter, tags=["Integrate"], prefix="/integrate")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "My REST API server!"}