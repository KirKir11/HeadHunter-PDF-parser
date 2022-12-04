from ExtractFile import extracting_text
import re

def get_gender(filename):
    resume = extracting_text(filename)
    match = re.findall(r'Мужчина|Женщина', resume)
    print("Пол: " + match[0])