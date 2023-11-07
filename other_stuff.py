import struct

def get_png_dimensions(file_path):
    with open(file_path, "rb") as file:
        # PNG files start with a signature of 8 bytes
        # Read the first 24 bytes to get the header information
        header = file.read(24)

        # Check if the file has a valid PNG signature
        if header.startswith(b'\x89PNG\r\n\x1a\n'):
            # Extract width and height from the header
            width = int.from_bytes(header[16:20], byteorder='big')
            height = int.from_bytes(header[20:24], byteorder='big')
            return width, height
        else:
            raise ValueError("Invalid PNG file")

def get_jpeg_dimensions(file_path):
    with open(file_path, "rb") as file:
        # Check for JPEG start marker
        if file.read(2) == b'\xFF\xD8':
            while True:
                # Find the next marker
                marker, = struct.unpack('!H', file.read(2))
                length, = struct.unpack('!H', file.read(2))
                # SOF markers (Start Of Frame) contain the width and height
                if 0xFFC0 <= marker <= 0xFFCF and marker != 0xFFC4 and marker != 0xFFC8:
                    file.read(1)  # Skip precision byte
                    height, width = struct.unpack('!HH', file.read(4))
                    return width, height
                # Move to the next marker
                file.seek(length - 2, 1)
        else:
            raise ValueError("Invalid JPEG file")