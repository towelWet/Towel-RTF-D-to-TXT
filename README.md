ONLY RTFD TO TXT WORKS FOR NOW!

# 📜 Towel RTF(D) to TXT Converter

The Towel RTF(D) to TXT Converter is an efficient tool for macOS users to convert RTFD and RTF files to plain text (TXT) format. It combines user-friendly design with powerful functionality, making it an ideal solution for handling rich text files.

## 🚀 Getting Started

These instructions will help you set up and run the Towel RTF(D) to TXT Converter on your local machine for development and testing purposes.

### Prerequisites

- macOS 12.6 or later.
- Python 3.11 installed.
- PyInstaller for packaging the application.

### 🛠 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/towelWet/Towel-RTF-D-to-TXT/tree/main
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd path/to/Towel-RTF-D-to-TXT
   ```

3. **(Optional) Install Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Dependencies**
   - If your project requires any dependencies, install them here.

### 📦 Packaging the Application with PyInstaller

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Package the Application**
   ```bash
   pyinstaller --onefile --windowed --name "Towel RTF RTFD to TXT" --icon=/path/to/AppIcon.icns RTFD.py
   ```
   - Replace `/path/to/AppIcon.icns` with the actual path to your icon file.

3. **Locate the Packaged Application**
   - The executable will be located in the `dist` directory.

### 🏃 Running the Application

- Open the `dist` directory.
- Double-click on `Towel RTF RTFD to TXT.app` to run the application.

### 🖥️ Using the Application

- **Select Files**: Click "Select RTFD/RTF Files" to choose files for conversion.
- **Output Folder**: Choose a destination folder for the converted TXT files.
- **Convert**: Click "Convert Files" to start the conversion.
- **Notification**: A success message appears once the conversion is complete.
