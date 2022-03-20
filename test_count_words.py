"""
This module tests the module count_words.py
"""
# pylint: disable=R0903
# pylint: disable=R0201
# pylint: disable=C0303
import pytest
from count_words import WordCounter

class TestWordCounter:
    
    """
    Methods to test the WordCounter class
    """

    def test_empty(self):
        """
        Test if we can 0 words in a sample string
        """
        words = ""
        assert WordCounter(words).count_words() == 0

    def test_one(self):
        """
        Testing one word in a string
        """
        words = "Name"
        assert WordCounter(words).count_words() == 1
    
    def test_multiple_words(self):
        """
        Testing multiple words in a string
        """
        words = "Testing multiple words in a string"
        assert WordCounter(words).count_words() == 6
    
    def test_line_breaks(self):
        """
        Test if we can count words in a string separated
        by line breaks
        """
        words = "Test\nif\nwe\ncan\ncount\nwords\nwithin\nline\nbreaks"
        assert WordCounter(words).count_words() == 9
    
    def test_html(self):
        """
        Test whether we can count words entrapped with a html text
        """
        words = "<h1> This is a html heading </h1>"
        assert WordCounter(words).count_words() == 5
    
    def test_html_with_attributes(self):
        """
        Testing whether we can count text in html with attributes
        """
        words = '<h1 class="joseph">This html text has a class attribute</h1>'
        assert WordCounter(words).count_words() == 7
    
    def test_words_with_hyphens(self):
        """
        Testing words with hyphens
        """
        words = "Peter-Otto-von-Bismark"
        assert WordCounter(words).count_words() == 4
    
    def test_wrong_data_type(self):
        """
        Catching exception if wrong data type
        """
        words = ["I am not going anywhere"]
        with pytest.raises(Exception) as error:
            WordCounter(words).count_words()
        assert "input must be a string" in str(error.value)


# Test parameterizations: Running many tests in one

MY_TESTS = [
    ("", 0),
    ("Name", 1),
    ("Testing multiple words in a string", 6),
    ("Test\nif\nwe\ncan\ncount\nwords\nwithin\nline\nbreaks", 9),
    ("<h1> This is a html heading </h1>", 5),
    ('<h1 class="joseph">This html text has a class attribute</h1>', 7),
    ("Peter-Otto-von-Bismark", 4)
]

@pytest.mark.parametrize('input, output', MY_TESTS)
def test_all_in_one_function(input, output):
    assert WordCounter(input).count_words() == output