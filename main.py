import re
def read_file_content(filename):
    text= open(filename)
    return text
Dict = {}
def count_words():
    text = read_file_content("./story.txt")
    wordlist =[]
    for line in text:
        words = re.split(" ", line.strip())
        wordlist.extend(words)
    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i].lower()
    for key in wordlist:
        Dict[key] = wordlist.count(key)
    return Dict
print(count_words())