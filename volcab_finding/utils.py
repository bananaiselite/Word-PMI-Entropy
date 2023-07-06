import re

def fullwidth_to_halfwidth(text):
    halfwidth_text = ""
    for char in text:
        code = ord(char)
        # 全形字符範圍：65281~65374
        if 65281 <= code <= 65374:
            # 將全形字符轉換為對應的半形字符
            halfwidth_char = chr(code - 65248)
            halfwidth_text += halfwidth_char
        else:
            halfwidth_text += char
            
    return halfwidth_text

def remove_english(text):
    
    pattern = r'[a-zA-Z]'
    removed_text = re.sub(pattern, '', text)
    return removed_text


def words_check(string):
    """
    檢查字串是否只包含數字或符號
    """

    pattern = r'^[0-9!@#$% ^&*\(\)-_=+\[\]\{\}\\|;:\'\",./<>?`~]+$'
    match = re.match(pattern, string)

    if match:
        return True
    else:
        return False