from fastapi import FastAPI, Depends, Security

from app.auth.security import get_api_key
from app.image.handler import handler_image
from app.image.schemas import SImage, SWatermark

app = FastAPI(
    title="Image handler API",
    version="1.0.0",
    root_path="/api"
)


@app.post("/process-image")
async def process_image_endpoint(
        image: SImage = Depends(),
        watermark: SWatermark = Depends(),
        api_key: str = Security(get_api_key)
):
    return await handler_image(image, watermark)
