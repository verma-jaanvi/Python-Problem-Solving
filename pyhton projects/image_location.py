import os

def find_file_by_name(file_name, start_directory='/'):

    for root, _, files in os.walk(start_directory):
        for file in files:
            if file.lower() == file_name.lower():
                return os.path.abspath(os.path.join(root, file))
    return None


file_name = input("Enter the image file name (with extension):")
start_directory = input("Enter the directory to start searching (leave empty for root directory): ").strip()
if not start_directory:
    start_directory = '/' if os.name != 'nt' else 'C:\\'

if os.path.isdir(start_directory):
    file_path = find_file_by_name(file_name, start_directory)
    if file_path:
        print(f"\nFile found: {file_path}")
    else:
        print("No file with the specified name was found.")
else:
    print("The specified starting directory does not exist.")