from time import time
import os
import shutil
import json

default_config = {
    'Videos': (
        '.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', 
        '.webm', '.mpeg', '.m4v', '.3gp', '.f4v', '.vob',
        '.rm', '.rmvb', '.divx', '.ogv'
    ),
    'Audios': (
        '.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', 
        '.wma', '.opus', '.aiff', '.cda', '.amr', '.mka',
        '.raw', '.dts', '.wv'
    ),
    'Documents': (
        '.pdf', '.docx', '.txt', '.pptx', '.xls', '.csv', 
        '.odt', '.rtf', '.xml', '.json', '.md', '.doc', 
        '.ppt', '.xlsm', '.dotx', '.odm', '.wps'
    ),
    'Images': (
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', 
        '.svg', '.raw', '.heif', '.ico', '.webp', '.jfif',
        '.cr2', '.nef', '.dng'
    ),
    'Archives': (
        '.zip', '.tar', '.gz', '.rar', '.7z', '.iso', 
        '.dmg', '.xz', '.bz2', '.z', '.cbr', '.cbz', 
        '.tar.gz', '.tar.bz2'
    ),
    'Scripts': (
        '.py', '.js', '.html', '.css', '.sh', '.bat', 
        '.php', '.rb', '.pl', '.go', '.ts', '.java', 
        '.r', '.swift', '.vb', '.lua', '.dart', 
        '.sql', '.groovy', '.coffee', '.json', '.xml', 
        '.cmd', '.ksh', '.zsh', '.ps1', '.vbs', 
        '.ahk', '.f90',
    ),
    'Ebooks': (
        '.epub', '.mobi', '.azw', '.fb2', '.ibooks', 
        '.lit', '.txt', '.pdf'
    ),
    'Fonts': (
        '.ttf', '.otf', '.woff', '.woff2', '.eot', 
        '.fon', '.pfa', '.pfb'
    ),
    'Databases': (
        '.sql', '.db', '.sqlite', '.mdb', '.accdb', 
        '.dbf', '.prn', '.csv'
    ),
    'CADs': (
        '.dwg', '.dxf', '.dgn', '.plt', '.stl', 
        '.step', '.iges', '.3dm', '.skp'
    ),
    'Executeables': (
        '.exe', '.dll', '.sys', '.bat', '.cmd', 
        '.app', '.sh'
    ),
    # Add more file extensions group here
}

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def load_custom_categories(file_path):
    if not os.path.isfile(file_path):
        print(f"{RED}[ERROR]{RESET} The file '{file_path}' does not exist.")
        print(f"{GREEN}[INFO]{RESET} Switching to default config file.")
        return {}
    
    try:
        with open(file_path, 'r') as f:
            categories = json.load(f)

            if not isinstance(categories, dict):
                print(f"{RED}[ERROR]{RESET} The JSON file must be an object (dictionary).")
                return {}

            for category, extensions in categories.items():
                if not isinstance(extensions, list):
                    print(f"{RED}[ERROR]{RESET} The extensions for '{category}' must be a list.")
                    return {}
                for ext in extensions:
                    if not isinstance(ext, str):
                        print(f"{RED}[ERROR]{RESET} Each extension must be a string in category '{category}'.")
                        return {}

            return categories
            
    except json.JSONDecodeError:
        print(f"{RED}[ERROR]{RESET} The file '{file_path}' is not valid JSON.")
    except Exception as e:
        print(f"{RED}[ERROR]{RESET} Could not load categories from '{file_path}': {e}")
        
    return {}

def get_category(filename, file_categories):
    for category, extensions in file_categories.items():
        if filename.lower().endswith(tuple(ext.lower() for ext in extensions)):
            return category
    return 'Others'


def is_already_organized(base_directory):
    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)
        if os.path.isfile(item_path):
            return False
    return True


def get_confirmation(prompt):
    response = input(prompt).strip().lower()
    return response in ['y', '']


def organize_files():
    file_categories = default_config

    while True:
        try:
            base_directory = input("Enter the destination path for organizing ('q' to quit): ")
            if base_directory.lower() == "q":
                print(f"{GREEN}[INFO]{RESET} Exiting the program.")
                break

            if not os.path.exists(base_directory):
                print(f"{RED}[ERROR]{RESET} The directory '{base_directory}' does not exist. Please try again.")
                continue

            custom_config_path = input("Do you have a custom file categories JSON file? (leave blank for default): ").strip()
            if custom_config_path:
                custom_categories = load_custom_categories(custom_config_path)
                if custom_categories:
                    file_categories = custom_categories

            if is_already_organized(base_directory):
                print(f"{RED}[ERROR]{RESET} The directory '{base_directory}' is already organized. Please select a different folder.")
                continue

            if not get_confirmation(f"Are you sure you want to organize the files in '{base_directory}'? (Y/n): "):
                print(f"{RED}[INFO]{RESET} Operation canceled. Please enter a new path.")
                continue

            start_time = time()
            categories_with_files = {category: [] for category in file_categories.keys()}
            categories_with_files['Others'] = []

            for filename in os.listdir(base_directory):
                file_path = os.path.join(base_directory, filename)
                if os.path.isfile(file_path):
                    category = get_category(filename, file_categories)
                    categories_with_files[category].append(filename)

            summary = {category: 0 for category in categories_with_files.keys()}

            for category, files in categories_with_files.items():
                if files:
                    category_path = os.path.join(base_directory, category)
                    os.makedirs(category_path, exist_ok=True)

                    for filename in files:
                        file_path = os.path.join(base_directory, filename)
                        destination_path = os.path.join(category_path, filename)
                        try:
                            shutil.move(file_path, destination_path)
                            summary[category] += 1
                            print(f"{GREEN}[INFO]{RESET} Moved: {filename} -> {category}")
                        except Exception as e:
                            print(f"{RED}[ERROR]{RESET} An error occurred while moving {filename}: {e}")

            print_summary(summary, time() - start_time)
            input("\nPress any key to return to the menu.")
            break

        except Exception as err:
            print(f"{RED}[ERROR]{RESET} An error has occurred: {err}")


def print_summary(summary, elapsed_time):
    print(f"\n{' Summary '.upper().center(50, '#')}")
    for category, count in summary.items():
        if count > 0:
            print(f"{category}: {count} file(s)")
    print(f"Time Elapsed: {elapsed_time:.2f}s")


def ungroup_folder(folder_path, folders_to_ungroup):
    start_time = time()
    available_folders = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
    
    if not available_folders:
        print(f"{RED}[INFO]{RESET} No folders found in '{folder_path}'. No actions required.")
        return

    if folders_to_ungroup in ['all', '*', '']:
        folders_to_ungroup = available_folders
        print(f"{GREEN}[INFO]{RESET} Ungrouping all folders: {folders_to_ungroup}")
    else:
        folders_to_ungroup = [folder.strip() for folder in folders_to_ungroup.split(',') if folder.strip()]
        invalid_folders = [folder for folder in folders_to_ungroup if folder not in available_folders]

        if invalid_folders:
            print(f"{RED}[ERROR]{RESET} The following folders are not valid: {', '.join(invalid_folders)}. Skipping those.")

        folders_to_ungroup = [folder for folder in folders_to_ungroup if folder in available_folders]
        
        if not folders_to_ungroup:
            print(f"{RED}[ERROR]{RESET} No valid folders to ungroup. Stopping the operation.")
            return

        print(f"{GREEN}[INFO]{RESET} Ungrouping specified folders: {folders_to_ungroup}")

    moved = 0
    removed = 0

    for folder in folders_to_ungroup:
        folder_path_to_ungroup = os.path.join(folder_path, folder)
        if not os.path.isdir(folder_path_to_ungroup):
            print(f"{RED}[ERROR]{RESET} '{folder}' is not a valid folder in '{folder_path}'. Skipping.")
            continue

        for root, dirs, files in os.walk(folder_path_to_ungroup, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                shutil.move(file_path, folder_path)
                print(f'{GREEN}[INFO]{RESET} Moved: {file_path} -> {folder_path}')
                moved += 1

            for name in dirs:
                dir_path = os.path.join(root, name)
                try:
                    os.rmdir(dir_path)
                    print(f'{GREEN}[INFO]{RESET} Removed empty directory: {dir_path}')
                    removed += 1
                except OSError as e:
                    print(f'{RED}[ERROR]{RESET} Could not remove directory {dir_path}: {e}')

        try:
            os.rmdir(folder_path_to_ungroup)
            print(f'{GREEN}[INFO]{RESET} Removed directory: {folder_path_to_ungroup}')
            removed += 1
        except OSError as e:
            print(f'{RED}[ERROR]{RESET} Could not remove directory {folder_path_to_ungroup}: {e}')

    print_summary({'Moved': moved, 'Removed': removed}, time() - start_time)
    input("\nPress any key to return to the menu.")


def ungroup():
    while True:
        user_input = input("Enter the folder path to ungroup ('q' to quit): ")
        if user_input.lower() == "q":
            print(f"{GREEN}[INFO]{RESET} Exiting the program.")
            break

        if not user_input:
            print(f"{RED}[ERROR]{RESET} No folder path provided. Please try again.")
            continue

        if not os.path.isdir(user_input):
            print(f"{RED}[ERROR]{RESET} The path '{user_input}' is not a valid directory.")
            continue

        folders_input = input("Enter the folder names to ungroup (comma or semicolon separated), or leave blank for all: ")
        ungroup_folder(user_input, folders_input)
        break


def main_menu():
    while True:
        print("\n" + "#" * 30)
        print("FILE ORGANIZER".center(30))
        print("#" * 30 + "\n")
        print("Choose an option:")
        print("1. Organize Files")
        print("2. Ungroup Folders")
        print("q. Quit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == '1':
            organize_files()
        elif choice == '2':
            ungroup()
        elif choice == 'q':
            print(f"{GREEN}[INFO]{RESET} Exiting the program.")
            break
        else:
            print(f"{RED}[ERROR]{RESET} Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
