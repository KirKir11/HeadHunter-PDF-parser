import PyPDF2
from PyPDF2 import PageObject


def extracting_text(filename):
    file = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(file)
    page_obj: PageObject = pdf_reader.getPage(0)
    return page_obj.extractText()
    file.close()


#print(extracting_text('resume_for_test_2.pdf'))