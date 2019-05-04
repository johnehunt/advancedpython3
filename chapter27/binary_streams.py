import io, os

print('In memory Binary Streams')
binary_stream = io.BytesIO()
print('binary_stream', binary_stream)

# Binary data and strings are different types, so a str
# must be encoded to binary using ascii, utf-8, or other.
binary_stream.write("Hello, world!\n".encode('ascii'))

# Move cursor back to the beginning of the buffer
binary_stream.seek(0)

# Read all data from the stream
stream_data = binary_stream.read()

# The stream_data is type 'bytes', immutable
print(type(stream_data))
print(stream_data)

# To modify the actual contents of the existing buffer
# use getbuffer() to get an object you can modify.
# Modifying this object updates the underlying BytesIO buffer
mutable_buffer = binary_stream.getbuffer()
print(type(mutable_buffer))  # class 'memoryview'
mutable_buffer[0] = 0xEF

# Re-read the original stream. Contents will be modified
# because we modified the mutable buffer
binary_stream.seek(0)
print(binary_stream.read())

print('-' * 25)

print('File based binary stream')

# Binary IO aka Buffered IO
binary_stream_from_file = io.BufferedReader(io.BytesIO(b'starship.png'))
print('f3', binary_stream_from_file)
print('f3.read()', binary_stream_from_file.read()) # Read the whole of the file
file_length_in_bytes = os.path.getsize('starship.png')
print('file_length_in_bytes', file_length_in_bytes)
binary_stream_from_file.seek(0, 0) # Go to the start fo the file
bytes = binary_stream_from_file.read(4)
print(bytes)


