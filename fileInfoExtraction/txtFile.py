import os.path
import re
from datetime import datetime
from pathlib import Path

import chardet
import magic


def file_name(file_path: str) -> str:
    """
    Return the file name from a given file path.
    
    Parameters
    ----------
    file_path : str
        The path to the file.
    
    Returns
    -------
    str
        The name of the file.
    """
    return Path(file_path).name




def file_type(file_path: str) -> any:
    """
    Get the type of the file specified by `file_path`.
    
    Parameters
    ----------
    file_path : str
        The path of the file whose type is to be determined.
    
    Returns
    -------
    str
        A string representing the type of the file.
    
    Notes
    -----
    This function uses the `magic` library to determine the file type. The `magic` library reads the 
    file contents and determines the file type based on the contents. 
    
    Examples
    --------
    Get the type of a file:
    >>> file_type("/path/to/file.txt")
    'ASCII text'
    """
    magic_db_path = "/usr/share/misc/magic.mgc"
    magic_obj = magic.Magic(magic_file=magic_db_path)
    return magic_obj.from_file(Path(file_path))


def file_size(file_path: str) -> float:
    """
    Get the size of a file in kilobytes (KB).
    
    Parameters
    ----------
    file_path : str
        The path to the file.
        
    Returns
    -------
    float
        The file size in kilobytes (KB).
        
    Example
    -------
    >>> file_size('/path/to/file.txt')
    1024.0
    """
    return os.path.getsize(Path(file_path)) / 1024


def file_creation_time(file_path: str) -> str:
    """Return a formatted string representing the creation time of a file.

    Parameters
    ----------
    file_path : str
        Path to the file.

    Returns
    -------
    str
        A formatted string representing the creation time of the file in the format "dd/mm/yyyy hh:mm:ss".

    """
    return datetime.fromtimestamp(os.path.getctime(Path(file_path))).strftime(
        "%d/%m/%Y %H:%M:%S"
    )


def file_modification_time(file_path: str) -> str:
    """
    Returns the modification time of a file in a human-readable string format.

    Parameters
    ----------
    file_path : str
        The path to the file to get the modification time for.

    Returns
    -------
    str
        A string representing the modification time of the file, in the format "DD/MM/YYYY HH:MM:SS".

    Examples
    --------
    >>> file_modification_time("path/to/myfile.txt")
    '13/02/2023 15:21:35'
    """
    return datetime.fromtimestamp(os.path.getmtime(Path(file_path))).strftime(
        "%d/%m/%Y %H:%M:%S"
    )


def file_access_time(file_path: str) -> str:
    return datetime.fromtimestamp(os.path.getatime(Path(file_path))).strftime(
        "%d/%m/%Y %H:%M:%S"
    )


def file_number_of_lines(file_path: str) -> int:
    with open(Path(file_path), "rb") as f:
        return len(f.readlines())


def file_number_of_words(file_path: str) -> int:
    with open(Path(file_path), "rb") as f:
        return sum(len(line.split()) for line in f.readlines())


def file_encoding(file_path: str) -> str:
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read())
        return result["encoding"]


def find_keywords(file_path, keywords: list[str]):
    with open(Path(file_path), "r", encoding=file_encoding(file_path)) as f:
        contents = f.read()

    for keyword in keywords:
        matches = re.findall(keyword.upper(), contents.upper())
        if matches:
            print(
                f"\nFound {len(matches)} occurences of '{keyword}' keyword in file: {file_name(file_path)}\n"
            )
            line_num = 0
            for line in contents.split("\n"):
                line_num += 1
                if keyword.upper() in line.upper():
                    print(f"'{keyword}' keyword found on line {line_num}: '{line}'\n")
        else:
            print(f"\nNo occurrences of '{keyword}' keyword found in {file_name(file_path)}\n")


def full_report(file_path: str) -> str:
    report = f"File name: {file_name(file_path)}\nFile type: {file_type(file_path)}\nFile size: {file_size(file_path)} KB\nCreation time: {file_creation_time(file_path)}\nModification time: {file_modification_time(file_path)}\nAccess time: {file_access_time(file_path)}\nNumber of lines: {file_number_of_lines(file_path)}\nNumber of words: {file_number_of_words(file_path)}\nEncoding: {file_encoding(file_path)}"
    return report


file_path = "/mnt/d/d_desktop/cc/thesea/casoPratico01TentativaPhishing_Email_Header.txt"
find_keywords(file_path, ["bitcoin", "wallet"])

# print(
#     full_report(
#         "/mnt/d/d_desktop/cc/thesea/casoPratico01TentativaPhishing_Email_Header.txt"
#     )
# )
