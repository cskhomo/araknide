from config import config_reader
from api import fetch
from storage import filter, save

GROUPS_CONFIG_FILE = "config/groups_config.json"


def main():
    
    print("Starting KDE top-level groups fetch...")
    configuration = config_reader.load_config(GROUPS_CONFIG_FILE)
    
    base_url = configuration['base_url']
    per_page = configuration['per_page']
    groups_file = configuration['groups_file']
    desired_fields = configuration.get('desired_fields', [])

    groups = fetch.get_groups(base_url, per_page)
    filtered_groups = filter.normalise(groups, desired_fields)
    save.write_json(filtered_groups, groups_file)

    print("Done.")


if __name__ == "__main__":
    main()