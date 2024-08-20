from pandas import read_csv, DataFrame

from ..model.file_model import FileType


class Reader:
    def __init__(self, format: FileType = FileType.csv):
        self.format: str = format

    def read(self, file_path) -> DataFrame:
        """
        Read a file based on the file format
        """
        reader = Reader._general_reader(self.format)
        print(reader)
        return reader(file_path)
    
    def _general_reader(type: FileType):
        """
        Factory method to read a file based on the file type
        """
        if type == FileType.csv:
            return read_csv
        else:
            raise ValueError("Unsupported file type")