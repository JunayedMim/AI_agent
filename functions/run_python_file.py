import os
import subprocess 
def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory_abspath = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abspath, file_path))
        valid_target_file = os.path.commonpath([working_directory_abspath, target_file])
        if valid_target_file != working_directory_abspath:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif os.path.isfile(target_file) is False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif target_file.endswith(".py") is False:
            return f'Error: "{file_path}" is not a Python file'
        

        command = ["python", target_file]
        if args != None:
            command.extend(args)

        result = subprocess.run(command,
            cwd=working_directory_abspath,
            capture_output=True,
            text=True,
            timeout=30,
        )
        

        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        elif result.stdout == "" and result.stderr == "":
            return "No output produced"
        else:
            return_lines = []
            if result.stdout != "":
                return_lines.append(f"STDOUT: {result.stdout}")
            if result.stderr != "":
                return_lines.append(f"STDERR: {result.stderr}")
            return "\n".join(return_lines)

    except Exception as e:
        return f"Error: executing Python file: {e}"