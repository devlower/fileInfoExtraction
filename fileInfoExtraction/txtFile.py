import os.path
from pathlib import Path
import chardet
from datetime import datetime


def file_name(file_path: str) -> str:
    return Path(file_path).name


def file_size(file_path: str) -> float:
    return os.path.getsize(Path(file_path)) / 1024


def file_creation_time(file_path: str) -> str:
    return datetime.fromtimestamp(os.path.getctime(Path(file_path))).strftime('%d/%m/%Y %H:%M:%S')


def file_modification_time(file_path: str) -> str:
    return datetime.fromtimestamp(os.path.getmtime(Path(file_path))).strftime('%d/%m/%Y %H:%M:%S')


def file_access_time(file_path: str) -> str:
    return datetime.fromtimestamp(os.path.getatime(Path(file_path))).strftime('%d/%m/%Y %H:%M:%S')


def file_number_of_lines(file_path: str) -> int:
    with open(Path(file_path), 'rb') as f:
        return len(f.readlines())


def file_number_of_words(file_path: str) -> int:
    with open(Path(file_path), 'rb') as f:
        return sum(len(line.split()) for line in f.readlines())


def file_encoding(file_path: str) -> str:
    with open(Path(file_path), 'rb') as f:
        return chardet.detect(f.read())['encoding']


def full_report(file_path: str) -> str:
    return f'File name: {file_name(Path(file_path))}\nFile size: {file_size(Path(file_path))} kB\nCreation time: {file_creation_time(Path(file_path))}\nModification time: {file_modification_time(Path(file_path))}\nAccess time: {file_access_time(Path(file_path))}\nNumber of lines: {file_number_of_lines(Path(file_path))}\nNumber of words: {file_number_of_words(Path(file_path))}\nEncoding: {Path(file_path)}'


print(full_report('/mnt/d/d_desktop/chata/chata.jpg'))


