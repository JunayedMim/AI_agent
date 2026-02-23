import os
from config import *
def get_file_content(working_directory, file_path):
    try:

        working_directory_abspath = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abspath, file_path))
        valid_target_file = os.path.commonpath([working_directory_abspath, target_file])
        if valid_target_file != working_directory_abspath:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif os.path.isfile(target_file) is False:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        

        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"

