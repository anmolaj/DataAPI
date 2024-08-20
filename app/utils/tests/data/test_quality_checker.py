# test_quality_checker.py
import pandas as pd
from app.utils.quality_checker import QualityChecker


def test_duplicate_checker():
    # Create a DataFrame with duplicate rows
    data = pd.DataFrame({"col1": [1, 2, 2, 4], "col2": [5, 6, 6, 8]})

    # Instantiate the QualityChecker
    checker = QualityChecker(data)

    # Call the duplicate_checker method
    duplicates = checker.duplicate_checker()

    # Assert that duplicates are correctly identified
    assert duplicates is not None
    assert duplicates.sum() == 1  # One duplicate row


def test_duplicate_checker_with_subset():
    # Create a DataFrame with duplicate rows
    data = pd.DataFrame({"col1": [1, 2, 2, 4], "col2": [5, 6, 7, 8]})

    # Instantiate the QualityChecker with subset columns
    checker = QualityChecker(data, cols=["col1"])

    # Call the duplicate_checker method
    duplicates = checker.duplicate_checker()

    # Assert that duplicates are correctly identified based on subset
    assert duplicates is not None
    assert duplicates.sum() == 1  # One duplicate row based on 'col1'


def test_no_duplicates():
    # Create a DataFrame with no duplicate rows
    data = pd.DataFrame({"col1": [1, 2, 3, 4], "col2": [5, 6, 7, 8]})

    # Instantiate the QualityChecker
    checker = QualityChecker(data)

    # Call the duplicate_checker method
    duplicates = checker.duplicate_checker()

    # Assert that no duplicates are found
    assert duplicates is None
