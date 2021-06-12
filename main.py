import pickle
import os
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import spacy
import time
import sys

def compute_key_words_distribution(key_words, w2v_model):
    key_words = [word.lower() for word in key_words]
    total_vector = []
    #print(key_words)
    for key_word in key_words:
        try:
            total_vector.append(w2v_model[key_word])
        except:
            print(key_word, 'is not in our corpus!')
            exit()
    #total_vector = np.array(total_vector)
    #average_vector = total_vector.mean(axis=0)
    #return average_vector
    return total_vector


def compute_papers_distribution(papers, w2v_model, nlp):
    '''
    total_vector = []
    for paper in papers:
        #paper = [word.lower() for word in paper]
        doc = nlp(paper)
        paper = [token.lemma_ for token in doc if (not token.is_stop) and (not token.is_punct)]
        for word in paper:
            try:
                total_vector.append(w2v_model[word])
            except:
                continue
    total_vector = np.array(total_vector)
    average_vector = total_vector.mean(axis=0)
    return average_vector
    #return total_vector
    '''
    total_vector = []
    for paper in papers:
        current_total_vector = []
        #paper = [word.lower() for word in paper]
        doc = nlp(paper)
        paper = [token.lemma_ for token in doc if (not token.is_stop) and (not token.is_punct)]
        for word in paper:
            try:
                current_total_vector.append(w2v_model[word])
            except:
                continue
        total_vector.append(current_total_vector)
    #total_vector = np.array(total_vector)
    return total_vector


def keywords_advisor_similarity(key_words_distribution, papers_distribution):
    '''
    score = np.dot(key_words_distribution, papers_distribution)
    score = score / np.linalg.norm(key_words_distribution, ord=2)
    score = score / np.linalg.norm(papers_distribution, ord=2)
    return score
    '''
    """
    max_score = -1
    for key_word in key_words_distribution:
        for paper in papers_distribution:
            score = np.dot(key_word, paper)
            score = score / np.linalg.norm(key_word, ord=2)
            score = score / np.linalg.norm(paper, ord=2)
            if score > max_score:
                max_score = score
    return max_score
    """
    total_score = []
    for paper in papers_distribution:
        max_score = -1
        for key_word in key_words_distribution:
            for paper_word in paper:
                score = np.dot(key_word, paper_word)
                score = score / np.linalg.norm(key_word, ord=2)
                score = score / np.linalg.norm(paper, ord=2)
                if score > max_score:
                    max_score = score
        total_score.append(max_score)
    total_score = np.array(total_score)
    return total_score.mean()



if __name__ == "__main__":
    start_time = time.time()
    #w2v_model = KeyedVectors.load_word2vec_format('./../data/word_vec.txt', binary=False)
    w2v_model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)
    #print(time.time() - start_time)
    data_path = os.path.join(os.path.dirname(__file__), "./data.pkl")
    f = open(data_path, 'rb')
    advisor_info = pickle.load(f)
    #key_words = 'recommendation'
    key_words=sys.argv[1]
    #print(w2v_model.most_similar(positive=["ai"]))
    #print(advisor_info)
    nlp = spacy.load('en_core_web_sm', disable=['ner', 'parser'])
    doc = nlp(key_words)
    #print([token for token in doc])
    key_words = [token.lemma_ for token in doc if (not token.is_stop) and (not token.is_punct)]
    #key_words = nlp.pipe(key_words)
    #print(key_words)
    key_words_distribution = compute_key_words_distribution(key_words, w2v_model)
    advisor_list = list(advisor_info.keys())
    #print(advisor_list)
    advisor_score_dict = {}
    for advisor in advisor_list:
        advisor_papers = advisor_info[advisor]['paper_list']
        papers_distribution = compute_papers_distribution(advisor_papers, w2v_model, nlp=nlp)
        score = keywords_advisor_similarity(key_words_distribution=key_words_distribution, papers_distribution=papers_distribution)
        advisor_score_dict[advisor] = score

    #print(sorted(advisor_score_dict.items(), key=lambda item: item[1], reverse=True))
    advisor_score_dict=sorted(advisor_score_dict.items(), key=lambda item: item[1], reverse=True)
    output=''
    ct=0
    for name,score in advisor_score_dict:
        ct+=1
        if ct>3:
            break
        score='%.2f'%score
        output=output+name+','+score+','
    print(output[:-1])
    #print(time.time() - start_time)
    #print(keywords_advisor_similarity(w2v_model['explainable'], w2v_model['interpret']))
    #print(w2v_model.similarity("interpret", 'explainable'))
    #print(np.linalg.norm(np.array(w2v_model['interpret']), ord=2))
    #print(w2v_model.most_similar(positive=["explainable"]))
    #print(np.linalg.norm(w2v_model['explainable'], ord=2))
    # print(w2v_model.most_similar(positive=["traffic"]))
    #print(w2v_model[])

    #path = os.path.join(os.path.dirname(__file__), "./../data/data(1).pkl")
    #f = open(path, 'rb')
    #info = pickle.load(f)
    #print(info)   #show file
    #print(len(info))
    #for i in info:
    #    print(i)
