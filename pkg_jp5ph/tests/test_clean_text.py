import sys

sys.path.append('.')

import pytest
import logging
from tokenizer import clean_text

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@pytest.mark.parametrize('text, expected_text', [
    ('But the Raven, sitting lonely on the placid bust!','but the raven sitting lonely on the placid bust'),
    ('Once upon a midnight dreary, while I pondered, weak and weary...', 'once upon a midnight dreary while i pondered weak and weary'),
    ('And Le Corbeau, perche solitairement sur ce buste placide, parla...', 'and le corbeau perche solitairement sur ce buste placide parla')
])
def test_clean_text(text, expected_text):
    """
    Test the clean_text function.
    Given a text string:
    - When the text is passed to clean_text()
    - Then verify that the cleaned text matches the expected text.
    """
    logger.debug("Testing clean_text with text: %s", text)
    actual_text = clean_text(text)
    logger.debug("Expected text: %s", expected_text)
    logger.debug("Actual text: %s", actual_text)
    assert actual_text == expected_text, f"Failed on text: {text}"

