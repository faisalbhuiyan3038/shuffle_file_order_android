# File Randomizer for Android

This tool helps you randomly shuffle file order by renaming files with random number prefixes. It's particularly useful for applications that only sort by filename.

## Scripts

1. `random_rename.py` - Adds random number prefixes to all files in the current directory
2. `restore_names.py` - Restores the original filenames

## How to Use

### On Android:

1. Install a Python app from the Play Store (like Pydroid 3)
2. Copy these scripts to the folder containing the files you want to rename
3. Run the scripts using your Python app

### To Randomize Files:
1. Open `random_rename.py` in your Python app
2. Run the script
- All files in the current directory will be renamed with random number prefixes
- A hidden file `.filename_mapping.json` will be created to store original names

### To Restore Original Names:
1. Open `restore_names.py` in your Python app
2. Run the script
- All files will be restored to their original names
- The mapping file will be automatically deleted

## Notes:
- The scripts will not rename themselves or any other .py or .json files
- Make sure to keep both scripts and the mapping file together until you restore the original names
- Always run the restore script before running the random rename script again
