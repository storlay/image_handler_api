from fastapi import (
    HTTPException,
    UploadFile,
    status,
)

from app.config.constants import (
    ALLOWED_IMAGE_FILE_FORMATS,
    ALLOWED_WATERMARK_FILE_FORMATS,
)


def validate_image_file_format(file: UploadFile) -> None:
    file_format = file.filename.split(".")[-1].lower()
    check_format("image", file_format, ALLOWED_IMAGE_FILE_FORMATS)


def validate_watermark_file_format(file: UploadFile) -> None:
    file_format = file.filename.split(".")[-1].lower()
    check_format("watermark", file_format, ALLOWED_WATERMARK_FILE_FORMATS)


def check_format(
        file_type: str,
        file_format: str,
        allowed_formats: set[str]
) -> HTTPException | None:
    detail = "Invalid file format for {}: {}. Allowed formats: {}"
    if file_format not in allowed_formats:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail.format(file_type, file_format, ", ".join(allowed_formats))
        )
    return None
