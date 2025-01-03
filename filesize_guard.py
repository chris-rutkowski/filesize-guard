import os
import fnmatch
import json
import sys

def load_ignore_patterns(ignore_file):
    with open(ignore_file, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def should_ignore(file, patterns):
    return any(fnmatch.fnmatch(file, pattern) for pattern in patterns)

def load_files_from_json(file_paths):
    files = []
    for file_path in file_paths:
        with open(file_path, "r") as f:
            files.extend(json.load(f))
    return files

ignore_patterns = load_ignore_patterns(sys.argv[1])
max_size_kb = int(sys.argv[2])
files = load_files_from_json(sys.argv[3:])

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
        print(f"Error: '{file}' is {filesize_kb:.2f} kB, which exceeds the allowed limit of {max_size_kb} kB.")
        exit_code = 1

sys.exit(exit_code)
