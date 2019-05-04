# Standard IO streams
import io, sys

print(sys.stdin)
print(sys.stdout)
print(sys.stderr)

print('-' *25)

wrapper = io.TextIOWrapper(sys.stdout, line_buffering=True)
wrapper.write('Hello World')




