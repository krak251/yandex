import sys

unique = set()
for line in sys.stdin:
    words = line.strip().split()
    if not words:
        continue
    max_word = max(words)
    unique.add(max_word)
for word in unique:
    print(word)

