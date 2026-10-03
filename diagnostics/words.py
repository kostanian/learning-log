import string


def read_words(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text = text.lower()
    for mark in string.punctuation+ "—«»…":
        text = text.replace(mark, " ")
    return text.split()


def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


words = read_words("text.txt")
counts = count_words(words)
top = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:5]
for word, n in top:
    print(f"{word}: {n}")
print("тире:", counts.get("—", 0))