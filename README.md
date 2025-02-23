# PDF to Word Converter  

## Overview  
This project is a **PDF to Word converter** developed in Python. It allows users to convert PDF files into editable Word documents, aiming to preserve text formatting as accurately as possible.  

## Features  
✔ Convert PDF to Word (`.docx`)  
✔ Preserve text formatting as much as possible

## Requirements  
- Python 3.11 or 3.12 (Python 3.13 is not compatible due to the removal of msilib). [Learn more](https://docs.python.org/3/library/msilib.html)  
- Required libraries listed in `requirements.txt`.

## Installation  

### Clone the Repository  
Clone the repository and navigate to the project directory:  
```bash  
git clone https://github.com/jeniferalberti/PDF-to-Word-Converter.git  
cd PDF-to-Word-Converter  
```  

### Set Up a Virtual Environment  

Create a virtual environment:  
```bash  
python -m venv .venv  
```  

### Activate the Virtual Environment  

On **Windows**:  
```bash  
.venv\Scripts\activate  
```  

On **macOS/Linux**:  
```bash  
source .venv/bin/activate  
```  

### Install Dependencies  

Ensure that `pip` is installed, then install the dependencies:  
```bash  
pip install -r requirements.txt  
```  

### Build  

Run the script to build the project:  
```bash  
python setup.py build  
```  

## Usage  

To use the converter, run the script and follow the on-screen instructions:  
```bash  
python main.py  
```  

Alternatively, if you want to run the executable directly, navigate to the build directory:  
```bash  
cd \build\exe.win-amd64-3.11\PDF-to-Word-Converter.exe  
```  

## License  

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  

---

Changes made:
- Clarified the project description and features.
- Improved formatting consistency (e.g., file names like `requirements.txt` and `setup.py` are now in code format).
- Adjusted instructions for running the executable for clarity.
- Tidied up the section titles for better readability.