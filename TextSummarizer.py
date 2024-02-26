from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import TextPreProcessing
import numpy as np
import math

def summarizeText(file_content):
    # calculate TF-IDF for each sentence
    [original_sentences, preprocessed_text] = TextPreProcessing.preprocess_data(file_content)
    Vectorizer = TfidfVectorizer()
    Vectorized_matrix = Vectorizer.fit_transform(preprocessed_text)

    # get cosine similarity between each of the results

    similarity_matrix = cosine_similarity(Vectorized_matrix)

    # return top N results, N will determined by pdf content length
    # Note thatn SummaryLength = N
    similarities = []
    for index, similarity in enumerate(similarity_matrix):
        similarities.append({'similarityID': index, 'similarity': np.sum(similarity[1]) / len(similarity_matrix)})

    sortedSimilarities = sorted(similarities, key = lambda x: x['similarity'], reverse=True)

    SummaryLength = math.floor(len(original_sentences) / 2)

    summary = []
    for sentenceID in range(SummaryLength):
        targetSentenceID = sortedSimilarities[sentenceID]['similarityID']
        summary.append(original_sentences[targetSentenceID])

    return summary[0]