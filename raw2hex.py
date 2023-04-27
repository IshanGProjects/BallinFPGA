import os

def raw_to_hex(input_file, output_file):
    with open(input_file, "rb") as raw_file, open(output_file, "w") as hex_file:
        byte = raw_file.read(1)
        while byte:
            hex_file.write(f"{ord(byte):02x}\n")
            byte = raw_file.read(1)

if __name__ == "__main__":
    input_file = "4g.raw"
    output_file = "4g.hex"
    raw_to_hex(input_file, output_file)