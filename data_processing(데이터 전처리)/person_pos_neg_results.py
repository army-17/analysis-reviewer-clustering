# ------------------- 코드 파일 설명 -------------------#
'''
- 한 사용자의 각 댓글 긍정/부정/중립 여부 판별
- customer_data2_numbering(325) 폴더안 325개 파일 읽어와서
  customer_data2_pos_neg_results(325) 폴더안에 325개 결과 파일 생성
- get_x_variable_functions_4 함수 파일의 함수 사용해서  리뷰어 이름, 키 값도 출력
- 맨마지막에 평점 컬럼 추가! -> 평점과 긍부정 판별 match 구하기 쉽게 하려고!
'''


import nltk
import pandas as pd
import numpy as np
import csv
import os
from get_x_variable_functions_5 import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import re

from konlpy.tag import Okt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from hanspell import spell_checker

# SettingWithCopyError
pd.set_option('mode.chained_assignment', None)

# KOSAC 감성사전 불러오기
table = dict()
with open('polarity.csv', 'r', -1, 'utf-8') as polarity:
    next(polarity)
    for line in csv.reader(polarity):
        key = str()
        for word in line[0].split(';'):
            key += word.split('/')[0]
        table[key] = {'Neg':line[3], 'Neut':line[4], 'Pos':line[6]}


# 데이터 불러오기
file_list = os.listdir("C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_numbering(1250)")

print(file_list)
print(len(file_list))

for file_name in file_list:
    direct = "C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_numbering(1250)\\{0}".format(file_name)
    df = pd.read_excel(direct)
    # print(xlsx)

    userInfo_list = []

    # 1. 리뷰어 이름 --> 입력변수 함수 사용! (get_x_variable_functions_3)
    reviewer = userName(df)
    print("리뷰어 이름: ", reviewer)
    userInfo_list.append(reviewer)

    # 2. 리뷰어 키(넘버) --> 입력변수 함수 사용! (get_x_variable_functions_3)
    reviewer_key = userKey(df)
    print("리뷰어 넘버: ", reviewer_key)
    userInfo_list.append(reviewer_key)

    # df1 생성 (첫번째 데이터 프레임)
    df1_columns = ['Customer_name','Customer_key']
    df1 = pd.DataFrame([userInfo_list], columns=df1_columns)
    print(df1)


    # 특수문자, 공백, 영어, 숫자 제거 (한글 제외 모든 문자 제거)
    df_clean = df["리뷰 내용"].str.replace(pat=r'[^가-힣]', repl=r'', regex=True)

    # df_clean 행 개수
    i = len(df_clean)

    # 불용어 텍스트 파일 불러오기
    f = open('koreanStopwords.txt','r',encoding='utf-8')
    lines = f.readlines()
    stop_words = []
    for line in lines:
        line = line.replace('\n','')
        stop_words.append(line)
    f.close()

    # 긍정, 부정, 중립, 결과 리스트 생성
    negative_list = []
    neutral_list = []
    positive_list = []
    result_list = []

    # 텍스트 전처리
    for f in range(0,i):
        # 맞춤법 검사 (hanspell)
        spelled_sent = spell_checker.check(df_clean[f])
        data_1 = spelled_sent.checked

        # 형태소 분리
        okt = Okt()
        data_2 = okt.morphs(data_1, stem=True)
        data_3 = " ".join(data_2)

        # 불용어 제거
        word_tokens = word_tokenize(data_3)
        delete_result = []
        for w in word_tokens:
            if w not in stop_words:
                delete_result.append(w)
        data_4 = " ".join(delete_result)

        # 표제어 처리
        data_5 = okt.morphs(data_4, stem=True)
        #print(data_5)

        # 감성사전 (긍정, 부정, 중립 비율 구하기)
        negative = 0
        neutral = 0
        positive = 0
        for word in data_5:
            if word in table:
                negative += float(table[word]['Neg'])
                neutral += float(table[word]['Neut'])
                positive += float(table[word]['Pos'])
        negative_list.append(negative)
        neutral_list.append(neutral)
        positive_list.append(positive)

    # 열 생성
    columns = ['negative', 'neutral', 'positive', 'blank', 'max', 'min', 'result']
    df_finish = pd.DataFrame(columns=columns)


    # 긍정, 부정, 중립, 최대값 데이터프레임에 추가
    df_finish['negative'] = negative_list
    df_finish['neutral'] = neutral_list
    df_finish['positive'] = positive_list
    df_finish['max'] = df_finish.max(axis=1)
    df_finish['min'] = df_finish.min(axis=1)

    # 긍정, 부정, 중립 문자 출력 (최대값)
    for g in range(0,i):
            if (df_finish['max'][g] == df_finish['negative'][g])\
                and (df_finish['max'][g] > df_finish['neutral'][g])\
                and (df_finish['max'][g] > df_finish['positive'][g]):
                result_list.append("부정")
            elif (df_finish['max'][g] == df_finish['neutral'][g])\
                and (df_finish['max'][g] > df_finish['negative'][g])\
                and (df_finish['max'][g] > df_finish['positive'][g]):
                result_list.append("중립")
            elif (df_finish['max'][g] == df_finish['positive'][g])\
                and (df_finish['max'][g] > df_finish['negative'][g])\
                and (df_finish['max'][g] > df_finish['neutral'][g]) :
                result_list.append("긍정")
            elif (df_finish['negative'][g] == 0)\
                and (df_finish['neutral'][g] == 0)\
                and (df_finish['positive'][g] == 0):
                result_list.append("blank")
            elif (df_finish['negative'][g] != 0)\
                and (df_finish['neutral'][g] != 0)\
                and (df_finish['negative'][g] != 0)\
                or ((df_finish['negative'][g] == df_finish['neutral'][g])\
                    and (df_finish['negative'][g] > df_finish['positive'][g])):
                result_list.append("부정")
            elif (df_finish['negative'][g] != 0)\
                and (df_finish['neutral'][g] != 0)\
                and (df_finish['negative'][g] != 0)\
                or ((df_finish['positive'][g] == df_finish['neutral'][g])\
                    and (df_finish['positive'][g] > df_finish['negative'][g])):
                result_list.append("긍정")
            elif (df_finish['negative'][g] != 0)\
                and (df_finish['neutral'][g] != 0)\
                and (df_finish['negative'][g] != 0)\
                or (df_finish['negative'][g] == df_finish['positive'][g]):
                result_list.append("중립")
            else:
                result_list.append("X")

    # 긍정, 부정, 중립 문자 값 데이터프레임에 추가
    df_finish['result'] = result_list

    # 빈칸 여부를 blank 열에 표시
    df_finish['blank'] = df_finish['blank'].fillna(0)
    for g in range(0,i):
        if (df_finish['result'][g] == 'blank'):
            df_finish['blank'].iloc[g] = 1

    # 데이터 프레임 출력 열 개수
    pd.set_option('display.max_rows',1000)

    # 최종 결과 출력
    print(df_finish)

    # 평점 컬럼 추가
    star_column = df.iloc[:, 6]
    list_from_df = star_column.values.tolist()
    #print(list_from_df)
    df_finish['리뷰 평점'] = list_from_df

    # df1,df2 합치기
    result_all = pd.concat([df1, df_finish], axis=1)
    print(result_all)
    person_pos_neg_result_filename = 'po_ne_result_{0}'.format(file_name)
    result_all.to_excel(excel_writer='C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_pos_neg_results(1250)\\{0}'.format(person_pos_neg_result_filename))

