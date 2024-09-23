from json import loads
import pandas as pd
import io

async def read_from_file(
        filename: str,
        content: bytes
        ):
    """
        Reads data from a file and stores it in
        a pandas dataframe object

        Args:

        filename (str): The name of the file to be read
        content (bytes): The content of the file in bytes
    """
    try:
        file_split = filename.split(".")
        
        if file_split[-1] not in ["xlsx","csv"]:
            raise Exception({
                "error":"Invalid file format",
                "tag":"invalid"
            })
        
        if file_split[-1] == "csv":
            string_io = io.StringIO(content.decode("utf-8"))
            mass_entries = pd.read_csv(string_io, skipinitialspace=True,engine="python",sep=' *, *')
        
            return mass_entries
        if file_split[-1] == "xlsx":
            string_io = io.BytesIO(content)
            mass_entries = pd.read_excel(string_io)

            return mass_entries
    except FileNotFoundError:
        raise Exception({
                "error":"File not found",
                "tag":"not_found"  
        })
    except Exception as exc:
        raise Exception({
            "error":str(exc),
            "tag":"internal_server_error"
        })


async def parse_to_json(mass_entries: pd.DataFrame):
    try:
        mass_entries_json = mass_entries.to_json(orient='records')
        json_obj = loads(mass_entries_json)
        return json_obj
    except Exception as exc:
        raise Exception({
            "error":str(exc),
            "tag":"internal_server_error"
        })
