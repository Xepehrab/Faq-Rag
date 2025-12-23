import re
def clean_text(text):
    if not isinstance(text,str):
        return ""
    
    text = str(text)
    text=text.replace("\u200c"," ")
    text=re.sub(r"\s+"," ",text)
    return text.strip()
