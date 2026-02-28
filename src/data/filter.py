from typing import List, Dict


def normalise(raw_data: List[Dict], desired_fields: List[str]) -> List[Dict]:
    """
    Filter desired fields from a list of group dictionaries.

    Args:
        raw_data (List[Dict]): Raw list of group dictionaries from the API.
        desired_fields (List[str]): Names of fields to keep in each dictionary.

    Returns:
        List[Dict]: List of dictionaries containing only the desired fields.

    Raises:
        ValueError: If 'desired_fields' is missing or empty.
    """
    if not desired_fields:
        raise ValueError("'desired_fields' list is missing or empty")

    return [{field: item.get(field) for field in desired_fields} for item in raw_data]