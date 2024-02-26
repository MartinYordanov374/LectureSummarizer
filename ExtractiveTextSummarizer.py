import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# get text input
file_content = 'This is a sample text that will be retrieved from the pdf later on.'
# tokenize data
tokenized_file_content = word_tokenize(file_content)

# get rid of stopwords
# expand contraction words
# lemmatize words