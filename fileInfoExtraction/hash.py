import hashlib
from pathlib import Path

def hash_file(file_path, algorithm='sha256') -> str:

    BUFSIZE = 65536
    hasher = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        buf = f.read(BUFSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(BUFSIZE)
    return hasher.hexdigest()

print(hash_file(Path('D:\\d_desktop\\CC\\thesea\\casoPratico01TentativaPhishing_Email_Header.txt'), 'md5'))





