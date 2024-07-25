"""
Module for tokenizing text.
"""

import string
import logging
import requests

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download(text_numbers):

    """

    Download raw text data from gutenberg with the book id's

    Args:
        text_numbers (list): List of book id's to download from Project Gutenberg.

    Returns: 
        list: List of raw text data.

    """

    logger.info("downloading raw data ...")
    base_url = "https://www.gutenberg.org/cache/epub/{}/pg{}.txt"
    raw_texts =[]

    for number in text_numbers:
        url = base_url.format(number, number)
        logger.info("downloading from URL: %s", url)
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Ensure we notice bad responses
        raw_texts.append(response.text)

    return raw_texts

def clean_text(text):
    """
    Convert text to lowercase and remove punctuation.

    Args:
        text (str): The input string.

    Returns:
        str: The cleaned text.
    """
    logger.info("cleaning text input...")
    assert isinstance(text, str), "Input should be a string"

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def tokenize(text):
    """
    Tokenize the input text into a list of words.

    Args:
        text (str): The input string.

    Returns:
        list: A list of words.
    """

    logger.info("tokenizing text input...")
    assert isinstance(text, str), "Input should be a string"

    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    return words

def count_words(text):
    """
    Count the frequency of each word in the text.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """

    logger.info("Counting words...")
    assert isinstance(text, str), "Input should be a string"

    words = tokenize(text)
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
