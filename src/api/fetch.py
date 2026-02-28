import requests
import time
from typing import List, Dict


def fetch_all(url: str, per_page: int) -> List[Dict]:
    """
    Fetch all pages from a paginated GitLab endpoint.

    Args:
        url (str): Full API endpoint URL.
        per_page (int): Items per page.

    Returns:
        List[Dict]: Combined results from all pages.
    """
    results = []
    page = 1

    while True:
        params = set_parameters(per_page, page)
        data = fetch_page(url, params)

        if not data:
            break

        results.extend(data)
        print(f"Page {page}: {len(data)} entries fetched")

        page += 1
        time.sleep(0.5)

    return results
    

def set_parameters(per_page: int, page: int) -> Dict:
    """
    Build query parameters for a paginated GitLab API request.

    Args:
        per_page (int): Number of items per page.
        page (int): Page number.

    Returns:
        Dict: Query parameters dictionary.
    """
    return {
        "per_page": per_page,
        "page": page,
        "top_level_only": "true"
    }


def fetch_page(url: str, params: Dict) -> List[Dict]:
    """
    Fetch a single page from a GitLab API endpoint.

    Args:
        url (str): Full API endpoint URL.
        params (Dict): Query parameters.

    Returns:
        List[Dict]: API results for that page. Empty list if failed.
    """
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Error {response.status_code} on page {params['page']}: {response.text.strip()}")
        return []

    return response.json()