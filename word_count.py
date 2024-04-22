import sys
import re
from collections import Counter

def count_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)
            word_count = Counter(words)
            for word, count in word_count.most_common():
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"Error: The file at {filepath} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input.file")
    else:
        filepath = sys.argv[1]
        count_words(filepath)
