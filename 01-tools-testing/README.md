# Folder overview

There are Jupyter Notebooks, where we tested different tool for Ukrainian NLP.

**01-base-text-preparation-example.ipynb**

This notebook contains function for text preparatio: 

- Remove paragraphs
- Convert all characters to lowercase from list of tokenized words
- Remove punctuation from list of tokenized words
- Replace all interger occurrences in list of tokenized words with textual representation

Also, this functions was test on news text from BBC website.

**02-lemmatization-ukrainian-texts.ipynb**

Lemetization flow is more difficalt than stemming. We used [LanguageTool API NLP UK](https://github.com/brown-uk/nlp_uk) for it.

We need to clone this repository:

`git clone https://github.com/brown-uk/nlp_uk.git`

And use this command for lemmatization:

`groovy LemmatizeText.groovy -i <input_file> -o <output_file>`


**03-stemming-ukrainian-text.ipynb**

Install needed package for the stemming:

`pip install git+https://github.com/Desklop/Uk_Stemmer`

There are testing of ukrainian stemmer based on the simple sentence.

