from fastapi import FastAPI, Depends

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
        watermark: SWatermark = Depends()
):
    return await handler_image(image, watermark)
