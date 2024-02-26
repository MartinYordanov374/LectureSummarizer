from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import TextPreProcessing

# calculate TF-IDF for each sentence
data = TextPreProcessing.preprocess_data('This is the text')
print(data)
# get cosine similarity between each of the results
# return top N results, N will determined by pdf content length
