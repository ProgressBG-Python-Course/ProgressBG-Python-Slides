import re

pattern = re.compile(r"ab{2,3}c")

print(pattern.search("abc"))  # Matches
print(pattern.search("abbc"))  # Matches
print(pattern.search("abbbc"))  # Matches
print(pattern.search("abbbbc"))  # Matches
