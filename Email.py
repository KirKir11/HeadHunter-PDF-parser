from ExtractFile import extracting_text
import re


def get_mail(filename):
    resume = extracting_text(filename)
    match = re.findall(r'[A-Za-z0-9]{1,}@[A-Za-z0-9]{1,}\.[A-Za-z0-9]{1,}', resume)
    print("Почта: " + match[0])