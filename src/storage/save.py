import json
from typing import List, Dict


def write_json(data: List[Dict], filepath: str) -> None:
    """
    Save filtered data to a JSON file.

    Args:
        data (List[Dict]): List of filtered dictionaries.
        filepath (str): Path where the JSON file should be written.

    Returns:
        None
    """
    with open(filepath, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)
    print(f"Saved {len(data)} entries to {filepath}")