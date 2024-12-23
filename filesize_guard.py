import sys
import os
import fnmatch

def load_ignore_patterns(ignore_file):
    with open(ignore_file, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def should_ignore(file, patterns):
    return any(fnmatch.fnmatch(file, pattern) for pattern in patterns)

ignore_file = sys.argv[1]
max_size_kb = int(sys.argv[2])
files = sys.argv[3].split(",")

ignore_patterns = load_ignore_patterns(ignore_file)
exit_code = 0

for file in files:
    if not file:
        continue

    if should_ignore(file, ignore_patterns):
        print(f"Ignoring: '{file}'")
        continue

    print(f"Processing: '{file}'")

    filesize_b = os.path.getsize(file)
    filesize_kb = filesize_b / 1024
    if filesize_kb >= max_size_kb:
        print(f"Error: '{file}' exceeds {max_size_kb} kB ({filesize_kb:.2f} kB)")
        exit_code = 1

sys.exit(exit_code)
