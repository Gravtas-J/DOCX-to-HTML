import streamlit as st
import mammoth
import base64
from io import BytesIO

# Function to convert DOCX to HTML
def docx_to_html(docx_file):
    with docx_file:
        result = mammoth.convert_to_html(docx_file)
        html = result.value  # The generated HTML
        return html

# Function to download HTML file
def get_html_download_link(html_content, filename):
    buffer = BytesIO()
    buffer.write(html_content.encode())
    buffer.seek(0)
    b64 = base64.b64encode(buffer.read()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="{filename}">Download HTML file</a>'
    return href

st.title('DOCX to HTML Converter')

# Initialize or toggle the state
if 'show_html' not in st.session_state:
    st.session_state.show_html = False  # Default: don't show

# Button to toggle visibility
with st.sidebar:
    if st.button('Show/Hide Converted HTML'):
        st.session_state.show_html = not st.session_state.show_html

# File uploader
uploaded_file = st.file_uploader("Choose a .docx file", type="docx")

if uploaded_file is not None:
    # Convert DOCX to HTML
    html_content = docx_to_html(uploaded_file)
    
    # Optionally display HTML in the app
    if st.session_state.show_html:
        st.markdown("### Converted HTML:")
        st.markdown(html_content, unsafe_allow_html=True)

    # Download link for HTML
    st.markdown(get_html_download_link(html_content, 'converted.html'), unsafe_allow_html=True)
