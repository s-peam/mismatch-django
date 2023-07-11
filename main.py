import os
import re
import yaml

# Specify the directory to search
directory = "./"

# Regular expression patterns to match os.environ.get(KEY), os.environ["KEY"], and os.getenv("KEY")
pattern_get = re.compile(r"os\.environ\.get\((.*?)(?:,|\))")
pattern_brackets = re.compile(r"os\.environ\[(.*?)\]")
pattern_getenv = re.compile(r"os\.getenv\((.*?)(?:,|\))")

# List to store the matching keys
matching_keys = []

# Iterate over all files in the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)

            # Open the file and search for os.environ.get, os.environ, and os.getenv calls
            with open(file_path, "r") as f:
                content = f.read()
                matches_get = pattern_get.findall(content)
                matches_brackets = pattern_brackets.findall(content)
                matches_getenv = pattern_getenv.findall(content)
                matching_keys.extend([match.strip('\'"') for match in matches_get])
                matching_keys.extend([match.strip('\'"') for match in matches_brackets])
                matching_keys.extend([match.strip('\'"') for match in matches_getenv])

# Remove duplicate keys
matching_keys = list(set(matching_keys))
matching_keys.sort()

# Specify the directory to search
directory = "deployments/kubernetes/helm/"

# List to store the matching keys

# Iterate over all files in the directory
for root, dirs, files in os.walk(directory):
    if root == directory:
        for file in files:
            env_vars = []
            print('--------------------------------------------')
            print(file)
            print('--------------------------------------------')
            if file.endswith(".yaml"):
                file_path = os.path.join(root, file)

                # Open the file and search for environmentVariables key names
                with open(file_path, "r") as f:
                    try:
                        data = yaml.safe_load(f)
                        environment_variables = data.get("environmentVariables", [])
                        # print(file_path,environment_variables)
                        # if not environment_variables:
                        #     continue
                        for env_var in environment_variables:
                            key = env_var.get("name")
                            if key:
                                # print(key)
                                env_vars.append(key)
                    except yaml.YAMLError as e:
                        print(f"Error parsing YAML file: {file_path}")
                        print(e)
            main_list = list(set(env_vars)-set(matching_keys))
            print(main_list)
