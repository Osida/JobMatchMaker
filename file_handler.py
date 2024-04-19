# Handles file reading and writing operations

# Version Control: When managing file versions, handle potential conflicts or errors in version numbering.

import os.path


def read_file(file_path):
    # Existing function to read file content
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"


def save_to_file(content, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as io_err:
        print(f"An I/O error occurred: {io_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def get_next_version_number(directory, base_filename):
    version = 1

    while os.path.exists(os.path.join(directory, f"{base_filename}_v{version}.txt")):
        version += 1
    return version
