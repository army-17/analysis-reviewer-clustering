# ------------------- 코드 파일 설명 -------------------#
'''
- 입력변수 1~27번 구현 함수 파일
  -> 순서대로 배치함
- 입력변수 설명 파일 참조!
'''

from datetime import datetime
from pandas import date_range

# -------------------함수 선언--------------- #

# [함수 1] 리뷰어 이름
def userName(xlsx):
    name = xlsx.loc[0].iloc[1]
    return name

# [함수 2] 리뷰어 키
def userKey(xlsx):
    key = xlsx.loc[0].iloc[11]
    return key

# [함수 3] 리뷰어 랭킹 점수
def ranking(xlsx):
    user_ranking = str(xlsx.loc[0].iloc[2]).strip()
    if user_ranking == '1,000+':
        return 0
    else:
        return 1

# [함수 4] 총 도움이 돼요 수(해당기간)
def helpful_count(xlsx):

    helpful_counts = 0
    for i in xlsx.iloc[:, 10]:
        if i == 'None' or i == '0':
            continue
        else:
            i = int(i)
            helpful_counts += i

    return helpful_counts

# [함수 5] 리뷰어의 별점1 비율
def star1_count(xlsx,reviews_num):

    star1_count = 0
    for j in xlsx.iloc[:,6]:

        if j == 1.0:
            star1_count += 1
        else:
            continue
    return star1_count/reviews_num

# [함수 6] 리뷰어의 별점2 비율
def star2_count(xlsx,reviews_num):

    star2_count = 0
    for j in xlsx.iloc[:,6]:

        if j == 2.0:
            star2_count += 1
        else:
            continue
    return star2_count/reviews_num

# [함수 7] 리뷰어의 별점3 비율
def star3_count(xlsx,reviews_num):

    star3_count = 0
    for j in xlsx.iloc[:,6]:

        if j == 3.0:
            star3_count += 1
        else:
            continue
    return star3_count/reviews_num

# [함수 8] 리뷰어의 별점4 비율
def star4_count(xlsx,reviews_num):

    star4_count = 0
    for j in xlsx.iloc[:,6]:

        if j == 4.0:
            star4_count += 1
        else:
            continue
    return star4_count/reviews_num

# [함수 9] 리뷰어의 별점5 비율
def star5_count(xlsx,reviews_num):

    star5_count = 0
    for j in xlsx.iloc[:,6]:

        if j == 5.0:
            star5_count += 1
        else:
            continue
    return star5_count/reviews_num

# [함수 10] 리뷰어 평균 별점
def star_average(star1Num, star2Num, star3Num, star4Num, star5Num):

    star_average_num = star1Num*1 + star2Num*2 + star3Num*3 + star4Num*4 + star5Num*5

    return star_average_num


# [함수 11] 중복 날짜 제거 작성 댓글 비율(중복 날짜 제거 수/ 전체 댓글 수[함수13])
def drop_dupl_date(xlsx, reviews_num):
    drop_dupl_dates = xlsx.drop_duplicates(['작성날짜'], keep='first')

    date_num = len(drop_dupl_dates.iloc[:, 7])
    drop_date_per = date_num/reviews_num

    return date_num, drop_date_per

# [함수 12] 작성 주기 평균
def writting_cycle_mean(xlsx):
    date_diff_list = []

    for i in range(0,len(xlsx.iloc[:,7])-1):

        date_start = str(xlsx.loc[i].iloc[7])
        date_end = str(xlsx.loc[i+1].iloc[7])

        date_start_obj = datetime.strptime(date_start, '%Y.%m.%d')
        date_end_obj = datetime.strptime(date_end, '%Y.%m.%d')

        date_diff = int((date_start_obj - date_end_obj).days)

        if date_diff != 0:
            date_diff_list.append(date_diff)
        else:
            continue

    if len(date_diff_list) != 0:
        mean = float(sum(date_diff_list) / len(date_diff_list))
        return mean
    else:
        mean = 0.0
        return mean

# [함수 13] 2021.03.31 기준 리뷰 작성하지 않은 기간
def lastDate_Period(xlsx):

    standard_date = '2021.03.31'
    lastdate = str(xlsx.iloc[(0, 7)])


    standard_date_obj = datetime.strptime(standard_date, '%Y.%m.%d')
    last_standard_date_obj = datetime.strptime(lastdate, '%Y.%m.%d')
    date_period = int((standard_date_obj - last_standard_date_obj).days)

    return date_period


# [함수 14] 시즌별 작성 리뷰 비율(1월 - 3월)
def sesson_reviewPortion_section1(xlsx, reviews_num):

    standard_date1 = '2020.01.01'
    standard_date2 = '2020.03.31'
    standard_date1_obj = datetime.strptime(standard_date1,'%Y.%m.%d')
    standard_date2_obj = datetime.strptime(standard_date2,'%Y.%m.%d')

    session_review_num_1 = 0

    i = datetime

    for i in xlsx.iloc[:, 7]:
        if i in date_range(standard_date1_obj,standard_date2_obj) :
            session_review_num_1 += 1
        else:
            continue

    session_reviewPortion_section1 = session_review_num_1 / reviews_num

    return session_reviewPortion_section1


# [함수 15] 시즌별 작성 리뷰 비율(4월 - 6월)

def sesson_reviewPortion_section2(xlsx , reviews_num):

    standard_date3 = '2020.04.01'
    standard_date4 = '2020.06.30'
    standard_date3_obj = datetime.strptime(standard_date3,'%Y.%m.%d')
    standard_date4_obj = datetime.strptime(standard_date4,'%Y.%m.%d')

    session_review_num_2 = 0

    i = datetime

    for i in xlsx.iloc[:, 7]:
        if i in date_range(standard_date3_obj,standard_date4_obj):
            session_review_num_2 += 1
        else :
            continue

    session_reviewPortion_section2 = session_review_num_2 / reviews_num

    return session_reviewPortion_section2


# [함수 16] 시즌별 작성 리뷰 비율(7월 - 9월)
def sesson_reviewPortion_section3(xlsx , reviews_num):

    standard_date5 = '2020.07.01'
    standard_date6 = '2020.09.30'
    standard_date5_obj = datetime.strptime(standard_date5,'%Y.%m.%d')
    standard_date6_obj = datetime.strptime(standard_date6,'%Y.%m.%d')

    session_review_num_3 = 0

    i = datetime

    for i in xlsx.iloc[:, 7]:
        if i in date_range(standard_date5_obj,standard_date6_obj):
            session_review_num_3 += 1
        else:
            continue

    session_reviewPortion_section3 = session_review_num_3 / reviews_num

    return session_reviewPortion_section3


# [함수 17] 시즌별 작성 리뷰 비율(2020년 10월 - 12월)
def sesson_reviewPortion_section4(xlsx , reviews_num):

    standard_date7 = '2020.10.01'
    standard_date8 = '2020.12.31'
    standard_date7_obj = datetime.strptime(standard_date7,'%Y.%m.%d')
    standard_date8_obj = datetime.strptime(standard_date8,'%Y.%m.%d')

    session_review_num_4 = 0

    i = datetime

    for i in xlsx.iloc[:, 7]:
        if i in date_range(standard_date7_obj,standard_date8_obj):
            session_review_num_4 += 1
        else:
            continue

    session_reviewPortion_section4 = session_review_num_4 / reviews_num

    return session_reviewPortion_section4


# [함수 18] 시즌별 작성 리뷰 비율(2021년 1월 - 3월)
def sesson_reviewPortion_section5(xlsx , reviews_num):

    standard_date9 = '2021.01.01'
    standard_date10 = '2021.03.31'
    standard_date9_obj = datetime.strptime(standard_date9,'%Y.%m.%d')
    standard_date10_obj = datetime.strptime(standard_date10,'%Y.%m.%d')

    session_review_num_5 = 0

    i = datetime

    for i in xlsx.iloc[:, 7]:
        if i in date_range(standard_date9_obj,standard_date10_obj):
            session_review_num_5 += 1
        else:
            continue

    session_reviewPortion_section5 = session_review_num_5 / reviews_num

    return session_reviewPortion_section5

# [함수 19] 계절별 작성 리뷰 비율( 봄 )
def sesson_reviewPortion_spring(xlsx, reviews_num):

    standard_date1 = '2020.03.01'
    standard_date2 = '2020.05.31'
    standard_date3 = '2021.03.01'
    standard_date4 = '2021.03.31'
    standard_date1_obj = datetime.strptime(standard_date1,'%Y.%m.%d')
    standard_date2_obj = datetime.strptime(standard_date2,'%Y.%m.%d')
    standard_date3_obj = datetime.strptime(standard_date3, '%Y.%m.%d')
    standard_date4_obj = datetime.strptime(standard_date4, '%Y.%m.%d')

    spring_review_num_1 = 0

    i = datetime

    for i in xlsx.iloc[:, 7]:
        if i in date_range(standard_date1_obj,standard_date2_obj) :
            spring_review_num_1 += 1
        if i in date_range(standard_date3_obj, standard_date4_obj) :
            spring_review_num_1 += 1
        else:
            continue

    session_reviewPortion_spring = spring_review_num_1 / reviews_num

    return session_reviewPortion_spring

# [함수 20] 계절별 작성 리뷰 비율( 여름 )
def sesson_reviewPortion_summer(xlsx, reviews_num):

    standard_date1 = '2020.06.01'
    standard_date2 = '2020.08.31'
    standard_date1_obj = datetime.strptime(standard_date1,'%Y.%m.%d')
    standard_date2_obj = datetime.strptime(standard_date2,'%Y.%m.%d')

    summer_review_num_1 = 0

    i = datetime

    for i in xlsx.iloc[:, 7]:
        if i in date_range(standard_date1_obj,standard_date2_obj) :
            summer_review_num_1 += 1
        else:
            continue

    session_reviewPortion_summer = summer_review_num_1 / reviews_num

    return session_reviewPortion_summer

# [함수 21] 계절별 작성 리뷰 비율( 가을 )
def sesson_reviewPortion_fall(xlsx, reviews_num):

    standard_date1 = '2020.09.01'
    standard_date2 = '2020.11.30'
    standard_date1_obj = datetime.strptime(standard_date1,'%Y.%m.%d')
    standard_date2_obj = datetime.strptime(standard_date2,'%Y.%m.%d')

    fall_review_num_1 = 0

    i = datetime

    for i in xlsx.iloc[:, 7]:
        if i in date_range(standard_date1_obj,standard_date2_obj) :
            fall_review_num_1 += 1
        else:
            continue

    session_reviewPortion_fall = fall_review_num_1 / reviews_num

    return session_reviewPortion_fall

# [함수 22] 계절별 작성 리뷰 비율( 겨울 )
def sesson_reviewPortion_winter(xlsx, reviews_num):

    standard_date1 = '2020.12.01'
    standard_date2 = '2021.02.28'
    standard_date1_obj = datetime.strptime(standard_date1,'%Y.%m.%d')
    standard_date2_obj = datetime.strptime(standard_date2,'%Y.%m.%d')

    winter_review_num_1 = 0

    i = datetime

    for i in xlsx.iloc[:, 7]:
        if i in date_range(standard_date1_obj,standard_date2_obj) :
            winter_review_num_1 += 1
        else:
            continue

    session_reviewPortion_winter = winter_review_num_1 / reviews_num

    return session_reviewPortion_winter

# [함수 23] 이미지 댓글 비율(이미지 있는 댓글 수/ 전체 댓글 수[함수13])
def image_reviews_per(xlsx, reviews_num):
    image_count = 0
    for i in xlsx.iloc[:, 8]:
        i = str(i)
        if i == '1':
            image_count += 1
        else:
            continue

    image_percent = image_count / reviews_num
    return image_count, image_percent


# [함수 24] 리뷰 길이 평균(글자수)
def count_length(xlsx, reviews_num):
    count = 0
    for i in xlsx.iloc[:, 9]:
        # print(i)
        count += len(str(i))

    length_mean = count / reviews_num
    return length_mean

# [함수 25] 리뷰어의 전체 댓글 개수(2020~2021.03)
def reviews_count(xlsx):
    reviews_counts = len(xlsx.iloc[:, 9])
    return reviews_counts


# [함수 26] 도움이 돼요 받은 댓글 비율
def helpful_review_ratio(xlsx, reviews_num):

    helpful_review_counts = 0

    for i in xlsx.iloc[:, 10]:
        if i == 'None' or i == '0':
            continue
        else:
            helpful_review_counts += 1

    helpful_review_portion = helpful_review_counts/reviews_num

    return helpful_review_portion


# [함수 27] None 리뷰 비율
def noneNum_ratio(xlsx,reviews_num):
    noneNum = 0

    for i in xlsx.iloc[:, 9]:

        if (i == 'None') or (i == '0') or (i == 0):
            noneNum += 1
        else:
            continue

    noneNum_portion = noneNum / reviews_num

    return noneNum_portion


