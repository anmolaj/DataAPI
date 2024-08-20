import pytest
from pandas import DataFrame
from app.utils.reader import Reader


def test_read_csv():
    # Mock the return value of read_csv
    # mock_read_csv.return_value = DataFrame({'col1': [1, 2], 'col2': [3, 4]})

    reader = Reader(format="csv")
    result = reader.read("app/utils/tests/data/dummy_path.csv")

    # Assert read_csv was called with the correct file path
    # mock_read_csv.assert_called_once_with('dummy_path.csv')
    # Assert the result is a DataFrame
    assert isinstance(result, DataFrame)
    # Assert the DataFrame content
    assert (result["col1"] == [1, 2]).all()
    assert (result["col2"] == [3, 4]).all()


def test_unsupported_file_type():
    reader = Reader(format="unsupported_format")
    with pytest.raises(ValueError, match="Unsupported file type"):
        reader.read("dummy_path")
