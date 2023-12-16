from sklearn.decomposition import PCA
from sklearn.manifold import SpectralEmbedding
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.manifold import TSNE
import numpy as np

def merge(X, K = 1, spectral = 0, lle = 0, tsne = 0 ):
    if spectral == 1:
        embedding = SpectralEmbedding(n_components=K)
        return embedding.fit_transform(X).T.reshape(-1)
    elif tsne == 1:
        X_embedded = TSNE(n_components=K, learning_rate='auto',
                          init='random', perplexity=3).fit_transform(X)
        return X_embedded.reshape(-1)
    elif lle == 1:
        embedding = LocallyLinearEmbedding(n_components=K)
        return embedding.fit_transform(X).T.reshape(-1)
    else:
        return np.zeros(X.shape[1])