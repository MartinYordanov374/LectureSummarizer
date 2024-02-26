import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# get text input
file_content = 'This is a sample text that will be retrieved from the pdf later on.'
# tokenize data
tokenized_file_content = word_tokenize(file_content)

# get rid of stopwords

cleaned_text = [clean_word for clean_word in tokenized_file_content if clean_word not in stopwords.words('english')]

# expand contraction words
# lemmatize words