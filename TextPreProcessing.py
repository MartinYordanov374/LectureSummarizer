import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import contractions
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

Lemmatizer = WordNetLemmatizer()
def preprocess_data(fileContent):
    # get text input
    file_content = fileContent
    # extract sentences
    file_sentences = sent_tokenize(file_content)
    
    # make sure that the sentences order is shown in the resulting structure
    sentence_words = [word_tokenize(file_sentence.lower()) for file_sentence in file_sentences]

    # get rid of stopwords
    clean_sentences = [cleanSentenceWord for sentence in sentence_words for cleanSentenceWord in sentence if cleanSentenceWord not in stopwords.words('english')]
    
    cleaned_text = " ".join(clean_sentences).split(' . ')

    regex_tokenizer = RegexpTokenizer(r'\w+')
    punctuation_clean_sentences = [regex_tokenizer.tokenize(sentence) for sentence in cleaned_text]
    joined_punctuation_clean_sentences = [" ".join(punctuation_clean_sentence) for punctuation_clean_sentence in punctuation_clean_sentences]
    print(joined_punctuation_clean_sentences[0])

    # lemmatize adjectives
    
    lemmatized_text_adjectives = [' '.join([Lemmatizer.lemmatize(word, pos='a') for word in word_tokenize(sentence)]) for sentence in joined_punctuation_clean_sentences]
    # lemmatize verbs

    lemmatized_text_verbs = [' '.join([Lemmatizer.lemmatize(word, pos='v') for word in word_tokenize(sentence)]) for sentence in lemmatized_text_adjectives]
    # lemmatize nouns (assuming you meant to lemmatize nouns)
    lemmatized_text_nouns = [' '.join([Lemmatizer.lemmatize(word, pos='n') for word in word_tokenize(sentence)]) for sentence in lemmatized_text_verbs]

    return lemmatized_text_nouns