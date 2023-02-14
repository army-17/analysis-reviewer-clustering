# ------------------- 코드 파일 설명 -------------------#
'''
- 한 사용자별 각 리뷰들의 평점과 긍정/부정/중립 판단여부 매칭(-> 325개 파일 생성)

- customer_data2_pos_neg_results(325) 폴더안에 325개 파일 읽어와서 customer_data2_pos_neg_matchStar_results(325) 폴더에 325개 파일 생성
   -> 한 사용자의 각 댓글별 긍/부/중 판단된 데이터 사용한다는 뜻

- 리뷰어 이름, 키값도 컬럼으로 저장 (항상 모든 결과값에 있어야함)
  -> pos_neg_ratio_functions 함수 파일의 함수 사용
  -> get_x_variable_functions_4 함수 파일의 함수와 다른 함수(주의!)
'''

import nltk
import pandas as pd
import numpy as np
import csv
import os
from pos_neg_ratio_functions import *

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import re
import openpyxl

from konlpy.tag import Okt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from hanspell import spell_checker

# SettingWithCopyError
pd.set_option('mode.chained_assignment', None)

# ------------------- 평점과 감성분석 결과 일치 여부 변수 -------------------#

# 데이터 불러오기
file_list = os.listdir("C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_pos_neg_results(1250)")

print(file_list)
print(len(file_list))

for file_name in file_list:
    direct = "C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_pos_neg_results(1250)\\{0}".format(file_name)
    df_finish = pd.read_excel(direct)
    # print(xlsx)

    userInfo_list = []

    # 1. 리뷰어 이름 --> (pos_neg_results_ratio_functions)
    reviewer = userName(df_finish)
    print("리뷰어 이름: ", reviewer)
    userInfo_list.append(reviewer)

    # 2. 리뷰어 키(넘버) --> (pos_neg_results_ratio_functions)
    reviewer_key = userKey(df_finish)
    print("리뷰어 넘버: ", reviewer_key)
    userInfo_list.append(reviewer_key)

    review_num = reviews_count(df_finish)
    print("전체 리뷰 수:", review_num)
    userInfo_list.append(review_num)

    # df1 생성 (첫번째 데이터 프레임)
    df1_columns = ['Customer_name', 'Customer_key', "전체 리뷰 수"]
    df1 = pd.DataFrame([userInfo_list], columns=df1_columns)
    print(df1)

    # 변수 설정
    df_grade = df_finish['리뷰 평점']
    # print(df_grade)

    # 열 생성
    columns_value = ['negative_1', 'negative_2', 'negative_3', 'negative_4', 'negative_5',
                    'neutral_1', 'neutral_2', 'neutral_3', 'neutral_4', 'neutral_5',
                    'positive_1', 'positive_2', 'positive_3', 'positive_4', 'positive_5']
    df_value = pd.DataFrame(columns=columns_value)

    # 결과 리스트 생성
    negative_1_list = []
    negative_2_list = []
    negative_3_list = []
    negative_4_list = []
    negative_5_list = []
    neutral_1_list = []
    neutral_2_list = []
    neutral_3_list = []
    neutral_4_list = []
    neutral_5_list = []
    positive_1_list = []
    positive_2_list = []
    positive_3_list = []
    positive_4_list = []
    positive_5_list = []

    # 전체 리뷰 개수
    i = len(df_grade)

    # 평점과 감성분석 결과 일치 여부 확인
    for d in range(0,i):
        if (df_grade[d] == 1)\
                and (df_finish['result'][d] == "부정"):
            negative_1_list.append(1)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 2) \
                and (df_finish['result'][d] == "부정"):
            negative_1_list.append(0)
            negative_2_list.append(1)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 3) \
                and (df_finish['result'][d] == "부정"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(1)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 4) \
                and (df_finish['result'][d] == "부정"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(1)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 5) \
                and (df_finish['result'][d] == "부정"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(1)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 1)\
                and (df_finish['result'][d] == "중립"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(1)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 2) \
                and (df_finish['result'][d] == "중립"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(1)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 3) \
                and (df_finish['result'][d] == "중립"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(1)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 4) \
                and (df_finish['result'][d] == "중립"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(1)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 5) \
                and (df_finish['result'][d] == "중립"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(1)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 1)\
                and (df_finish['result'][d] == "긍정"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(1)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 2) \
                and (df_finish['result'][d] == "긍정"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(1)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 3) \
                and (df_finish['result'][d] == "긍정"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(1)
            positive_4_list.append(0)
            positive_5_list.append(0)
        elif (df_grade[d] == 4) \
                and (df_finish['result'][d] == "긍정"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(1)
            positive_5_list.append(0)
        elif (df_grade[d] == 5) \
                and (df_finish['result'][d] == "긍정"):
            negative_1_list.append(0)
            negative_2_list.append(0)
            negative_3_list.append(0)
            negative_4_list.append(0)
            negative_5_list.append(0)
            neutral_1_list.append(0)
            neutral_2_list.append(0)
            neutral_3_list.append(0)
            neutral_4_list.append(0)
            neutral_5_list.append(0)
            positive_1_list.append(0)
            positive_2_list.append(0)
            positive_3_list.append(0)
            positive_4_list.append(0)
            positive_5_list.append(1)

    # 데이터프레임에 리스트 추가
    df_value['negative_1'] = negative_1_list
    df_value['negative_2'] = negative_2_list
    df_value['negative_3'] = negative_3_list
    df_value['negative_4'] = negative_4_list
    df_value['negative_5'] = negative_5_list
    df_value['neutral_1'] = neutral_1_list
    df_value['neutral_2'] = neutral_2_list
    df_value['neutral_3'] = neutral_3_list
    df_value['neutral_4'] = neutral_4_list
    df_value['neutral_5'] = neutral_5_list
    df_value['positive_1'] = positive_1_list
    df_value['positive_2'] = positive_2_list
    df_value['positive_3'] = positive_3_list
    df_value['positive_4'] = positive_4_list
    df_value['positive_5'] = positive_5_list

    # 변수 결과 출력
    print(df_value)

    # 최종 결과 엑셀 파일로 저장
    result_all = pd.concat([df1, df_value], axis=1)
    person_pos_neg_result_filename = 'mathStar_{0}'.format(file_name)
    result_all.to_excel(excel_writer='C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_pos_neg_matchStar_results(1250)\\{0}'.format(person_pos_neg_result_filename))


