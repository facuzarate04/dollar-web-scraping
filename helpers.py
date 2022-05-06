
import re

def parse_to_float(number):
    if type(number) is float or type(number) is int:
        return number
    else:
        parsed_number = re.findall(r"[-+]?(?:\d*\,\d+|\d+)", number)[0].replace(',','.')
        return float(parsed_number)