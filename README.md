# 📁 File Organizer

![GitHub last commit](https://img.shields.io/github/last-commit/Renzie2161/FileSwift)
![GitHub issues](https://img.shields.io/github/issues/Renzie2161/FileSwift)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Renzie2161/FileSwift)

A simple and effective Python script to organize your files into designated folders based on their file extensions. 

## 📖 Table of Contents
- [Introduction](#-introduction)
- [Installation](#-installation)
- [Usage](#-usage)
  - [Organizing Files](#organizing-files)
  - [Ungrouping Folders](#ungrouping-folders)
- [Custom Configuration](#custom-configuration)
- [License](#license)

---

## 🎉 Introduction
The **File Organizer** helps users efficiently manage their files by categorizing them into folders like **Videos**, **Audios**, **Documents**, **Images**, **Archives**, and more. You can also ungroup folders and move files back to a specified directory.

---

## 💻 Installation

### Prerequisites
- **Python 3.x**: Ensure you have Python installed. Download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository
```bash
git clone https://github.com/Renzie2161/FileSwift
cd FileSwift
```

### Dependencies
No external libraries required; the script uses standard Python libraries.

---

## 🚀 Usage

### Running the Script
To run the script, use the following command:
```bash
python fileswift.py
```

### Organizing Files
1. **Enter the destination path** where your files are located (or type `q` to quit).
2. **Custom JSON Configuration**: Enter the path to your custom config file or press Enter to use the default.
3. **Confirmation**: Confirm if you want to organize the files in the specified directory.

### Ungrouping Folders
1. **Enter the folder path** containing subfolders you wish to ungroup.
2. **Specify folder names** to ungroup, separated by commas (or leave blank to ungroup all).

---

## ⚙️ Custom Configuration

### Creating a Custom Configuration File
Create a JSON file with this structure:
```json
{
    "CategoryName": [".ext1", ".ext2"],
    "AnotherCategory": [".ext3", ".ext4"]
}
```

#### Example:
```json
{
    "Music": [".mp3", ".wav"],
    "Documents": [".pdf", ".docx"],
    "Images": [".jpg", ".png"]
}
```

### Loading the Custom Configuration
Provide the path to your custom JSON file when prompted. The program will validate the structure.

---

> [!IMPORTANT]
> This program is no longer actively maintained or supported. Feel free to use it as-is, but there may be bugs or issues that have not been addressed. Consider using alternative solutions for similar functionality.

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
