"""
This module contains methods for counting words in a string
We shall make sure that the module adheres to PEP convention
We shall therefore run a linter to make sure this happens.
"""
# pylint: disable=R0903
# pylint: disable=C0303
# pylint: disable=E0401
import re
from bs4 import BeautifulSoup
class WordCounter:

    """
    Class to count words in a string
    """
    
    def __init__(self, words_string):
        """
        Constructor class: All global attributes listed here
        """
        assert isinstance(words_string, str), "input must be a string"
        self.words_string = words_string
    
    def count_words(self):
        """
        This is the method that counts words
        """
        # Before splitting we need to test if the words are html!
        self.run_string_through_html_filter()
        self.run_string_through_hyphen_filter()
        split_words = self.words_string.split()
        return len(split_words)
    
    def run_string_through_html_filter(self):
        """
        We need to run the words through a html filter
        in case the words are entrapped in a html text.
        Thus we need to extract text from a possible html
        sentence/text! We use Beautiful soup. One can use
        any other method
        """
        soup = BeautifulSoup(self.words_string, features="html.parser")
        if len(soup.find_all()) > 0:
            self.words_string = soup.get_text()
    
    def run_string_through_hyphen_filter(self):
        """
        We also want to count words separated by hyphens
        """
        self.words_string = re.sub("-", " ", self.words_string)

if __name__ == "__main__":
    WORDS = "My name is Joseph Njeri"
    print(WordCounter(WORDS).count_words())
