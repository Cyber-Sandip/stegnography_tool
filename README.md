
🔐 Steganography Tool

A Python-based desktop application that allows users to hide and extract multiple files inside a JPG image using steganography techniques. Built with a modern GUI, this tool is simple, fast, and practical for learning data hiding concepts.

📌 Features
🔒 Hide multiple files inside a JPG image
🔓 Extract hidden files easily
🖥️ User-friendly GUI using CustomTkinter
📁 Supports all file types (txt, pdf, zip, etc.)
⚡ Lightweight and fast
🛠️ Tech Stack
Language: Python 3
GUI: Tkinter, CustomTkinter
Modules: os, struct

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/your-username/steganography-tool.git
cd steganography-tool
2. Install Dependencies
pip install customtkinter
3. Run the Application
python main.py

🧠 How It Works
The tool appends hidden data after the JPEG End-of-File marker (FFD9)
Uses a custom identifier: STEGOv2
Stores:
Number of files
File names
File sizes
File data

This ensures the image remains viewable while carrying hidden content.

📂 Project Structure
steganography-tool/
│
├── main.py        # Main application file
├── README.md      # Documentation


⚠️ Limitations
Only supports JPG/JPEG images
No encryption (data is hidden but not secured)
File size increases with hidden content
🔮 Future Improvements
Add password protection & encryption
Support PNG and other formats
Add drag-and-drop functionality
Improve UI/UX


👨‍💻 Author ~  
Sandip Hazra

📜 License

This project is open-source and free to use for learning purposes.

⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork it
🤝 Contribute