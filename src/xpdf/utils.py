import os


def add_suffix_to_filename(file_path, suffix):
    # 分离文件路径和文件名
    directory, filename = os.path.split(file_path)

    # 分离文件名和文件扩展名
    name, extension = os.path.splitext(filename)

    # 构造新的文件名
    new_filename = f"{name}{suffix}{extension}"

    # 构造新的文件路径
    new_file_path = os.path.join(directory, new_filename)

    return new_file_path
