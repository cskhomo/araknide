from api import fetch
from data import load, filter, dump

base_url = None
groups_file = None
projects_file = None

def main():

    groups_config = load.read_json("config/groups_config.json")
    projects_config = load.read_json("config/projects_config.json")
    init_globals(groups_config, projects_config)

    get_groups(groups_config["per_page"], groups_config.get("desired_fields", []),)
    get_projects(projects_config["per_page"], projects_config.get("desired_fields", []),)


def init_globals(groups_config, projects_config):

    global base_url, groups_file, projects_file

    base_url = groups_config["base_url"]
    groups_file = groups_config["save_file"]
    projects_file = projects_config["save_file"]


def get_groups(per_page, desired_fields):

    print("Fetching groups...")

    groups = fetch.fetch_all(base_url, per_page)
    filtered = filter.normalise(groups, desired_fields)

    dump.write_json(filtered, groups_file)

    print("Groups done.")


def get_projects(per_page, desired_fields):

    print("Fetching projects...")

    groups = load.read_json(groups_file)

    all_projects = []

    for group in groups:

        group_id = group["id"]
        projects_url = f"{base_url}/{group_id}/projects"

        projects = fetch.fetch_all(projects_url, per_page)
        all_projects.extend(projects)

    filtered = filter.normalise(all_projects, desired_fields)
    dump.write_json(filtered, projects_file)

    print("Projects done.")


if __name__ == "__main__":
    main()