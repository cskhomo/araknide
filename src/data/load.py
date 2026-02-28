import json
from typing import Dict


def read_json(path: str) -> Dict:
    """
    Read configuration from a JSON file.

    Args:
        path (str): Path to the configuration JSON file.

    Returns:
        Dict: The loaded configuration.
    """
    with open(path, encoding='utf-8') as config_file:
        return json.load(config_file)