import re
import unicodedata


def unicode_normalization(text):
    """"
    Remove string like "\xa0\"
    """
    normalized_text = unicodedata.normalize("NFKD", text)
    return normalized_text


def remove_paragraph(text_corpus):
    """"
    Remove "\n"
    """
    new_text_corpus = text_corpus.replace('\n','')
    return new_text_corpus


def remove_button_words(text):
    """"
    Remove button words like розгорнути / згорнути
    """
    new_text = text.replace('розгорнути','')
    new_text = new_text.replace('згорнути','')
    return new_text


def to_lowercase(text_corpus):
    """Convert all characters to lowercase from list of tokenized words"""
    words = text_corpus.split(' ')
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return ' '.join(new_words)


def remove_punctuation(text_corpus):
    """Remove punctuation from list of tokenized words"""
    words = text_corpus.split(' ')
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return ' '.join(new_words)


def remove_numbers(text):
    return ''.join([i for i in text if not i.isdigit()])


def text_normalization(text):
    new_text = unicode_normalization(text)
    new_text = remove_paragraph(new_text)
    new_text = remove_button_words(new_text)
    new_text = to_lowercase(new_text)
    new_text = remove_punctuation(new_text)
    new_text = remove_numbers(new_text)
    return new_text 