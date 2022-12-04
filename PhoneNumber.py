from ExtractFile import extracting_text
import re


def get_phone_number(filename):
    resume = extracting_text(filename)
    match = re.findall(r'\+[0-9]{1,}\s+\([0-9]{1,}\)\s+[0-9]{1,}', resume)
    print("Номер телефона: " + match[0])

