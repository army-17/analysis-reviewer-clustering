from sklearn.preprocessing import MinMaxScaler
import pandas as pd
# -------------------함수 선언--------------- #
# 함수 1, 2, 3은 새로 생성한 함수! -> x_variable_functions_4에 있는 함수들과 다름!

#1. 리뷰어 이름
def userName(xlsx):
    name = xlsx.loc[0].iloc[1]
    return name

#2. 리뷰어 키
def userKey(xlsx):
    key = xlsx.loc[0].iloc[2]
    return key

#3. 리뷰어의 전체 댓글 개수(2020~2021.03)
def reviews_count(xlsx):
    reviews_counts = len(xlsx.iloc[:, 9])
    return reviews_counts

#4. 긍정 댓글 개수
def positive_count(xlsx):

    positive_count = 0
    for i in xlsx.iloc[:,9]:

        if i == '긍정':
            positive_count += 1
            continue
    return positive_count

#5. 부정 댓글 개수
def negative_count(xlsx):

    negative_count = 0
    for i in xlsx.iloc[:,9]:

        if i == '부정':
            negative_count += 1
        else:
            continue
    return negative_count

#6. 중립 댓글 개수
def neutrality_count(xlsx):

    neutrality_count = 0
    for i in xlsx.iloc[:,9]:

        if i == '중립':
            neutrality_count += 1
        else:
            continue
    return neutrality_count

# [함수 28] 긍정 댓글 비율
def positive_percentage(posNum,reviews_num):

    positive_percentage_num = (posNum/reviews_num)

    return positive_percentage_num

# [함수 29] 부정 댓글 비율
def negative_percentage(negNum,reviews_num):

    negative_percentage_num = negNum/reviews_num

    return negative_percentage_num

# [함수 30] 중립 댓글 비율
def neutrality_percentage(neuNum,reviews_num):

    neutrality_percentage_num = neuNum /reviews_num

    return neutrality_percentage_num

# [함수 31] 전체 긍정 비율
def total_pos_ratio(df_finish):
    scaler = MinMaxScaler()
    df_scaler = df_finish[['negative', 'neutral', 'positive']]
    df_scaler = df_scaler.T

    df_scaled = scaler.fit_transform(df_scaler.values)
    df_scaled = pd.DataFrame(df_scaled)
    df_scaled_list = df_scaled.values.tolist()

    i = len(df_finish)
    same_value = 0
    for g in range(0, i):
        if (df_finish['negative'][g] == df_finish['neutral'][g]) \
                and (df_finish['neutral'][g] == df_finish['positive'][g]) \
                and (df_finish['negative'][g] != 0) \
                and (df_finish['neutral'][g] != 0) \
                and (df_finish['positive'][g] != 0):
            same_value = same_value + 1

    total_pos_ratio = (sum(df_scaled_list[2]) + same_value) / i

    return total_pos_ratio

# [함수 32] 전체 부정 비율
def total_neg_ratio(df_finish):
    scaler = MinMaxScaler()
    df_scaler = df_finish[['negative', 'neutral', 'positive']]
    df_scaler = df_scaler.T

    df_scaled = scaler.fit_transform(df_scaler.values)
    df_scaled = pd.DataFrame(df_scaled)
    df_scaled_list = df_scaled.values.tolist()

    i = len(df_finish)
    same_value = 0
    for g in range(0,i):
            if (df_finish['negative'][g] == df_finish['neutral'][g])\
                and (df_finish['neutral'][g] == df_finish['positive'][g])\
                and (df_finish['negative'][g] != 0)\
                and (df_finish['neutral'][g] != 0)\
                and (df_finish['positive'][g] != 0):
                same_value = same_value + 1

    total_neg_ratio = (sum(df_scaled_list[0]) + same_value) / i

    return total_neg_ratio

# [함수 33] 전체 중립 비율
def total_neu_ratio(df_finish):
    scaler = MinMaxScaler()
    df_scaler = df_finish[['negative', 'neutral', 'positive']]
    df_scaler = df_scaler.T

    df_scaled = scaler.fit_transform(df_scaler.values)
    df_scaled = pd.DataFrame(df_scaled)
    df_scaled_list = df_scaled.values.tolist()

    i = len(df_finish)
    same_value = 0
    for g in range(0, i):
        if (df_finish['negative'][g] == df_finish['neutral'][g]) \
                and (df_finish['neutral'][g] == df_finish['positive'][g]) \
                and (df_finish['negative'][g] != 0) \
                and (df_finish['neutral'][g] != 0) \
                and (df_finish['positive'][g] != 0):
            same_value = same_value + 1

    total_neu_ratio = (sum(df_scaled_list[1]) + same_value) / i

    return total_neu_ratio


