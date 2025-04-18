        
def count_words(text : str):
    words = text.split()
    return len(words)
    
def count_chars(text : str):
    words = text.lower()
    counted = {}
    for char in words:
        if char != " ":
            counted[char] = counted.get(char, 0) + 1
    return counted

def sorted_chars(counted : dict):
    sort = []
    keys = sorted(counted, key=lambda k: counted[k], reverse=True)
    for key in keys:
        sort.append({"char" : key, "count" : counted[key]})
        
    return sort