from dateutil import parser
from dateutil.relativedelta import relativedelta
from datetime import datetime, timezone
import json
import requests

def main():
    repo = "multimedia%2Fkdenlive"

    merge_requests = get_merge_requests(repo)

    for merge_request in filter_last_two_weeks(merge_requests):
        print('- - - -')
        print(f"{merge_request['merged_at']} - {merge_request['title']}\n\n")


def filter_last_two_weeks(merge_requests: list[dict]) -> list[dict]:
    result = []
    two_weeks_ago = datetime.now(timezone.utc) - relativedelta(weeks=2)

    for merge_request in merge_requests:
        merge_request_date = parser.parse(merge_request['merged_at'])
        if merge_request_date > two_weeks_ago:
            result.append(merge_request)

    return result


def get_merge_requests(repo: str) -> list[dict]:
    url = f"https://invent.kde.org/api/v4/projects/{repo}/merge_requests?state=merged"
    return requests.get(url).json()


if __name__ == '__main__':
    main()