import re
import string
import Stemmer

# Top 25 most common words in English and "wikipedia":
# https://en.wikipedia.org/wiki/Most_common_words_in_English
STOPWORDS = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have',
                 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you',
                 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'wikipedia'])
PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))
STEMMER = Stemmer.Stemmer('english')

def tokenize(text):
    """Split the text into tokens"""
    return text.split()

def lowercase_filter(tokens):
    """Convert tokens to lowercase"""
    return [token.lower() for token in tokens]

def punctuation_filter(tokens):
    """Remove punctuation from tokens"""
    return [PUNCTUATION.sub('', token) for token in tokens]

def stopword_filter(tokens):
    """Remove stopwords from tokens"""
    return [token for token in tokens if token not in STOPWORDS]

def stem_filter(tokens):
    """Apply stemming to tokens"""
    return STEMMER.stemWords(tokens)

def analyze(text):
    """
    Analyze the text by tokenizing, lowercasing, removing punctuation,
    removing stopwords, and stemming
    """
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter(tokens)
    tokens = stem_filter(tokens)

    return [token for token in tokens if token]
