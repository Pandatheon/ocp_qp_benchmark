"""I/O utility functions."""

import json
import os


def load_data(json_path: str) -> dict:
    """
    Load meta data from the meta.json file for a given problem folder.

    Args:
        qp_folder_path: Path to the QP problem folder.

    Returns:
        Dictionary containing the meta data.
    """
    with open(json_path, "r") as f:
        return json.load(f)