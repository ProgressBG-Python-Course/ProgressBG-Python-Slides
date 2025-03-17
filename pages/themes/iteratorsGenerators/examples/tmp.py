# class WordsFromSentence:
#     def __init__(self, sentence):
#         self.words = sentence.split() if sentence else []
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.words):
#             raise StopIteration

#         self.index += 1
#         return self.words[self.index - 1]


# def words_generator(sentence):
#     words = sentence.split() if sentence else []
#     for word in words:
#         yield word


# for w in WordsFromSentence("this is a test"):
#     print(w)

# for w in words_generator("this is a test"):
#     print(w)


# def simple_generator():
#     print("Start")
#     yield 1
#     print("Resume")
#     yield 2
#     print("Resume")
#     yield 3
#     print("Done")


# gen = simple_generator()

# print(next(gen))  # Start -> Yields 1
# print(next(gen))  # Resumes -> Yields 2
# print(next(gen))  # Resumes -> Yields 3
# print(next(gen))  # Raises StopIteration


def foo_generator():
    print("generator start")

    # yield is almost like return, but it freezes the execution
    yield 1
    yield 2

    print("generator end")


foo_gen = foo_generator()
print(foo_gen)
