from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import TextPreProcessing

# calculate TF-IDF for each sentence
GPT_Generated_text = "Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data. NLP has many applications, including machine translation, text summarization, sentiment analysis, and question answering systems. One of the fundamental tasks in NLP is text processing, which involves tokenization, stemming, lemmatization, and removing stop words. TF-IDF (Term Frequency-Inverse Document Frequency) is a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents. It helps in identifying the significance of words in a document corpus by considering both the frequency of occurrence of a word in a document and its rarity across the entire corpus. TF-IDF is widely used in information retrieval, document classification, and text mining tasks."
preprocessed_text = TextPreProcessing.preprocess_data(GPT_Generated_text)
Vectorizer = TfidfVectorizer()
Vectorized_matrix = Vectorizer.fit_transform([preprocessed_text])

# get cosine similarity between each of the results
# return top N results, N will determined by pdf content length
