import hashlib

BUFSIZE = 65536


def hash_file(file_path: str, algorithm: str = "sha256") -> str:
    hasher = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        buf = f.read(BUFSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(BUFSIZE)
    return str(hasher.hexdigest())
