import PyPDF2
from PyPDF2 import PageObject
import re


class HeadHunterParser:

    def get_extracting_text(filename):
        file = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(file)
        page_obj: PageObject = pdf_reader.getPage(0)
        return page_obj.extractText()
        file.close()

    def get_gender(filename):
        resume = HeadHunterParser.get_extracting_text(filename)
        match = re.findall(r'Мужчина|Женщина', resume)
        return "Пол: " + match[0]

    def get_name(filename):
        resume = HeadHunterParser.get_extracting_text(filename)
        match = re.findall(r'.*', resume)
        return "Имя: " + match[0]

    def get_phone_number(filename):
        resume = HeadHunterParser.get_extracting_text(filename)
        match = re.findall(r'\+[0-9]{1,}\s+\([0-9]{1,}\)\s+[0-9]{1,}', resume)
        return "Номер телефона: " + match[0]

    def get_mail(filename):
        resume = HeadHunterParser.get_extracting_text(filename)
        match = re.findall(r'[A-Za-z0-9]{1,}@[A-Za-z0-9]{1,}\.[A-Za-z0-9]{1,}', resume)
        return "Почта: " + match[0]