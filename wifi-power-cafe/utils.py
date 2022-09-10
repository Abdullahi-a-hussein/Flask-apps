
import re

def valid_password(password:str) -> bool:
    return True if re.findall('[A-z]', password) and re.findall('[a-z]', password) and (
        re.findall('[0-9]', password)) else False
    
print(valid_password('WeArelazy0'))