import re

def validating_str(s):
    return bool((len(s)<14) * (len(s)>7) * len(re.findall("[a-z]", s)) * len(re.findall("[A-Z]", s)) * len(re.findall(r"\d", s)) * (len(re.findall("[_:@]", s))>1) * (not (len(re.findall("[~+\-!#]", s)))) * (not len(re.findall("[A-Z][A-Z]", s))) * (not len(re.findall("[a-zA-Z0-9]\s[a-zA-Z0-9]", s))))

# if __name__ == "__main__":
    # print( validating_str( input() ) )


