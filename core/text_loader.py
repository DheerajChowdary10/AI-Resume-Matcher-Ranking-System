import pdfplumber

def load_resume(file):
    content = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                content += text + " "
    return content.strip()