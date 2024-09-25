from typing import List
from json import loads
import pandas as pd
import io

from .errors import CustomException

async def match_columns(
        input_columns: List[str],
        df_columns: List[str]
):
    try:
        for column in input_columns:
            if column.strip() not in df_columns:
                raise CustomException(
                    f"Invalid request; Expected: '{column}'",
                    "invalid_request",
                    400
                )
    except CustomException as exc:
        raise exc
    except Exception as exc:
        raise CustomException(
            str(exc),
            "internal_server_error",
            500
        )


async def read_from_file(
        filename: str,
        content: bytes,
        columns: List[str]
        ):
    """
        Reads data from a file and stores it in
        a pandas dataframe object

        Args:

        filename (str): The name of the file to be read
        content (bytes): The content of the file in bytes
        columns (list): A list of the columns to be expected
    """
    try:
        file_split = filename.split(".")
        
        if file_split[-1] not in ["xlsx","csv"]:
            raise CustomException(
                "Invalid file format",
                "invalid_request",
                400
            )
        
        if file_split[-1] == "csv":
            string_io = io.StringIO(content.decode("utf-8"))
            mass_entries = pd.read_csv(string_io, skipinitialspace=True,engine="python",sep=' *, *')
            
            await match_columns(columns,mass_entries.columns.tolist())
            return mass_entries
        if file_split[-1] == "xlsx":
            string_io = io.BytesIO(content)
            mass_entries = pd.read_excel(string_io)

            await match_columns(columns,mass_entries.columns.tolist())

            return mass_entries
    except FileNotFoundError:
        raise Exception(
                "File not found",
                "not_found",
                404
        )
    except CustomException as exc:
        raise exc
    except Exception as exc:
        raise CustomException(
            str(exc),
            "internal_server_error",
            500
        )


async def parse_to_json(mass_entries: pd.DataFrame):
    try:
        mass_entries_json = mass_entries.to_json(orient='records')
        json_obj = loads(mass_entries_json)
        return json_obj
    except CustomException as exc:
        raise exc
    except Exception as exc:
        raise CustomException(
            str(exc),
            "internal_server_error",
            500
        )
