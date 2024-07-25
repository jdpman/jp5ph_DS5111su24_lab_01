# tests/test_integration.py

import pytest
from tokenizer import download, clean_text, tokenize, count_words

@pytest.mark.integration
def test_integration_process_3():
    # List of book id's to download from project gutenberg
    text_numbers = [1063, 1064, 2151, 10031, 10947, 15143, 17192, 25525, 32037, 51060]

    # Download raw data
    raw_texts = download(text_numbers)
    assert isinstance(raw_texts, list), "Expected list of downloaded texts"
    assert all(isinstance(text, str) for text in raw_texts), "Expected each downloaded text to be a string"
    
    for raw_data in raw_texts:
        # Clean data
        cleaned_data = clean_text(raw_data)
        assert isinstance(cleaned_data, str), "Expected cleaned data to be a string"

        # Tokenize data
        tokens = tokenize(cleaned_data)
        assert isinstance(tokens, list), "Expected tokens to be a list"
        assert len(tokens) > 0, "Expected non-empty list of tokens"

        # Count common words
        common_words_count = count_words(cleaned_data)
        assert isinstance(common_words_count, dict), "Expected count of common words to be a dictionary"
        assert len(common_words_count) > 0, "Expected non-empty dictionary of word counts" 

#@pytest.mark.integration
#def test_integration_process_1():
    #Example integration test scenario
    #download_result = download()
    #cleaned_text = clean_text(download_result)
    #tokens = tokenize(cleaned_text)
    #common_words_count = count_words(tokens)

    #assert common_words_count >=0, "Expected positive count of common words"

    #assert isinstance(common_words_count, int), f"Expected integer count of common words,got {type(common_words_count)}"

