from fileinput import filename

import PyPDF2
from PyPDF2 import PageObject
import re


class HeadHunterParser:

    def __init__(self, file):
        self.file = file

    def get_extracting_text(self):
        #file = open(self.filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(self.file)
        page_obj: PageObject = pdf_reader.getPage(0)
        text = page_obj.extractText()
        self.file.close()
        return text

    def get_fields(self):
        hh = HeadHunterParser(self.file)
        resume = hh.get_extracting_text()
        match_name = "Имя: " + re.findall(r'.*', resume)[0]
        match_phone = "Номер телефона: " + re.findall(r'\+[0-9]{1,}\s+\([0-9]{1,}\)\s+[0-9]{1,}', resume)[0]
        match_mail = "Почта: " + re.findall(r'[A-Za-z0-9]{1,}@[A-Za-z0-9]{1,}\.[A-Za-z0-9]{1,}', resume)[0]
        match_gender = "Пол: " + re.findall(r'Мужчина|Женщина', resume)[0]
        final_match = match_name + '\n' + match_phone + '\n' + match_mail + '\n' + match_gender
        return final_match
