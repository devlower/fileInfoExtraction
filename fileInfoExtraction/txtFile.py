import os.path
import pathlib
import chardet
from datetime import datetime


def file_name(file_path: pathlib.Path) -> str:
    return file_path.name


def file_size(file_path: pathlib.Path) -> float:
    return os.path.getsize(file_path) / 1024


def file_creation_time(file_path: pathlib.Path) -> str:
    return datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%d/%m/%Y %H:%M:%S')


def file_modification_time(file_path: pathlib.Path) -> str:
    return datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%d/%m/%Y %H:%M:%S')


def file_access_time(file_path: pathlib.Path) -> str:
    return datetime.fromtimestamp(os.path.getatime(file_path)).strftime('%d/%m/%Y %H:%M:%S')


def file_number_of_lines(file_path: pathlib.Path) -> int:
    with open(file_path, 'rb') as f:
        return len(f.readlines())


def file_number_of_words(file_path: pathlib.Path) -> int:
    with open(file_path, 'rb') as f:
        return sum(len(line.split()) for line in f.readlines())


def file_encoding(file_path: pathlib.Path) -> str:
    with open(file_path, 'rb') as f:
        return chardet.detect(f.read())['encoding']


def full_report(file_path: pathlib.Path) -> str:
    return f'File name: {file_name(file_path)}\nFile size: {file_size(file_path)} kB\nCreation time: {file_creation_time(file_path)}\nModification time: {file_modification_time(file_path)}\nAccess time: {file_access_time(file_path)}\nNumber of lines: {file_number_of_lines(file_path)}\nNumber of words: {file_number_of_words(file_path)}\nEncoding: {file_path}'


print(full_report(pathlib.Path('E:\\your\\file_directory.extension')))


