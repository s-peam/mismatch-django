# Mismatch-django
This code is written in Python and aims to search for specific patterns and extract information from files within a given directory. The code utilizes regular expressions and the YAML module to accomplish its tasks.

## Requirements
- Python installed (version 3 or above)
- pyyaml library installed (to handle YAML parsing)

## Process Overview
**1. Regular Expression Patterns**: The code defines three regular expression patterns:
- **pattern_get**: Matches **os.environ.get(KEY)** calls.
- **pattern_brackets**: Matches **os.environ["KEY"]** calls.
- **pattern_getenv**: Matches **os.getenv("KEY")** calls.

**2. Searching for Key Names in Python Files**:
- The code starts by searching for the specified patterns in all files within the provided directory.
- It recursively walks through all subdirectories, extracts the key names from the matched patterns, and adds them to the **`matching_keys`** list.

**3. Removing Duplicate and Sorting Keys**:
- After collecting the key names, the code removes any duplicate keys using the **`list(set(matching_keys))`** operation.
- Finally, it sorts the keys in ascending order using **`matching_keys.sort()`**.

**4. Searching for Key Names in YAML Files**:
- The code searches for the key names in YAML files (**`.yaml`**) within the specified directory.
- It iterates through the files, parses them using the **`yaml.safe_load`** function, and extracts the key names from the **`environmentVariables`** section.
- The key names found in the YAML files are stored in the **`env_vars`** list.

**5. Comparing and Printing Results**:
- The code compares the key names found in the YAML files (**`env_vars`**) with the key names extracted from the Python files (**`matching_keys`**).
- It generates a list **`main_list`** containing the key names found in the YAML files but not in the Python files.
- The code then prints the list **`main_list`** for each YAML file processed.

## Usage
1. Update the **`directory`** variable in the code to specify the directory path you want to search in.
2. Install the required **`pyyaml`** library (if not already installed) by running **`pip install pyyaml`** in your Python environment.
3. Run the script using Python: **`python main.py`**.

## Results
```
--------------------------------------------
values-qa.yaml
--------------------------------------------
['WEB_CONCURRENCY', 'DJANGO_SETTINGS_MODULE', 'GUNICORN_LOG_LEVEL']
--------------------------------------------
Chart.yaml
--------------------------------------------
[]
--------------------------------------------
values-qa-mm.yaml
--------------------------------------------
['WEB_CONCURRENCY', 'DJANGO_SETTINGS_MODULE', 'GUNICORN_LOG_LEVEL']
```
