from lookup.utils.token_utils import tokenize
from lookup.utils.embedding_utils import get_embedding, get_closest_index, read_phrases_csv, read_word2vec

class LookupAgent:
    def __init__(self, phrases_path, word2vec_path):
        self.phrases_path = phrases_path
        self.word2vec_path = word2vec_path
        self.phrases = None
        self.word2vec = None
        self.embeddings = None

    def load(self):
        self.phrases = read_phrases_csv(self.phrases_path)
        self.word2vec = read_word2vec(self.word2vec_path)
        self.embeddings = [get_embedding(tokenize(x), self.word2vec) for x in self.phrases]


    def get_closest_phrase(self, user_input):
        tokens = tokenize(user_input)
        embeddings = get_embedding(tokens, self.word2vec)
        closest_embedding, distance = get_closest_index(embeddings, self.embeddings)
        return self.phrases[closest_embedding], distance
