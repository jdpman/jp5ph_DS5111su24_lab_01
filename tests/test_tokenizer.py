import sys
sys.path.append('.')

import pytest
from tokenizer import tokenize

@pytest.mark.parametrize("text", [
    ('But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.')
])

def test_tokenize(text):
    # Given a string `text` with words
    # When I pass `text` to the `tokenize()` function
    # Then I should get a list of words as output

    tokens = tokenize(text)

    # Assertions
    assert isinstance(tokens, list), f"Expected list as output, but got {type(tokens)}"
    assert len(tokens) > 0, "Expected non-empty list of tokens"
    assert all(isinstance(token, str) for token in tokens), "Expected all tokens to be strings"

    # Additional checks (optional)
    assert tokens == tokenize(text.lower()), "Expected tokenization to be case insensitive"
    assert len(tokens) == 25, f"Expected 25 tokens, but got {len(tokens)}"  # Adjust expected count based on actual output

if __name__ == "__main__":
    pytest.main()

