import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import contractions
from nltk.stem import WordNetLemmatizer

Lemmatizer = WordNetLemmatizer()
def preprocess_data(fileContent):
    # get text input
    file_content = fileContent
    # extract sentences
    file_sentences = sent_tokenize(file_content)
    
    # convert everything to lower case
    lowercase = [sentence.lower() for sentence in file_sentences]

    # expand contraction words
    
    no_contractions_content = contractions.fix(" ".join(lowercase))

    # tokenize data
    tokenized_file_content = word_tokenize(no_contractions_content)

    # get rid of stopwords
    cleaned_text = [clean_word for clean_word in tokenized_file_content if clean_word not in stopwords.words('english')]

    # lemmatize words
    lemmatized_text_adverbs = [Lemmatizer.lemmatize(word, pos='a') for word in cleaned_text if str.isalpha(word)]
    lemmatized_text_verbs = [Lemmatizer.lemmatize(word, pos='v') for word in lemmatized_text_adverbs if str.isalpha(word)]
    lemmatized_text_nouns = [Lemmatizer.lemmatize(word, pos='v') for word in lemmatized_text_verbs if str.isalpha(word)]

    return " ".join(lemmatized_text_nouns)