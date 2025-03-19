from pymongo import MongoClient
from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.tokenize import word_tokenize
import numpy as np

nltk.download('punkt')

# Initialize MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['search_db']
collection = db['documents']

# Initialize BERT-based embeddings model
model = SentenceTransformer('all-MiniLM-L6-v2')

def keyword_search(query):
    results = collection.find({"$text": {"$search": query}})
    return list(results)

def ai_search(query, documents):
    query_embedding = model.encode(query, convert_to_tensor=True)
    answers = []
    for doc in documents:
        doc_embedding = model.encode(doc['content'], convert_to_tensor=True)
        score = util.pytorch_cos_sim(query_embedding, doc_embedding).item()
        answers.append({"title": doc['title'], "content": doc['content'], "score": score})
    sorted_answers = sorted(answers, key=lambda x: x['score'], reverse=True)
    return sorted_answers

def hybrid_search(query):
    # Keyword search
    keyword_results = keyword_search(query)
    
    # AI-powered search
    ai_results = ai_search(query, keyword_results)
    
    return ai_results


