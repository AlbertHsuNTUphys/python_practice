import re

def count(s):
    d = {}
    processed = re.split("[^a-zA-Z0-9]", s.lower())
    for word in processed:
        d[word] = d.get(word, 0) + 1
    del(d[''])
    # print(d)
    return d


# if __name__ == "__main__":
    # inp = "It\'s recommended you don\'t take down any load-bearing walls when renovating."  
    # print(count(inp))
