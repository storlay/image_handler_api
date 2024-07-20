from io import BytesIO

from PIL import Image, ImageEnhance
from fastapi import UploadFile


class ImageService:
    @staticmethod
    async def read_image_file(image_file: UploadFile) -> bytes:
        return await image_file.read()

    @staticmethod
    def open_image(data: bytes) -> Image.Image:
        return Image.open(BytesIO(data))

    @staticmethod
    def save_image(
            image: Image.Image,
            quality: int,
            file_format: str
    ) -> bytes:
        output = BytesIO()
        image.save(output, format=file_format, quality=quality)
        output.seek(0)
        return output.read()

    @staticmethod
    def save_gif(frames: list) -> bytes:
        output = BytesIO()
        frames[0].save(
            output, format='GIF', save_all=True, append_images=frames[1:], loop=0
        )
        output.seek(0)
        return output.read()


class WatermarkService:
    @staticmethod
    async def read_watermark_file(watermark_file: UploadFile) -> bytes | None:
        if watermark_file:
            return await watermark_file.read()
        return None

    @staticmethod
    def process_watermark(
            image: Image.Image,
            watermark_data: bytes,
            position: str,
            transparency: float
    ) -> Image.Image:
        watermark_image = Image.open(BytesIO(watermark_data))
        watermark_width, watermark_height = watermark_image.size
        image_width, image_height = image.size

        if watermark_width > image_width or watermark_height > image_height:
            watermark_image.thumbnail((image_width, image_height))

        alpha = watermark_image.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(transparency)
        watermark_image.putalpha(alpha)

        positions = {
            "center": ((image.width - watermark_image.width) // 2, (image.height - watermark_image.height) // 2),
            "top-left": (0, 0),
            "top-right": (image.width - watermark_image.width, 0),
            "bottom-left": (0, image.height - watermark_image.height),
            "bottom-right": (image.width - watermark_image.width, image.height - watermark_image.height)
        }

        position = positions.get(position, positions["center"])
        image.paste(watermark_image, position, watermark_image)
        return image
