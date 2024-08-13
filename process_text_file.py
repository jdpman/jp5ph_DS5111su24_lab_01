"""
process text

"""

import sys
from tokenizer import count_words

def process_file(filename):
    """
    Process a text file to count the frequency of each word.

    Args:
        filename (str): The name of the file to process.
    """
    with open(filename, 'r') as file:
        text = file.read()
    word_counts = count_words(text)
    output_filename = filename + '.count'
    with open(output_filename, 'w') as output_file:
        for word, count in word_counts.items():
            output_file.write(f'{word}: {count}\n')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python process_text_file.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    process_file(filename)
