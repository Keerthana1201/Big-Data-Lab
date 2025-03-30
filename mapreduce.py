from functools import reduce
from collections import defaultdict
def mapper(text):
    words = text.split()
    return [(word.lower(), 1) for word in words]  # return a tuple (word, 1)
def reducer(counts, word_count):
    word, count = word_count
    counts[word] += count
    return counts
def word_count(text):
    mapped_data = mapper(text)
    result = reduce(reducer, mapped_data, defaultdict(int))
    return result
def get_input():
    sentence = input("Enter a sentence: ")
    return sentence
def main():
    sentence = get_input()
    if sentence:
        word_counts = word_count(sentence)
        print("\nWord Counts:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")
    else:
        print("No input provided.")
if __name__ == "__main__":
    main()
