from aiologger.formatters.json import (
    FUNCTION_NAME_FIELDNAME,
    ExtendedJsonFormatter,
    LOG_LEVEL_FIELDNAME,
)
from aiologger.handlers.files import AsyncFileHandler
from fastapi import FastAPI
from pydantic import BaseModel
import logging
from aiologger.loggers.json import JsonLogger

app = FastAPI()

logger = JsonLogger.with_default_handlers(
    level=logging.INFO,
    serializer_kwargs={"indent": 4, "ensure_ascii": False},
)
file_handler = AsyncFileHandler(filename="logs.txt", encoding="utf-8")
file_handler.formatter = ExtendedJsonFormatter(
    exclude_fields=[
        FUNCTION_NAME_FIELDNAME,
        LOG_LEVEL_FIELDNAME,
        "file_path",
        "line_number",
    ]
)
logger.handlers = [file_handler]


class Message(BaseModel):
    message: str


@app.post("/")
async def echo(message: Message):
    await logger.info(message.message)
    return {"echo": message.message}
