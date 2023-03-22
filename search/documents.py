from collections import Counter
from dataclasses import dataclass

from .analysis import analyze

@dataclass
class Abstract:
    """
    Wikipedia abstract
    """
    ID: int
    title: str
    abstract: str
    url: str

    def __post_init__(self):
        self.term_frequencies = Counter()

    @property
    def fulltext(self):
        """
        Combine the title and abstract into a single text
        """
        return ' '.join([self.title, self.abstract])

    def analyze(self):
        """
        Analyze the fulltext and store the term frequencies
        """
        self.term_frequencies = Counter(analyze(self.fulltext))

    def term_frequency(self, term):
        """
        Get the frequency of a term in the fulltext
        """
        return self.term_frequencies.get(term, 0)
