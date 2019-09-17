############################################
## text summary generator demo project ##########
## Input: 
##      - filename: full filename of the input text to summarise.
##      - summary_ratio: percentage of desired summarisation.
## Output:
##      - summary of the input text printed out in the console
############################################

import sys
import random
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')


stop_words = stopwords.words('english')
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Text articles dataset from https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/ 

###########################
## AUXILIARY FUNCTIONS
def remove_stopword(sentence):
    clean_sentence = ' '.join([c for c in sentence.split() if c not in stop_words])
    return clean_sentence

def process_sentence(sentence):
    processed = sentence.lower()
    for x in processed:
        if x in punctuations:
            processed = processed.replace(x," ");
    return processed
############################


if __name__ == '__main__': 
    # process command line arguments
    if len(sys.argv) < 2:
        print("Input error: usage -> python text_summary.py article_id summary_ratio")
        exit()

    article_id = int(sys.argv[1])
    summary_ratio = float(sys.argv[2])

    # load articles from dataset
    df = pd.read_csv('tennis_articles_v4.csv')

    # making sure we are loading an existing article in the dataset
    if article_id < 0:
        article_id = 0
    if article_id >= len(df['article_id']):
        article_id = len(df['article_id']) - 1
    
    input_text = df['article_text'][article_id]
    total_text_length = len(input_text.split(' ')) # total length in words of the text

    # tokenize input text
    raw_sentences = nltk.sent_tokenize(input_text)

    # clean the text
    # remove stop words
    clean_sentences = [process_sentence(s) for s in raw_sentences]
    processed_sentences = [remove_stopword(sentence) for sentence in clean_sentences]

    # count word frequencies
    words = [w for sentence in processed_sentences for w in sentence.split()]
    word_frequencies = nltk.FreqDist(words)
    
    
    # calculate sentences score
    # based on word frequencies
    sentence_score = []
    for i, sentence in enumerate(processed_sentences):
        sentence_score.append(0)
        for word in sentence.split():
            sentence_score[i] += word_frequencies[word]
    
    # sort sentences by word frequency score
    sentence_order = np.argsort(sentence_score)

    # build the summary by adding one sentence at a time
    # add high score first
    # stop once the desired summary_ratio is reached
    summary_size = 0
    summary_text = []
    for index in reversed(sentence_order):
        next_sentence = raw_sentences[index]
        summary_text.append(next_sentence)
        summary_size += len(next_sentence.split(' '))
        if summary_size * 1.0 / total_text_length * 100.0 > summary_ratio:
            break
    
    
    # Display results
    print('Input text length: {}'.format(total_text_length))
    print('Sumary length: {}'.format(summary_size * 1.0 / total_text_length * 100.0))
    print('Summary: ' )
    print(summary_text)
    print()
