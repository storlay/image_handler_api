from enum import Enum
from typing import Optional

from fastapi import Form, UploadFile
from pydantic import BaseModel

from app.config.constants import WATERMARK_TRANSPARENCY, IMAGE_QUALITY


class WatermarkPosition(Enum):
    center = "center"
    top_left = "top-left"
    top_right = "top-right"
    bottom_left = "bottom-left"
    bottom_right = "bottom-right"


class OutputImageFormat(Enum):
    jpeg = "jpeg"
    png = "png"
    gif = "gif"
    webp = "webp"


class SImage(BaseModel):
    image_file: UploadFile
    image_width: Optional[int] = Form(None)
    image_height: Optional[int] = Form(None)
    image_quality: Optional[int] = Form(IMAGE_QUALITY)
    output_image_format: OutputImageFormat = Form(OutputImageFormat.jpeg)


class SWatermark(BaseModel):
    watermark_file: Optional[UploadFile] = Form(None)
    watermark_position: Optional[WatermarkPosition] = Form(WatermarkPosition.center)
    watermark_transparency: Optional[float] = Form(WATERMARK_TRANSPARENCY)
