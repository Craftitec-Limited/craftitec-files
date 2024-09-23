from os import chmod, mkdir, path


async def store_file(
        file: bytes,
        file_name: str,
        folder: str,
        masking_folder: str
):
    """
    Stores a file onto a folder

    Args:
        file (bytes): The file to be stored, represented in bytes

        file_name (str): The name of the file to store

        folder (str): The name of the folder to store the file to

        masking_folder (str): The name of the folder to be returned

    """
    try:
        if not path.exists(folder):
            mkdir(folder)

        file_path = f"{folder}/{file_name}"
        
        with open(file_path, "wb") as f:
            f.write(file)
            
            chmod(file_path,0o644)
        
        return f"{masking_folder}/{file_name}"
    except Exception as exc:
        raise Exception(str(exc))

