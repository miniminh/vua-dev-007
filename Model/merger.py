from sklearn.decomposition import PCA
from sklearn.manifold import SpectralEmbedding
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.manifold import TSNE
import numpy as np
import scipy 

def merge(X):
    X = X.T
    pca = PCA(n_components = 1)
    pca.fit(X)
    data_pca = pca.transform(X)
    return data_pca.T