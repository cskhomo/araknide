import requests
import time
from typing import List, Dict


def set_parameters(per_page: int, page: int) -> Dict:
    """
    Set query parameters for a GitLab API request for a page of groups.

    Args:
        per_page (int): Number of items per page.
        page (int): Page number to fetch.

    Returns:
        Dict: Dictionary of query parameters for the request.
    """
    return {
        'per_page': per_page,
        'page': page,
        'top_level_only': 'true'
    }


def fetch_page(url: str, params: Dict) -> List[Dict]:
    """
    Fetch a single page of groups from the GitLab API.

    Args:
        url (str): The full API URL for fetching groups.
        params (Dict): Query parameters for the request.

    Returns:
        List[Dict]: List of groups returned by the API.
        Returns an empty list if the request fails.
    """
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Error {response.status_code} on page {params['page']}: {response.text.strip()}")
        return []
        
    return response.json()


def get_groups(base_url: str, per_page: int) -> List[Dict]:
    """
    Fetch all top-level groups from GitLab across all pages.

    Args:
        base_url (str): Full API endpoint URL for groups.
        per_page (int): Number of items to request per page.

    Returns:
        List[Dict]: Combined list of all groups across all pages.
    """
    groups = []
    page = 1

    while True:
        params = set_parameters(per_page, page)
        data = fetch_page(base_url, params)

        if not data: break

        groups.extend(data)
        print(f"Page {page}: {len(data)} entries fetched")
        
        page += 1
        time.sleep(0.5)

    return groups