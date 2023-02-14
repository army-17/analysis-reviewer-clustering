'''
- 불일치 비율 구하는 파일
- customer_data2_pos_neg_matchStar_results(325) 폴더/ 325개 파일 읽어와서 구함
'''


import pandas as pd
import os
import openpyxl
import numpy as np


# ------------------------함수 정의-----------------------------

# [함수1] 리뷰어 이름
def userName(xlsx):
    name = xlsx.loc[0].iloc[1]
    return name

# [함수2] 리뷰어 키
def userKey(xlsx):
    key = xlsx.loc[0].iloc[2]
    return key

# [함수3] 리뷰어의 전체 댓글 개수(2020~2021.03)
def reviews_count(xlsx):
    reviews_counts = len(xlsx.iloc[:, 3])
    return reviews_counts

# [함수] 불일치 리뷰 수
def discord_num_ratio(xlsx,reviews_num):

    neg4_num = 0
    for neg4 in xlsx.iloc[:,7]:

        if neg4 == 1:
            neg4_num += 1
        else:
            continue

    neg5_num = 0
    for neg5 in xlsx.iloc[:,8]:

        if neg5 == 1:
            neg5_num += 1
        else:
            continue

    pos1_num = 0
    for pos1 in xlsx.iloc[:,14]:

        if pos1 == 1 :
            pos1_num += 1
        else:
            continue

    pos2_num = 0
    for pos2 in xlsx.iloc[:,15]:


        if pos2 == 1:
            pos2_num += 1
        else:
            continue



    discord_num_ratio = (pos1_num + pos2_num + neg5_num + neg4_num)/reviews_num

    return discord_num_ratio

# ---------------------------------------------------------
global userName_list
userName_list = []

global userKey_list
userKey_list = []

global discord_portion_list
discord_portion_list = []


# 데이터 불러오기
file_list = os.listdir("C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_pos_neg_matchStar_results(1250)")

print(file_list)
print(len(file_list))


for file_name in file_list:
    direct = "C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_pos_neg_matchStar_results(1250)\\{0}".format(file_name)
    # print(xlsx)
    xlsx = pd.read_excel(direct)

    # 1. 리뷰어 이름
    reviewer = userName(xlsx)
    print("리뷰어 이름: ", reviewer)
    userName_list.append(reviewer)

    # 2. 리뷰어 키(넘버)
    reviewer_key = userKey(xlsx)
    print("리뷰어 넘버: ", reviewer_key)
    userKey_list.append(reviewer_key)

    reviews_num = reviews_count(xlsx)
    print("전체 댓글 수", reviews_num)

    # 34. 불일치 개수
    discords_num_ratio = discord_num_ratio(xlsx, reviews_num)
    print("불일치 여부 리뷰 비율:", discords_num_ratio)
    discord_portion_list.append(discords_num_ratio)

# 리스트 확인
print(userName_list)
print(userKey_list)
print(discord_portion_list)

df3 = pd.DataFrame({'1. 리뷰어 이름': userName_list, '2. 리뷰어 키(넘버)': userKey_list,  '34. 평점 댓글 불일치 비율': discord_portion_list})

df3.to_excel(excel_writer='get_x_variable_Discord(1250).xlsx')