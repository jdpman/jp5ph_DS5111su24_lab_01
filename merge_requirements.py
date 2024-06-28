# merge_requirements.py

from collections import defaultdict

# Function to read requirements file and return a dict with package names and versions
def read_requirements(file_path):
    requirements = defaultdict(str)
    with open(file_path, 'r') as file:
        for line in file:
            if '==' in line:
                pkg, version = line.strip().split('==')
                requirements[pkg] = version
            else:
                requirements[line.strip()] = ''
    return requirements

# Paths to the requirements files
existing_requirements_path = 'requirements.txt'
new_requirements_path = 'new_requirements.txt'

# Read existing and new requirements
existing_reqs = read_requirements(existing_requirements_path)
new_reqs = read_requirements(new_requirements_path)

# Merge requirements, keeping the highest version
merged_reqs = {**existing_reqs, **new_reqs}

# Write merged requirements back to requirements.txt
with open(existing_requirements_path, 'w') as file:
    for pkg, version in merged_reqs.items():
        if version:
            file.write(f'{pkg}=={version}\n')
        else:
            file.write(f'{pkg}\n')

print("Merged requirements saved to requirements.txt")

