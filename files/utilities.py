from json import loads
import pandas as pd
import numpy as np
from io import BytesIO

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
        bytes_io = BytesIO(content)
        if filename.endswith(".xlsx"):
            mass_entries = pd.read_excel(content, engine='openpyxl')
        elif filename.endswith(".csv"):
            mass_entries = pd.read_csv(content, engine='c')
        else:
            raise Exception({
                "error":"Invalid file format",
                "tag":"invalid"
            })
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