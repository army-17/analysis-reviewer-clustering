# ------------------- 코드 파일 설명 -------------------#
'''
- 입력변수 1~27번 출력 코드
- customer_data1_numbering(125) 폴더안에 125개 파일 읽어와서 customer_data_x_variables_df1.xlsx에 저장
   -> 키 값 부여된 125개 데이터로 부터 구현!
- from get_x_variable_functions_4 파일의 함수들 사용
- 입력변수 설명 파일 참조! (함수명, 리스트명)
- global 선언 주의 할 것
'''

import pandas as pd
import os
import openpyxl
from get_x_variable_functions_5 import *
import numpy as np

# ---------- 변수정의, 리스트 정의 -------------------#
global userName_list
userName_list = []

global userKey_list
userKey_list = []

global ranking_list
ranking_list = []

global helpfulNum_list
helpfulNum_list = []

global star1_list
star1_list = []

global star2_list
star2_list = []

global star3_list
star3_list = []

global star4_list
star4_list = []

global star5_list
star5_list = []

global starAverage_list
starAverage_list = []

global reviews_count_list
reviews_count_list = []

global image_reviews_per_list
image_reviews_per_list = []

global drop_dupl_dates_per_list
drop_dupl_dates_per_list = []

global writting_cycle_mean_list
writting_cycle_mean_list = []

global length_review_list
length_review_list = []

global helpful_review_ratio_list
helpful_review_ratio_list = []

global noneNum_ratio_list
noneNum_ratio_list = []

global lastDate_Period_list
lastDate_Period_list = []

global session_reviewPortion_section1_list
session_reviewPortion_section1_list = []

global session_reviewPortion_section2_list
session_reviewPortion_section2_list = []

global session_reviewPortion_section3_list
session_reviewPortion_section3_list = []

global session_reviewPortion_section4_list
session_reviewPortion_section4_list = []

global session_reviewPortion_section5_list
session_reviewPortion_section5_list = []

global session_reviewPortion_spring_list
session_reviewPortion_spring_list = []

global session_reviewPortion_summer_list
session_reviewPortion_summer_list = []

global session_reviewPortion_fall_list
session_reviewPortion_fall_list = []

global session_reviewPortion_winter_list
session_reviewPortion_winter_list = []


# ---------------------------------------- main ---------------------------------------------------------#
file_list = os.listdir("C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_numbering(1250)")

print(file_list)
print(len(file_list))
#print(type(file_list))

for file_name in file_list:
    direct = "C:\\Users\\mingyeongkim\\Desktop\\clustering_project(1250)\\data\\customer_data_numbering(1250)\\{0}".format(file_name)
    # print(direct)
    xlsx = pd.read_excel(direct)
    # print(xlsx)

    # 1. 리뷰어 이름
    reviewer = userName(xlsx)
    print("리뷰어 이름: ", reviewer)
    userName_list.append(reviewer)

    # 2. 리뷰어 키(넘버)
    reviewer_key = userKey(xlsx)
    print("리뷰어 넘버: ", reviewer_key)
    userKey_list.append(reviewer_key)

    # 3. 리뷰어 랭킹 점수
    user_ranking = ranking(xlsx)
    print("사용자 랭킹: ", user_ranking)
    ranking_list.append(user_ranking)

    # 4. 총 도움이 돼요 수(해당기간)
    helpfulNum = helpful_count(xlsx)
    print("도움이 돼요 수(해당기간): ", helpfulNum)
    helpfulNum_list.append(helpfulNum)

    # 20. 리뷰어의 전체 댓글 수(해당기간) ---> 기준!
    reviews_num = reviews_count(xlsx)
    reviews_count_list.append(reviews_num)
    print("22. 리뷰어의 전체 댓글 수(해당기간)", reviews_num)

    # 5. 리뷰어의 별점1 비율
    star1Num = star1_count(xlsx, reviews_num)
    print("별점1 개수:", star1Num)
    star1_list.append(star1Num)

    # 6. 리뷰어의 별점2 비율
    star2Num = star2_count(xlsx, reviews_num)
    print("별점2 개수:", star2Num)
    star2_list.append(star2Num)

    # 7. 리뷰어의 별점3 비율
    star3Num = star3_count(xlsx, reviews_num)
    print("별점3 개수:", star3Num)
    star3_list.append(star3Num)

    # 8. 리뷰어의 별점4 비율
    star4Num = star4_count(xlsx, reviews_num)
    print("별점4 개수:", star4Num)
    star4_list.append(star4Num)

    # 9. 리뷰어의 별점5 비율
    star5Num = star5_count(xlsx, reviews_num)
    print("별점5 개수:", star5Num)
    star5_list.append(star5Num)

    # 10. 리뷰어의 평균 별점
    star_averages = star_average(star1Num, star2Num, star3Num, star4Num, star5Num)
    print("별점 평균: ", star_averages)
    starAverage_list.append(star_averages)

    # 23. 이미지 댓글 비율
    image_count, image_percent = image_reviews_per(xlsx, reviews_num)
    print("이미지 있는 댓글 수: ", image_count)
    print("23. 이미지 댓글 비율: ", image_percent)
    image_reviews_per_list.append(image_percent)

    # 11. 중복 날짜 제거 작성 비율
    date_num, drop_date_per = drop_dupl_date(xlsx, reviews_num)
    print("중복 날짜 제거 작성 수: ", date_num)
    print("11.중복 날짜 제거 수/ 전체 댓글 수: ", drop_date_per)
    drop_dupl_dates_per_list.append(drop_date_per)

    # 12. 작성 주기 평균
    cycle_mean = writting_cycle_mean(xlsx)
    print("작성 주기 평균: ", cycle_mean)
    writting_cycle_mean_list.append(cycle_mean)

    # 24. 리뷰 길이 평균(글자수)
    length_mean = count_length(xlsx, reviews_num)
    print("사용자 리뷰 길이 평균: ", length_mean)
    length_review_list.append(length_mean)

    # 26. 도움이 돼요 받은 댓글 비율
    helpful_review_ratios = helpful_review_ratio(xlsx, reviews_num)
    print("23. 도움이 돼요 받은 댓글 비율 :", helpful_review_ratios)
    helpful_review_ratio_list.append(helpful_review_ratios)

    # 27. None 리뷰 비율
    none_num_ratio = noneNum_ratio(xlsx, reviews_num)
    print("None 리뷰 비율 :", none_num_ratio)
    noneNum_ratio_list.append(none_num_ratio)

    # 13. 리뷰 작성하지 않은 기간
    lastdate_period = lastDate_Period(xlsx)
    print("마지막 작성 날짜 이후 기간 : ", lastdate_period)
    lastDate_Period_list.append(lastdate_period)

    # 14. 시즌별 작성 리뷰 비율 - Section1 (1월 - 3월)
    session_reviewPortion_section1 = sesson_reviewPortion_section1(xlsx, reviews_num)
    print("1월-4월 :", session_reviewPortion_section1)
    session_reviewPortion_section1_list.append(session_reviewPortion_section1)

    # 15. 시즌별 작성 리뷰 비율 - Section2 (4월 - 6월)
    session_reviewPortion_section2 = sesson_reviewPortion_section2(xlsx, reviews_num)
    print("5월-8월 :", session_reviewPortion_section2)
    session_reviewPortion_section2_list.append(session_reviewPortion_section2)

    # 16. 시즌별 작성 리뷰 비율 - Section3 (7월 - 9월)
    session_reviewPortion_section3 = sesson_reviewPortion_section3(xlsx, reviews_num)
    print("9월-12월 :", session_reviewPortion_section3)
    session_reviewPortion_section3_list.append(session_reviewPortion_section3)

    # 17. 시즌별 작성 리뷰 비율 - Section4 (10월 -12월)
    session_reviewPortion_section4 = sesson_reviewPortion_section4(xlsx, reviews_num)
    print("2021년 1월-3월 :", session_reviewPortion_section4)
    session_reviewPortion_section4_list.append(session_reviewPortion_section4)

    # 18. 시즌별 작성 리뷰 비율 - Section4 (2021년 1월 - 3월)
    session_reviewPortion_section5 = sesson_reviewPortion_section5(xlsx, reviews_num)
    print("2021년 1월-3월 :", session_reviewPortion_section5)
    session_reviewPortion_section5_list.append(session_reviewPortion_section5)

    # 19. 시즌별 작성 리뷰 비율 - spring (2020.03 - 2020.05, 2021.03)
    session_reviewPortion_spring = sesson_reviewPortion_spring(xlsx, reviews_num)
    print("봄 : ", session_reviewPortion_spring)
    session_reviewPortion_spring_list.append(session_reviewPortion_spring)

    # 20. 시즌별 작성 리뷰 비율 - summer (2020.06 - 2020.08)
    session_reviewPortion_summer = sesson_reviewPortion_summer(xlsx, reviews_num)
    print("여름 :", session_reviewPortion_summer)
    session_reviewPortion_summer_list.append(session_reviewPortion_summer)

    # 21. 시즌별 작성 리뷰 비율 - fall (2020.09 - 2020.11)
    session_reviewPortion_fall = sesson_reviewPortion_fall(xlsx, reviews_num)
    print("가을 :", session_reviewPortion_fall)
    session_reviewPortion_fall_list.append(session_reviewPortion_fall)

    # 22. 시즌별 작성 리뷰 비율 - winter (2020.12 - 2021.02)
    session_reviewPortion_winter = sesson_reviewPortion_winter(xlsx, reviews_num)
    print("겨울 :", session_reviewPortion_winter)
    session_reviewPortion_winter_list.append(session_reviewPortion_winter)

    print("=======================================================")

# 리스트 확인 (1~27 순서대로 배열)
print(userName_list)
print(userKey_list)
print(ranking_list)
print(helpfulNum_list)
print(star1_list)
print(star2_list)
print(star3_list)
print(star4_list)
print(star5_list)
print(starAverage_list)
print(drop_dupl_dates_per_list)
print(writting_cycle_mean_list)
print(lastDate_Period_list)
print(session_reviewPortion_section1_list)
print(session_reviewPortion_section2_list)
print(session_reviewPortion_section3_list)
print(session_reviewPortion_section4_list)
print(session_reviewPortion_section5_list)
print(image_reviews_per_list)
print(length_review_list)
print(reviews_count_list)
print(helpful_review_ratio_list)
print(noneNum_ratio_list)
print(session_reviewPortion_spring_list)
print(session_reviewPortion_summer_list)
print(session_reviewPortion_fall_list)
print(session_reviewPortion_winter_list)


df = pd.DataFrame({'1. 리뷰어 이름': userName_list, '2. 리뷰어 키(넘버)': userKey_list, '3. 리뷰어 랭킹 점수': ranking_list, '4. 총 도움이 돼요 수(해당기간)': helpfulNum_list,
                   '5. 별점 1 비율': star1_list, '6. 별점 2 비율': star2_list, '7. 별점 3 비율': star3_list, '8. 별점 4 비율': star4_list,
                   '9. 별점 5 비율': star5_list, '10. 별점 평균': starAverage_list,
                   "11. 중복 날짜 제거 작성 비율": drop_dupl_dates_per_list, "12. 작성 주기 평균": writting_cycle_mean_list, '13. 리뷰 작성하지 않은 기간': lastDate_Period_list,
                   "14. 시즌별 작성 리뷰 비율(1월 - 3월)": session_reviewPortion_section1_list, "15. 시즌별 작성 리뷰 비율(4월 - 6월)": session_reviewPortion_section2_list,
                   "16. 시즌별 작성 리뷰 비율(7월 - 9월)": session_reviewPortion_section3_list, "17. 시즌별 작성 리뷰 비율(10월 - 12월)": session_reviewPortion_section4_list,
                   "18. 시즌별 작성 리뷰 비율(2021년 1월 - 3월)": session_reviewPortion_section5_list,
                   "19. 시즌별 작성 리뷰 비율(봄)": session_reviewPortion_spring_list, "20. 시즌별 작성 리뷰 비율(여름)": session_reviewPortion_summer_list,
                   "21. 시즌별 작성 리뷰 비율(가을)": session_reviewPortion_fall_list, "22. 시즌별 작성 리뷰 비율(겨울)": session_reviewPortion_winter_list,
                   "23.이미지 댓글 비율": image_reviews_per_list, "24. 리뷰 길이 평균(글자수)": length_review_list,
                   "25. 리뷰어의 전체 댓글 수(해당기간)": reviews_count_list,
                   '26. 도움이 돼요 받은 댓글 비율': helpful_review_ratio_list, '27. None 리뷰 비율': noneNum_ratio_list})

df.to_excel(excel_writer='customer_data_x_variables_df1(1250).xlsx')

