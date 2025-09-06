import re

pattern = r"[A-Z]yclone"
text = '''
If there is a Cyclone and there is a another Cyclone it is called Dyclone
'''
matches = re.finditer(pattern,text)
for match in matches:
    print(match)