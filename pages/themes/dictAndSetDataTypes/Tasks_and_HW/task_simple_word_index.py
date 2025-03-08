text = """apple and banana one apple one banana
          a red apple and a green apple"""

words = text.split()

word_counts = {word:words.count(word) for word in set(words)}

for word,count in word_counts.items():
    print(f'{word} - {count}')