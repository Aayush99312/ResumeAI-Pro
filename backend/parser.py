import pdfplumber


def extract_text(pdf_path):
    """
    Extracts text from a PDF resume.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text.
    """

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# Test the parser
if __name__ == "__main__":

    pdf_file = "resumes/sample_resume.pdf"

    resume_text = extract_text(pdf_file)

    print("========== EXTRACTED TEXT ==========\n")
    print(resume_text)                      