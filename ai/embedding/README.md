# Embedding

## GloVe - Global Vectors for Word Representation
We are working with a 50-dimensional space where words are represented 
as vectors. When we say words are "quite close," we mean their vectors 
point in nearly the same direction in this high-dimensional space.

## Similar words are "nearby"
To understand "nearby" in N-Dimensions, think of every word as a point 
in a room. We will note that:
* Building and Skyscraper share a "structural" axis.
* Tower and Lighthouse share a "verticality" and "height" axis.
* Facade and Dome share an "architectural detail" axis.

In a 50-dimensional model, these words aren't just close on one line; 
they form a cluster or a "neighborhood." When we run the code, we 
calculate the Cosine Similarity, which measures the angle between 
these vectors.

## Install
```bash
# REPO points to root of the repo
cd $REPO/embedding 

# install python virtual env
python3 -m venv .venv
source .venv/bin/activate
pip install pip-tools

# 1. Compile: Generates requirements.txt with pinned versions and hashes
pip-compile requirements.in

# 2. Sync: Installs exactly what is in requirements.txt and REMOVES anything else
pip-sync requirements.txt

# point to browser so that it can open automatically without errors
# Run the embed.py
BROWSER='/mnt/c/Program Files/Google/Chrome/Application/chrome.exe' embed.py
```
