# pandas 패키지 임포트
import pandas as pd
import numpy as np


# read_excel() 함수를 이용하여 파일 불러오기
data = pd.read_excel('final_x_variables_results_2_(1250).xlsx')

#print(data)
print(data.columns)
print(len(data.columns))

print(type(data["4. 총 도움이 돼요 수(해당기간)"]))
print(type(data["10. 별점 평균"]))
print(type(data["12. 작성 주기 평균"]))
print(type(data["13. 리뷰 작성하지 않은 기간"]))
print(type(data["24. 리뷰 길이 평균(글자수)"]))
print(type(data["25. 리뷰어의 전체 댓글 수(해당기간)"]))


# 5. 총 도움이 돼요 수(해당기간)--------------------/
df1 = data["4. 총 도움이 돼요 수(해당기간)"]
#print(df1)

df1_no= (df1 - np.min(df1))/(np.max(df1)-np.min(df1))
print(df1_no)

data["4. 총 도움이 돼요 수(해당기간)"] = df1_no


# data["11. 별점 평균"] -------------------------/
df2 = data["10. 별점 평균"]
#print(df2)

df2_no= (df2 - np.min(df2))/(np.max(df2)-np.min(df2))
print(df2_no)

data["10. 별점 평균"] = df2_no
#print(data.columns)

# data["13. 작성 주기 평균"] -------------------------/
df3 = data["12. 작성 주기 평균"]
print(df3)

df3_no= (df3 - np.min(df3))/(np.max(df3)-np.min(df3))
print(df3_no)

data["12. 작성 주기 평균"] = df3_no

# data["14. 리뷰 작성하지 않은 기간"] -------------------------/
df4 = data["13. 리뷰 작성하지 않은 기간"]
print(df4)

df4_no = (df4 - np.min(df4))/(np.max(df4)-np.min(df4))
print(df4_no)

data["13. 리뷰 작성하지 않은 기간"] = df4_no

# data["20. 리뷰 길이 평균(글자수)"] -------------------------/
df5 = data["24. 리뷰 길이 평균(글자수)"]
print(df5)

df5_no = (df5 - np.min(df5))/(np.max(df5)-np.min(df5))
print(df5_no)

data["24. 리뷰 길이 평균(글자수)"] = df5_no

# data["22. 리뷰어의 전체 댓글 수(해당기간)"] -------------------------/
df6 = data["25. 리뷰어의 전체 댓글 수(해당기간)"]
print(df6)

df6_no = (df6 - np.min(df6))/(np.max(df6)-np.min(df6))
print(df6_no)

data["25. 리뷰어의 전체 댓글 수(해당기간)"] = df6_no
print(data.columns)
print(len(data.columns))


data.to_excel(excel_writer='final_x_variables_results_정규화_(1250).xlsx')

