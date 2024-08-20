from pandas import DataFrame
from typing import List


class QualityChecker:
    def __init__(self, data: DataFrame, cols: List[str] = None):
        self.data = data
        self.cols = cols

    def duplicate_checker(self) -> DataFrame:
        """
        Check for duplicate rows in the data
        """
        if self.cols and len(self.cols) > 0:
            duplicates = self.data.duplicated(subset=self.cols)
        else:
            duplicates = self.data.duplicated()

        if duplicates.any():
            return duplicates
        return None
    
    def missing_checker(self) -> DataFrame:
        """
        Check for missing values in the data
        """
        missing_value_df = self.data.isnull()
        if missing_value_df.sum().any():
            return missing_value_df
        return None
