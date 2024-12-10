import os
import json
from pathlib import Path

def restore_original_names(directory):
    # Load the mapping file
    mapping_file = os.path.join(directory, '.filename_mapping.json')
    
    try:
        with open(mapping_file, 'r') as f:
            name_mapping = json.load(f)
    except FileNotFoundError:
        print("No mapping file found! Please run random_rename.py first.")
        return
    
    # Restore original names
    for new_name, original_name in name_mapping.items():
        try:
            old_path = os.path.join(directory, new_name)
            new_path = os.path.join(directory, original_name)
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
        except Exception as e:
            print(f"Error restoring {new_name}: {str(e)}")
    
    # Remove the mapping file
    os.remove(mapping_file)
    print("Successfully restored original filenames!")

if __name__ == "__main__":
    # Use the current directory
    current_dir = os.getcwd()
    restore_original_names(current_dir)
