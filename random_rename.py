import os
import random
import json
from pathlib import Path

def random_rename_files(directory):
    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Create a mapping of new names to original names
    name_mapping = {}
    
    # Generate random numbers for all files
    numbers = list(range(1, len(files) + 1))
    random.shuffle(numbers)
    
    for i, filename in enumerate(files):
        # Skip the Python scripts and mapping file
        if filename.endswith('.py') or filename.endswith('.json'):
            continue
            
        # Generate new filename with random number prefix
        new_name = f"{numbers[i]:04d}_{filename}"
        
        # Store the mapping
        name_mapping[new_name] = filename
        
        # Rename the file
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
    
    # Save the mapping to a JSON file
    mapping_file = os.path.join(directory, '.filename_mapping.json')
    with open(mapping_file, 'w') as f:
        json.dump(name_mapping, f, indent=4)
    
    print(f"Successfully renamed {len(name_mapping)} files!")

if __name__ == "__main__":
    # Use the current directory
    current_dir = os.getcwd()
    random_rename_files(current_dir)
