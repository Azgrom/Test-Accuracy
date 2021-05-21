import os
import json
import pandas as pd

# Finds sample data in function of the script folder
script_directory = os.getcwd()
project_directory = os.path.abspath(os.path.join(script_directory,
                             os.pardir))

sample_data_path = f'{project_directory}/data/source_file_2.json'


with open(sample_data_path) as fp:
    data = json.load(fp)


data = pd.DataFrame(data)

managers_columns = ['man1', 'man2']
watchers_columns = ['wat1', 'wat2', 'wat3', 'wat4']

managers = pd.DataFrame(data["managers"].to_list(), columns=managers_columns)

managers = pd.concat([data[:], managers[:]], axis=1)

watchers = pd.DataFrame(managers["watchers"].to_list(), columns=watchers_columns)

watchers = pd.concat([managers[:], watchers[:]], axis=1)

watchers.pop('managers')
watchers.pop('watchers')

data = watchers

manager_dict = {}

for managers in managers_columns:
    for manager in data[managers].value_counts().index.values:
        manager_filter = data[managers] == manager
        filtered_manager_name_list = data[manager_filter]['name']
        manager_dict.update({f'{manager}': list(filtered_manager_name_list.values)})

watchers_dict = {}

for watchers in watchers_columns:
    for watcher in data[watchers].value_counts().index.values:
        watcher_filter = data[watchers] == watcher
        filtered_watcher_name_list = data[manager_filter]['name']
        watchers_dict.update({f'{watcher}': list(filtered_watcher_name_list.values)})


with open('managers.json', 'w') as f:
    details = json.dumps(manager_dict, indent = 5)
    f.write(details)

with open('watchers.json', 'w') as f:
    details = json.dumps(watchers_dict, indent = 5)
    f.write(details)
