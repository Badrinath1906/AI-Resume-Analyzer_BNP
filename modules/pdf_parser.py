import PyPDF2

#Purpose: Extract text from uploaded PDF

def extract_text_from_pdf(uploaded_file):

    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        text = ""

        for page in pdf_reader.pages:
            text += page.extract_text()

        return text

    except Exception:
        return ""