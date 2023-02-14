# ------------------- 코드 파일 설명 -------------------#
'''
- 사용자 전체 리뷰의 긍정/부정/중립 개수와 비율 구하는 코드 (입력변수 23~28번)
- customer_data2_pos_neg_results(325) 폴더안에 325개 파일 읽어와서 customer_data2_pos_neg_ratio_results(325).xlsx에 저장
   -> 한 사용자의 각 댓글별 긍/부/중 판단된 데이터 사용한다는 뜻
- 리뷰어 이름, 키값도 컬럼으로 저장 (항상 모든 결과값에 있어야함)
  -> pos_neg_ratio_functions 함수 파일의 함수 사용
  -> get_x_variable_functions_4 함수 파일의 함수와 다른 함수(주의!)
'''

import pandas as pd
import os
import openpyxl
import numpy as np
from pos_neg_ratio_functions import *


# 새로운 워크북 만들기
wb = openpyxl.Workbook()

# 현재 시트 선택
sheet = wb.active

# ---------- 변수정의, 리스트 정의 -------------------#
global customer_name_list
customer_name_list = []

global customer_key_list
customer_key_list = []

global positive_percentage_list
positive_percentage_list = []

global negative_percentage_list
negative_percentage_list = []

global neutrality_percentage_list
neutrality_percentage_list = []

global total_pos_ratio_list
total_pos_ratio_list = []

global total_neg_ratio_list
total_neg_ratio_list = []

global total_neu_ratio_list
total_neu_ratio_list = []


# ------------------- main -------------------#
file_list = os.listdir("C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_pos_neg_results(1250)")

print(file_list)
print(len(file_list))

for file_name in file_list:
    direct = "C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_pos_neg_results(1250)\\{0}".format(file_name)
    # print(direct)
    xlsx = pd.read_excel(direct)
    # print(xlsx)

    # [함수 1] 리뷰어 이름 -> pos_neg_results_ratio_functions
    reviewer = userName(xlsx)
    print("리뷰어 이름: ", reviewer)
    customer_name_list.append(reviewer)

    # [함수 2] 리뷰어 키(넘버) -> pos_neg_results_ratio_functions
    reviewer_key = userKey(xlsx)
    print("리뷰어 넘버: ", reviewer_key)
    customer_key_list.append(reviewer_key)

    # [함수 3] 전체 댓글 수 (해당기간) -> pos_neg_results_ratio_functions
    reviews_num = reviews_count(xlsx)
    print("전체 댓글 수", reviews_num)

    # 긍정 개수
    posNum = positive_count(xlsx)
    print("긍정 개수:", posNum)

    # 부정 개수
    negNum = negative_count(xlsx)
    print("부정 개수:", negNum)

    # 중립 개수
    neuNum = neutrality_count(xlsx)
    print("중립 개수:", neuNum)

    # 긍정 비율
    posPer = positive_percentage(posNum, reviews_num)
    print("긍정 비율:", posPer)
    positive_percentage_list.append(posPer)

    # 부정 비율
    negPer = negative_percentage(negNum,reviews_num)
    print("부정 비율:", negPer)
    negative_percentage_list.append(negPer)

    # 중립 비율
    neuPer = neutrality_percentage(neuNum,reviews_num)
    print("중립 비율:", neuPer)
    neutrality_percentage_list.append(neuPer)

    # 전체 부정 비율
    total_neg_ratio_result = total_neg_ratio(xlsx)
    print("전체 부정 비율:", total_neg_ratio_result)
    total_neg_ratio_list.append(total_neg_ratio_result)

    # 전체 중립 비율
    total_neu_ratio_result = total_neu_ratio(xlsx)
    print("전체 중립 비율:", total_neu_ratio_result)
    total_neu_ratio_list.append(total_neu_ratio_result)

    # 전체 긍정 비율
    total_pos_ratio_result = total_pos_ratio(xlsx)
    print("전체 긍정 비율:", total_pos_ratio_result)
    total_pos_ratio_list.append(total_pos_ratio_result)

    print('-'*20)

# 리스트 확인
print(customer_name_list)
print(customer_key_list)
print(positive_percentage_list)
print(negative_percentage_list)
print(neutrality_percentage_list)

df = pd.DataFrame({'Customer_name': customer_name_list,'Customer_key': customer_key_list,
                   '28. 긍정 댓글 비율': positive_percentage_list, '29. 부정 댓글 비율': negative_percentage_list, '30. 중립 댓글 비율': neutrality_percentage_list,
                   '31. 전체 긍정 비율': total_pos_ratio_list, '32. 전체 부정 비율': total_neg_ratio_list, '33. 전체 중립 비율': total_neu_ratio_list})


df.to_excel(excel_writer='customer_data_pos_neg_ratio_results(1250).xlsx')