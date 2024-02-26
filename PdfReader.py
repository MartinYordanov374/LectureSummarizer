from PyPDF2 import PdfReader 
  
def readPdf(targetPDF):
    reader = PdfReader(targetPDF) 
    allPagesText = [page.extract_text() for page in reader.pages]
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

