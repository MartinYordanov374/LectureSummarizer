import TextSummarizer
import PdfReader


pdf_text = PdfReader.readPdf('./lecture_06.pdf')

summarized_text = TextSummarizer.summarizeText(pdf_text)

print(summarized_text)