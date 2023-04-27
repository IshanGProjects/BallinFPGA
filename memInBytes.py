import os
import math

def get_file_size(file_path):
    return os.path.getsize(file_path)

if __name__ == "__main__":
    file_path = "4g.hex"
    file_size = get_file_size(file_path)
    print(f"File size: {file_size} bytes")
    print(math.ceil(math.log2(file_size)))
