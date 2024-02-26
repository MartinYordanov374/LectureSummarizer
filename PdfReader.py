from PyPDF2 import PdfReader 
  
def readPdf(targetPDF):
    reader = PdfReader(targetPDF) 
    allPagesText = [page.extract_text() for page in reader.pages]
    return allPagesText

