from pydantic import BaseModel
from enum import Enum


class FileType(str, Enum):
    csv = "csv"

class FileModel(BaseModel):
    type: FileType