from gensim.models import KeyedVectors
import numpy as np
import pandas as pd
from scipy.spatial.distance import cdist


def read_word2vec(vectors_path):
    wv = KeyedVectors.load_word2vec_format(vectors_path)
    return wv


def read_phrases_csv(phrases_path):
    df = pd.read_csv(phrases_path)
    phrases = list(df['Phrases'])
    return phrases


def get_embedding(tokens, word2vec):

    combined_vectors = None
    normalized_vector = None

    for word in tokens:
        try:
            vector = word2vec.get_vector(word)
            if combined_vectors is None:
                combined_vectors = vector
            else:
                combined_vectors = combined_vectors + vector
        except KeyError as e:
            print(f"Word {word} not found in the embeddings. Skipping.")

    if combined_vectors is not None:
        norm = np.linalg.norm(combined_vectors)
        normalized_vector = combined_vectors / norm

    return normalized_vector


def get_closest_index(input_embeddings, phrases_embeddings):
    distances = cdist([input_embeddings], phrases_embeddings)
    index_min = np.argmin(distances[0])
    return index_min, distances[0][index_min]