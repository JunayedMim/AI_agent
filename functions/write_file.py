import os
def write_file(working_directory, file_path, content):
    try:
        working_directory_abspath = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abspath, file_path))
        valid_target_file = os.path.commonpath([working_directory_abspath, target_file])
        if valid_target_file != working_directory_abspath:
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        elif os.path.isdir(target_file) is True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        file_directory = os.path.dirname(target_file)
        os.makedirs(file_directory, exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"