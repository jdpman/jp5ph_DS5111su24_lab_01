# tests/test_integration.py

import pytest
from tokenizer import clean_text, tokenize, count_words

@pytest.mark.integration
def test_integration_process_1():
    #Example integration test scenario
    #download_result = download()
    #cleaned_text = clean_text(download_result)
    tokens = tokenize(cleaned_text)
    common_words_count = count_words(tokens)

    assert common_words_count >=0, "Expected positive count of common words"

@pytest.mark.integration
def test_integration_process_2():
    # Another example integratio ntest scenario
    #download_result = download()
    cleaned_text = clean_text(download_result)
    tokens = tokenize(cleaned_text)
    common_words_count = count_common_words(tokens)

    assert isinstance(common_words_count, int), f"Expected integer count of common words,got {type(common_words_count)}"

@pytest.mark.integration
def test_integration_process_3():
    # Download raw data
    raw_data = download()
    assert isinstance(raw_data, str), "Expected downloaded data to be a string"

    # Clean data
    cleaned_data = clean_text(raw_data)
    assert isinstance(cleaned_data, str), "Expected cleaned data to be a string"

    # Tokenize data
    tokens = tokenize(cleaned_data)
    assert isinstance(tokens, list), "Expected tokens to be a list"
    assert len(tokens) > 0, "Expected non-empty list of tokens"

    # Count common words
    common_words_count = count_words(tokens)
    assert isinstance(common_words_count, int), "Expected count of common words to be an integer"
    assert common_words_count >= 0, "Expected positive count of common words"

