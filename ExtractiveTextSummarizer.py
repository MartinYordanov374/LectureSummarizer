import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import contractions
from nltk.stem import WordNetLemmatizer

Lemmatizer = WordNetLemmatizer()

# get text input
file_content = "This is a sample text that won't be retrieved from the pdf later on."

# expand contraction words

no_contractions_content = contractions.fix(file_content)

# tokenize data
tokenized_file_content = word_tokenize(no_contractions_content)

# get rid of stopwords
cleaned_text = [clean_word for clean_word in tokenized_file_content if clean_word not in stopwords.words('english')]

# lemmatize words

for word in cleaned_text:
    if str.isalpha(word):
        print(word)