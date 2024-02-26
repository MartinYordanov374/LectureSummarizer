from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import TextPreProcessing
import numpy as np
import math

# calculate TF-IDF for each sentence
GPT_Generated_text = "The rise of artificial intelligence (AI) has revolutionized numerous industries, from healthcare to finance, education, and beyond. AI systems, powered by machine learning algorithms and vast amounts of data, have enabled unprecedented advancements in automation, decision-making, and problem-solving. However, along with its transformative potential, AI also raises ethical concerns regarding privacy, bias, job displacement, and the societal impacts of autonomous decision-making. Despite these challenges, AI continues to evolve rapidly, with ongoing research and development pushing the boundaries of what's possible. As we navigate this AI-driven era, it's crucial to foster responsible AI development and deployment to maximize its benefits while mitigating potential risks."
[original_sentences, preprocessed_text] = TextPreProcessing.preprocess_data(GPT_Generated_text)
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