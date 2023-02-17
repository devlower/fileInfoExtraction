from fileInfoExtraction import (
    file_access_time,
    file_creation_time,
    file_encoding,
    file_modification_time,
    file_name,
    file_number_of_lines,
    file_number_of_words,
    file_size,
    full_report,
    hash_file,
)


def test_file_name_function_return():
    """Input date/time value is invalid"""
    assert type(file_name("../file-icon.png")) == str
