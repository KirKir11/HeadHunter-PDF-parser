from ExtractFile import extracting_text
import re

def get_name(filename):
    resume = extracting_text(filename)
    resume = extracting_text(filename)
    match = re.findall(r'.*', resume)
    print("Имя: " + match[0])

