READ_MODE = 'r'
WRITE_MODE = 'w'


def load_file_content(file_path):
    if file_path is None:
        print('No file path provided')
        return None

    try:
        with open(file_path, READ_MODE) as file:
            return file.read()
    except FileNotFoundError:
        print('File not found')
        return None


def print_file_content(file_content, file_type):
    if file_content is not None:
        print(f'{file_type} file content:\n{file_content[:100]}')
    else:
        print(f'No {file_type} file provided. Please provide a valid path to the {file_type} file.')

# def save_content_to_file(content, file_path):
#     try:
#         with open(file_path, WRITE_MODE) as file:
#             file.write(content)
#     except IOError as io_err:
#         print(f'An I/O error occurred: {io_err}')
#         return False
#     except Exception as e:
#         print(f'An unexpected error occurred: {e}')
#         return False
#     return True
#
# def get_next_version_number(directory, base_filename):
#     version = 1
#     while os.path.exists(os.path.join(directory, f'{base_filename}_v{version}.txt')):
#         version += 1
#     return version
#
# def save_to_file_output(content, directory, base_filename, version=None):
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     filename = f'{base_filename}_v{version}.txt' if version is not None else f'{base_filename}.txt'
#     filepath = os.path.join(directory, filename)
#     with open(filepath, WRITE_MODE) as file:
#         file.write(content)
#     print(f'Saved: {filepath}')
#
# resume_content = 'Your updated resume content here'
# save_content_to_file(resume_content, 'resumes', 'john_doe_resume', version=1)
