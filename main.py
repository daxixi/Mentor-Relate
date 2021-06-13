import pickle
import os
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import spacy
import time
import socket


def compute_key_words_distribution(key_words, w2v_model):
    key_words = [word.lower() for word in key_words]
    total_vector = []
    flag=0
    for key_word in key_words:
        try:
            total_vector.append(w2v_model[key_word])
        except:
            flag=1
            return total_vector,flag
    return total_vector,flag


def compute_key_words_weights(key_words, w2v_model):
    key_words = [word.lower() for word in key_words]
    #print(key_words)
    weights = []
    #weights = np.array(weights)
    general_words = ['ai', 'artificial', 'intelligence', 'cv', 'computer', 'vision', 'machine', 'learning',
                     'datum', 'mining', 'natural', 'language', 'processing', 'web', 'information', 'retrieval',
                     'architecture', 'network', 'security', 'database', 'design', 'automation', 'system',
                     'computing', 'mobile', 'analysis', 'operating', 'programming', 'software', 'engineering',
                     'algorithm', 'complexity', 'cryptography', 'logic', 'verification', 'bioinformatics',
                     'graphic', 'economic', 'computation', 'robotic', 'visualization']
    for key_word in key_words:
        sim = []
        #sim = np.array(sim)
        key_word_vec = w2v_model[key_word]
        for general_word in general_words:
            general_word_vec = w2v_model[general_word]
            score = np.dot(key_word_vec, general_word_vec)
            score = score / np.linalg.norm(key_word_vec, ord=2)
            score = score / np.linalg.norm(general_word_vec, ord=2)
            score = float(score)
            sim.append(score)
        sim = np.array(sim)
        #print(sim)
        #print(sim.mean())
        top_k_idx = sim.argsort()[::-1][0:2]
        top_k_value = sim[top_k_idx]
        weights.append(float(1 - top_k_value.mean()))
    weights = np.array(weights)
    weights = weights / weights.sum()
    print(weights)
    return weights


def compute_papers_distribution(papers, w2v_model, nlp):
    total_vector = []
    for paper in papers:
        current_total_vector = []
        doc = nlp(paper)
        paper = [token.lemma_ for token in doc if (not token.is_stop) and (not token.is_punct)]
        for word in paper:
            try:
                current_total_vector.append(w2v_model[word])
            except:
                continue
        total_vector.append(current_total_vector)
    return total_vector


def keywords_advisor_similarity(key_words_distribution, papers_distribution, key_words_weights):
    total_score = []
    for paper in papers_distribution:
        max_score = [-1 for i in range(len(key_words_distribution))]
        for idx, key_word in enumerate(key_words_distribution):
            for paper_word in paper:
                score = np.dot(key_word, paper_word)
                score = score / np.linalg.norm(key_word, ord=2)
                score = score / np.linalg.norm(paper, ord=2)
                if score > max_score[idx]:
                    max_score[idx] = score
        max_score = np.array(max_score)
        total_score.append(float(np.dot(max_score, key_words_weights)))
        # total_score.append(max_score.mean())
    total_score = np.array(total_score)
    top_k_idx = total_score.argsort()[::-1][0:5]
    top_k_value = total_score[top_k_idx]
    #return total_score.mean()
    return top_k_value.mean()


if __name__ == "__main__":
    homepage={'Yijia Chen':'',
          'Yuxi Fu':'http://basics.sjtu.edu.cn/~yuxi/',
          'Dominik Scheder':'http://basics.sjtu.edu.cn/~dominik/',
          'Xiaoju Dong':'',
          'Huan Long':'',
          'Hongfei Fu':'https://jhc.sjtu.edu.cn/~hongfeifu/',
          'Chihao Zhang':'http://chihaozhang.com/',
          'Guihai Chen':'',
          'Xiaofeng Gao':'https://www.cs.sjtu.edu.cn/~gao-xf/',
          'Haibing Guan':'https://www.cs.sjtu.edu.cn/~hbguan/',
          'Minyi Guo':'https://www.cs.sjtu.edu.cn/~guo-my/',
          'Weijia Jia':'https://scholar.google.com/citations?hl=en&user=jtvFB20AAAAJ',
          'Jie Li':'https://www.cs.sjtu.edu.cn/~lijie/',
          'Feilong Tang':'',
          'Chentao Wu':'https://www.cs.sjtu.edu.cn/~wuct/',
          'Fan Wu':'https://www.cs.sjtu.edu.cn/~fwu/',
          'Bin Yao':'https://www.cs.sjtu.edu.cn/~yaobin/',
          'Quan Chen':'https://www.cs.sjtu.edu.cn/~chen-quan/',
          'Jingwen Leng':'https://www.cs.sjtu.edu.cn/~leng-jw/',
          'Yao Shen':'https://www.cs.sjtu.edu.cn/~yshen/',
          'Jieru Zhao':'https://zjru.github.io/',
          'Wenli Zheng':'',
          'Tao Song':'',
          'Jian Cao':'',
          'Linpeng Huang':'https://www.cs.sjtu.edu.cn/~HUANG-LP/',
          'Guangtao Xue':'https://www.cs.sjtu.edu.cn/~xue-gt/',
          'Yanmin Zhu':'https://www.cs.sjtu.edu.cn/~yzhu/',
          'Yuting Chen':'https://ddst.sjtu.edu.cn/MemberDetail.aspx?id=5',
          'Yanyan Shen':'https://www.cs.sjtu.edu.cn/~shen-yy/',
          'Hao Zhong':'https://drhaozhong.github.io/',
          'Dongliang Xue':'',
          'Hongtao Lu':'',
          'Kai Yu':'https://speechlab.sjtu.edu.cn/members/kai_yu',
          'Liqing Zhang':'https://bcmi.sjtu.edu.cn/~zhangliqing/',
          'Hai Zhao':'',
          'Junni Zou':'https://www.cs.sjtu.edu.cn/~zou-jn/',
          'Yi Hong':'https://cs.sjtu.edu.cn/~yihong/',
          'Fang Li':'https://www.cs.sjtu.edu.cn/~li-fang/',
          'Li Niu':'https://bcmi.sjtu.edu.cn/home/niuli/',
          'Rui Wang':'https://wangruinlp.github.io/',
          'Yang Yang':'https://yangy09.github.io/',
          'Yanmin Qian':'https://speechlab.sjtu.edu.cn/~ymqian/',
          'Lu Chen':'https://coai-sjtu.github.io/',
          'Mengyue Wu':'',
          'Yaqian Zhang':'',
          'Dawu Gu':'https://loccs.sjtu.edu.cn/main/#',
          'Xuejia Lai':'',
          'Shengli Liu':'',
          'Yuan Luo':'',
          'Li Yu':'http://yuyu.hk/',
          'Fan Cheng':'https://www.cs.sjtu.edu.cn/~chengfan/',
          'Ning Ding':'',
          'Zhen Liu':'',
          'Yu Long':'',
          'Lei Wang':'',
          'Yuanyuan Zhang':'http://yyjess.com/',
          'Lizhuang Ma':'https://dmcv.sjtu.edu.cn/',
          'Ruimin Shen':'https://cs.sjtu.edu.cn/~shen-rm/index_2.html',
          'Bin Sheng':'',
          'Yong Yu':'http://apex.sjtu.edu.cn/members/yyu',
          'Cewu Lu':'',
          'Junchi Yan':'https://thinklab.sjtu.edu.cn/',
          'Weinan Zhang':'http://wnzhang.net/',
          'Ning Zhang':'https://ning6688.github.io/',
          'Xiaoyao Liang':'https://acalab.sjtu.edu.cn/CN/Teacher.aspx?infolb=4&flag=4',
          'Li Jiang':'https://cs.sjtu.edu.cn/~jiangli/',
          'Chao Li':'https://www.cs.sjtu.edu.cn/~lichao/',
          'Jialiang Lu':'',
          'Zhezhi He':'https://elliothe.github.io/people/zhezhi-he',
          'Jing Ke':'',
          'Yaohui Jin':'https://loct.sjtu.edu.cn/team/detail.aspx?cid=12&id=7',
          'Yue Gao':'https://gaoyue.sjtu.edu.cn/',
          'Wei Shen':'https://shenwei1231.github.io/',
          'Chao Ma':'https://vision.sjtu.edu.cn/',
          'Yunbo Wang':'http://people.csail.mit.edu/yunbo/',
          'Bo Jiang':'https://jhc.sjtu.edu.cn/~bjiang/',
          'Ye Pan':'http://www0.cs.ucl.ac.uk/staff/Y.Pan/videos.html',
          'Yuting Wang':'https://jhc.sjtu.edu.cn/~yutingwang/',
          'Quanshi Zhang':'http://qszhang.com/',
          'Shizhen Zhao':'https://jhc.sjtu.edu.cn/~shizhenzhao/',
          'Dongyao Chen':'https://chendy.tech/',
          'Qinxiang Cao':'',
          'Jiaxin Ding':'https://jhc.sjtu.edu.cn/~jiaxinding/',
          'Haiming Jin':'https://jhc.sjtu.edu.cn/~haimingjin/',
          'Meng Jin':'http://tns.thss.tsinghua.edu.cn/sun/members/MengJin/MengJin.html',
          'Shuai Li':'https://shuaili8.github.io/',
          'Zhouhan Lin':'https://hantek.github.io/',
          'Yuye Ling':'http://www.yuyeling.com/',
          'Yehan Ma':'https://yehancpsl.github.io/',
          'Biaoshuai Tao':'https://jhc.sjtu.edu.cn/~bstao/',
          'Liyao Xiang':'http://xiangliyao.cn/',
          'Kuan Yang':'https://sites.google.com/view/kuanyang',
          'Nanyang Ye':'https://jhc.sjtu.edu.cn/people/members/faculty/nanyang-ye.html',
          'Yuhao Zhang':'http://www.zyhwtc.com/',
          'Guanjie Zheng':'https://jhc.sjtu.edu.cn/~gjzheng/',
          'Wen Chen':'',
          'Chengnian Long':'',
          'Xueming Si':'',
          'Yue Ding':''}
    
    start_time = time.time()
    #w2v_model = KeyedVectors.load_word2vec_format('./../data/word_vec.txt', binary=False)
    w2v_model = KeyedVectors.load_word2vec_format('./script/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)
    
    data_path = os.path.join(os.path.dirname(__file__), "./script/data2.pkl")
    f = open(data_path, 'rb')
    advisor_info = pickle.load(f)

    data_path_2 = os.path.join(os.path.dirname(__file__), "./script/data.pkl")
    f_2 = open(data_path_2, 'rb')
    advisor_info_2 = pickle.load(f_2)
    advisor_list_2 = list(advisor_info_2.keys())
    for advisor in advisor_list_2:
        advisor_info[advisor] = advisor_info_2[advisor]

    #print(w2v_model.similarity("interpret", 'explainable'))
    #print(advisor_info['Quanshi Zhang'])
    #key_words = 'traffic ai'
    print('Finish load')
    while True:
        server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        server.bind(('127.0.0.1',1883))
        server.listen(5)
        server, addr = server.accept()
        key_words=server.recv(10240)
        key_words=pickle.loads(key_words)
        #print(w2v_model.most_similar(positive=["ai"]))
        #print(advisor_info)
        nlp = spacy.load('en_core_web_sm', disable=['ner', 'parser'])
        doc = nlp(key_words)
        #print([token for token in doc])
        key_words = [token.lemma_ for token in doc if (not token.is_stop) and (not token.is_punct)]
        #key_words = nlp.pipe(key_words)
        #print(key_words)
        key_words_distribution,flag = compute_key_words_distribution(key_words, w2v_model)
        if flag==1:
            output='ggg'
            output=pickle.dumps(output)
            server.sendall(output)
            time.sleep(2)
            server.close()
            continue
        key_words_weights = compute_key_words_weights(key_words, w2v_model)
        advisor_list = list(advisor_info.keys())
        advisor_list.sort()
        #print(advisor_list)
        advisor_score_dict = {}
        for advisor in advisor_list:
            advisor_papers = advisor_info[advisor]['paper_list']
            papers_distribution = compute_papers_distribution(advisor_papers, w2v_model, nlp=nlp)
            score = keywords_advisor_similarity(key_words_distribution=key_words_distribution,
                                                papers_distribution=papers_distribution,
                                                key_words_weights=key_words_weights)
            advisor_score_dict[advisor] = score

        advisor_score_dict=sorted(advisor_score_dict.items(), key=lambda item: item[1], reverse=True)
        output=''
        ct=0
        for name,score in advisor_score_dict:
            ct+=1
            if ct>3:
                break
            score=0.5*score+0.5
            score='%.2f'%score
            output=output+name+','+score+','+homepage[name]+','
        output=output[:-1]
        output=pickle.dumps(output)
        server.sendall(output)
        time.sleep(2)
        server.close()

