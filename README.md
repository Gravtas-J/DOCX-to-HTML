# README for DOCX to HTML Converter Streamlit App

This Streamlit application allows users to convert DOCX files to HTML format directly within a web interface. The conversion process is straightforward: users upload a DOCX file, and the application processes and shows the HTML output, which can also be downloaded as an HTML file. This README provides an overview of the application's functionality, requirements, and how to run it.

## Features

- **DOCX to HTML Conversion**: Converts uploaded DOCX files to HTML.
- **HTML Preview**: Option to display the converted HTML within the app.
- **Download HTML**: Allows users to download the converted HTML as a file.

## Requirements

To run this application, you will need:

- Python 3.6 or newer.
- Streamlit
- Mammoth `.docx` to HTML converter.

You can install the necessary libraries using pip:

```bash
pip install streamlit mammoth
```

## How to Run

1. Save the provided code in a Python file, for example, `docx_to_html_app.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved `docx_to_html_app.py`.
4. Run the application using Streamlit:

```bash
streamlit run docx_to_html_app.py
```

5. The Streamlit application will start, and your default web browser will open a new tab pointing to the local server (typically `http://localhost:8501`) where the app is running.

## Using the Application

- **Upload a DOCX File**: Use the file uploader to choose a `.docx` file from your computer.
- **Show/Hide Converted HTML**: Click the "Show/Hide Converted HTML" button to toggle the visibility of the converted HTML in the application.
- **Download Converted HTML**: After conversion, a download button appears in the sidebar. Click it to download the HTML file to your computer.

## Code Overview

- `docx_to_html(docx_file)`: A function that converts the uploaded DOCX file to HTML using the Mammoth library.
- `get_html_base64(html_content)`: Converts the HTML content to a base64-encoded string for easy download.
- The Streamlit UI components (`st.title`, `st.button`, `st.file_uploader`, etc.) create the application's interface.

## Limitations & Notes

- The application currently only supports `.docx` files.
- The HTML preview and download are based on the conversion results, which may vary depending on the complexity and formatting of the original DOCX file.

For any issues, suggestions, or contributions, please feel free to open an issue or pull request in the project's repository.
