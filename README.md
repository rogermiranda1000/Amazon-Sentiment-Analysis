# Amazon Sentiment Analysis
We'll use Natural Language Processing techniques in combination with Data Mining (Neural Networks) to extract sentiment analysis from Amazon reviews.

### Setup
As we'll be using Tensorflow with CUDA, we'll first need to setup a `conda` environment.
- Run `conda create --name sentiment-analysis`

Every time you want to run the code, start the environment with `conda activate sentiment-analysis`.

To use it with `jupyter`, run `python3 -m ipykernel install --user --name=sentiment-analysis`, and then run `jupyter notebook`. Remember to change the kernel (if you had another), under `Kernel > Change kernel > sentiment-analysis`.

#### Manual install
- `conda install -c conda-forge tensorflow`
- `conda install -c nvidia cuda`
- `conda install -c anaconda ipykernel`
- `python3 -m pip install gensim scikit-learn`
You have the dump (result `conda list -e`) on `requirements.txt`