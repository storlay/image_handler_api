from io import BytesIO

from PIL import ImageSequence
from PIL import Image
from starlette.responses import StreamingResponse

from app.image.schemas import SImage, SWatermark, OutputImageFormat
from app.image.service import ImageService, WatermarkService
from app.image.validators import validate_image_file_format, validate_watermark_file_format


async def handler_image(
        image_info: SImage,
        watermark_info: SWatermark
):
    validate_image_file_format(image_info.image_file)
    watermark_exists = False
    if watermark_info.watermark_file:
        validate_watermark_file_format(watermark_info.watermark_file)
        watermark_exists = True

    image_data = await ImageService.read_image_file(
        image_info.image_file
    )
    if watermark_exists:
        watermark_data = await WatermarkService.read_watermark_file(
            watermark_info.watermark_file
        )

    image = ImageService.open_image(image_data)
    if image_info.output_image_format == OutputImageFormat.gif:
        if watermark_exists:
            frames = [
                process_image(
                    frame, image_info, watermark_info, watermark_data
                )
                for frame in ImageSequence.Iterator(image)
            ]
        else:
            frames = [
                process_image(frame, image_info)
                for frame in ImageSequence.Iterator(image)
            ]
        processed_image_data = ImageService.save_gif(frames)
        media_type = "image/" + OutputImageFormat.gif.value
    else:
        if watermark_exists:
            image = process_image(
                image, image_info, watermark_info, watermark_data
            )
        else:
            image = process_image(
                image, image_info
            )

        image_format = image_info.output_image_format.value
        processed_image_data = ImageService.save_image(
            image, image_info.image_quality, image_format
        )
        media_type = "image/" + image_format
    return StreamingResponse(
        BytesIO(processed_image_data), media_type=media_type
    )


def process_image(
        image: Image.Image,
        image_info: SImage,
        watermark_info: SWatermark = None,
        watermark_data: bytes = None
):
    image = image.convert("RGB")
    if image_info.image_width or image_info.image_height:
        original_width, original_height = image.size
        new_size = (
            image_info.image_width or original_width,
            image_info.image_height or original_height
        )
        image.thumbnail(new_size)

    if watermark_data:
        image = WatermarkService.process_watermark(
            image,
            watermark_data,
            watermark_info.watermark_position.value,
            watermark_info.watermark_transparency
        )
    return image
