import sys

sys.path.append('.')

import pytest 
from tokenizer import count_words

@pytest.mark.parametrize("text, expected_counts", [
    ('But the Raven, sitting lonely on the placid bust, spoke only that one word, as if his soul in that one word he did outpour.',
     {'but': 1, 'the': 2, 'raven': 1, 'sitting': 1, 'lonely': 1, 'on': 1, 'placid': 1, 'bust': 1,
      'spoke': 1, 'only': 1, 'that': 2, 'one': 2, 'word': 2, 'as': 1, 'if': 1, 'his': 1, 'soul': 1,
      'in': 1, 'that': 2, 'outpour': 1, 'did': 1, 'he': 1})
])
def test_count_words(text, expected_counts):
    """
    Test the count_words function.
    Given a text string:
    - When the text is passed to count_words()
    - Then verify that the returned dictionary has the correct word counts.
    """

    # Get actual word counts from count_words function
    actual_counts = count_words(text)

    # Assert that the actual counts match the expected counts
    assert actual_counts == expected_counts, f"Failed on text: {text}"

if __name__ == "__main__":
    pytest.main()


