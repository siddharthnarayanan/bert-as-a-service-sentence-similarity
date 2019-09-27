#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Han Xiao <artex.xh@gmail.com> <https://hanxiao.github.io>

# NOTE: First install bert-as-service via
# $
# $ pip install bert-serving-server
# $ pip install bert-serving-client
# $

# simple similarity search on FAQ

import numpy as np
from bert_serving.client import BertClient
from termcolor import colored

# prefix_q = '##### **Q:** '
# topk = 5
# score_idx = 0

# with open('README.md') as fp:
#     questions = [v.replace(prefix_q, '').strip() for v in fp if v.strip() and v.startswith(prefix_q)]
#     print('%d questions loaded, avg. len of %d' % (len(questions), np.mean([len(d.split()) for d in questions])))

def scoring(pair):
    import math
    query_vec_1, query_vec_2 = bc.encode(pair)
    cosine = np.dot(query_vec_1, query_vec_2) / (np.linalg.norm(query_vec_1) * np.linalg.norm(query_vec_2))
    return 1/(1 + math.exp(-100*(cosine - 0.95)))


with BertClient(port=5555, port_out=5556, check_version=False) as bc:
    # doc_vecs = bc.encode(questions)
    # print('have reached here with questions: ', questions)
    
    from sentence_pairs import Pairs
    print("Start testing")
    
    for i, p in enumerate(Pairs):
        print("Similarity of Pair {}: ".format(i+1), scoring(p))
    
    
#    while True:
        # query_1 = input(colored('your sentence 1: ', 'green'))
        # query_2 = input(colored('your sentence 2: ', 'green'))
        # query_vec_1 = bc.encode([query_1])[0]
        # query_vec_2 = bc.encode([query_2])[0]
        # compute normalized dot product as score
        # score = np.dot(query_vec_1, query_vec_2) / (np.linalg.norm(query_vec_1) * np.linalg.norm(query_vec_2))
        
        # topk_idx = np.argsort(score)[::-1][:topk]

        # print('top %d questions similar to "%s"' % (topk, colored(query, 'green')))
        
        # for idx in topk_idx:
            # print('> %s\t%s\t%s\t%s' % (colored('%d' % idx, 'red'), colored('%.1f' % score[idx], 'cyan'), colored(questions[idx], 'yellow'), colored('%f' % score[::-1][score_idx], 'blue')))
            # score_idx+=1
        # print("similarity: ", score)