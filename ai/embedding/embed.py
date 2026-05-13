#! /usr/bin/env python3

import os
import sys
import gensim.downloader
from gensim.models import KeyedVectors

# --- Portable Backend Logic ---
import matplotlib

def setup_backend():
  if os.environ.get('DISPLAY', '') == '':
    print("No GUI display detected. Saving to PNG.")
    matplotlib.use('Agg')
    return

  # Try WebAgg (Browser-based) first for WSL/Remote compatibility
  try:
    import tornado
    matplotlib.use('WebAgg')
    print("Using WebAgg backend. Opening plot in your browser...")
  except ImportError:
    print("Tornado not found. Install it for interactive browser plots.")
    # Fallback to Agg if we can't do interactive
    matplotlib.use('Agg')

setup_backend()
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# --- 1. Load Logic with Caching ---
CACHE_FILE = "glove_50.bin"

if os.path.exists(CACHE_FILE):
  print(f"Loading model from local cache: {CACHE_FILE}...")
  model = KeyedVectors.load_word2vec_format(CACHE_FILE, binary=True)
else:
  print("Loading model from gensim (this may take a minute)...")
  model = gensim.downloader.load("glove-wiki-gigaword-50")
  model.save_word2vec_format(CACHE_FILE, binary=True)

# --- 2. Define Word List ---
words = [
  'tower', 'building', 'skyscraper', 'roof', 'built',
  'dome', 'facade', 'constructed', 'lighthouse', 'apple', 'bicycle'
]

# --- 3. Extract Vectors ---
word_vectors = [model[w] for w in words]

# --- 4. PCA Projection ---
# PCA "compresses" the 50 dimensions into 2 dimensions for our 2D screen.
pca = PCA(n_components=2)
result = pca.fit_transform(word_vectors)

# --- 5. Plotting ---
plt.figure(figsize=(10, 8))
plt.scatter(result[:, 0], result[:, 1], edgecolors='k', c='red')

for i, word in enumerate(words):
  plt.annotate(
    word, xy=(result[i, 0], result[i, 1]), xytext=(5, 2),
    textcoords='offset points', ha='right', va='bottom'
  )

plt.title("2D Projection of Word Embeddings")
plt.grid(True)

if matplotlib.get_backend() == 'Agg':
  plt.savefig("embedding_map.png")
  print("Plot saved to embedding_map.png")
else:
  plt.show()
