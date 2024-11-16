# 📁 FileSwift

![GitHub last commit](https://img.shields.io/github/last-commit/Renzie2161/FileSwift)
![GitHub issues](https://img.shields.io/github/issues/Renzie2161/FileSwift)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Renzie2161/FileSwift)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/Renzie2161/FileSwift?style=social)
![GitHub forks](https://img.shields.io/github/forks/Renzie2161/FileSwift)

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
**FileSwift** helps users efficiently manage their files by categorizing them into folders like **Videos**, **Audios**, **Documents**, **Images**, **Archives**, and more. You can also ungroup folders and move files back to a specified directory.

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
```json
{
  "Text and Document Files": [".txt", ".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".html", ".htm", ".md", ".epub", ".xml", ".json", ".csv"],
  "Spreadsheet and Database Files": [".xls", ".xlsx", ".ods", ".csv", ".mdb", ".sqlite", ".db"],
  "Image Files": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".svg", ".raw", ".ico", ".heif", ".heic"],
  "Audio and Video Files": [".mp3", ".wav", ".flac", ".ogg", ".aac", ".m4a", ".mp4", ".avi", ".mov", ".mkv", ".webm", ".flv", ".3gp", ".wmv"],
  "Compressed and Archive Files": [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2", ".xz", ".iso", ".img"],
  "Executable and Script Files": [".exe", ".bat", ".sh", ".ps1", ".apk", ".app", ".jar", ".py", ".php", ".cgi", ".rb"],
  "System and Configuration Files": [".ini", ".sys", ".dll", ".cfg", ".log", ".bak", ".tmp", ".config"],
  "Font Files": [".ttf", ".otf", ".woff", ".eot"],
  "Web and Internet Files": [".css", ".js", ".json", ".php", ".asp", ".aspx", ".xml", ".svg", ".rss", ".yml", ".yaml"],
  "Virtualization and Disk Images": [".vmdk", ".vdi", ".vhd", ".vhdx", ".qcow2"],
  "Programming and Development Files": [".cpp", ".h", ".java", ".cs", ".go", ".swift", ".rs", ".html", ".css", ".xml", ".json", ".sql"],
  "Miscellaneous": [".torrent", ".srt", ".vtt", ".ics", ".pst", ".eml", ".epub", ".mobi", ".azw3"]
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
