import os
def get_files_info(working_directory, directory= "."):
    try:

        working_directory_abspath = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abspath, directory))
        valid_target_dir = os.path.commonpath([working_directory_abspath, target_dir])
        if valid_target_dir != working_directory_abspath:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif os.path.isdir(target_dir) is False:
            return f'Error: "{directory}" is not a directory'
        else:
            files_info_list = []
            list_of_items_dir = os.listdir(target_dir)
            for item in list_of_items_dir:
                item_path = os.path.join(target_dir, item)
                item_size = os.path.getsize(item_path)
                item_is_dir = os.path.isdir(item_path)
                item_info = f"- {item}: file_size={item_size} bytes, is_dir={item_is_dir}"
                files_info_list.append(item_info)

            files_info = "\n".join(files_info_list)
            return files_info
    except Exception as e:
        return f"Error: {e}"
