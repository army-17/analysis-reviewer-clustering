import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import silhouette_score
import csv
import platform

# 한글 폰트 지원
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False


'''
차원 축소 한 클러스터링 모델
'''

# ----------------엑셀파일 가져오기------------------

# 1034개
# 23개 입력변수
#df = pd.read_excel('final_x_variables_results_정규화_2_(1250)_14-22제거.xlsx')

# 32개 입력변수
df = pd.read_excel('final_x_variables_results_정규화_2_(1250).xlsx')

# 클러스터링에 사용되는 입력변수 데이터 프레임
#df2 = df.iloc[:, 4:27]  # 아이디, 키 변수 제외한 변수
df2 = df.iloc[:, 4:36]
print(df2)


# -----------pca 차원 축소------------------------
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(df2)

# 2차원
principalDf = pd.DataFrame(data=principalComponents, columns = ['principal component1', 'principal component2'])

# 3차원
#principalDf = pd.DataFrame(data=principalComponents, columns = ['principal component1', 'principal component2', 'principal_component3'])

print(principalDf)

print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))


# -----------------최적 차원 개수----------------
cumsum1 = np.cumsum(pca.explained_variance_ratio_)
d = np.argmax(cumsum1 >= 0.80) + 1
print('선택할 차원 수 :', d)

# ------------------클러스터링-------------------

# 클러스터링
kmeans = KMeans(n_clusters=6, init='k-means++', n_init=25, random_state=0)
# kmeans = KMeans(n_clusters=2, init='random', n_init=20, random_state=0)

kmeans.fit(principalDf)

result = principalDf.copy()
result['cluster'] = kmeans.labels_


# --------------클러스터링 결과 그래프-----------------------
sns.scatterplot(x="principal component1", y="principal component2", hue="cluster", data=result,
                palette=['green', 'orange','blue','red','gray','pink'])

'''
# 범례 달기
for index, x, y in principalDf.itertuples():
    plt.annotate(index, (x, y))

plt.show()
'''
# print(kmeans)
print(result)

# 클러스터링 결과 엑셀파일 저장
result.to_excel(excel_writer='clustering_result2.xlsx')

# 각 군집에 포함된 리뷰어 인덱스 출력
print(result.index[result['cluster']==0])
print(result.index[result['cluster']==1])
print(result.index[result['cluster']==2])
print(result.index[result['cluster']==3])
print(result.index[result['cluster']==4])
print(result.index[result['cluster']==5])
print(result.index[result['cluster']==6])

# 각 군집에 포함된 리뷰어 인덱스 리스트화
a = result.index[result['cluster']==0]
b = result.index[result['cluster']==1]
c = result.index[result['cluster']==2]
d = result.index[result['cluster']==3]
e = result.index[result['cluster']==4]
g = result.index[result['cluster']==5]
h = result.index[result['cluster']==6]

# 군집별 인덱스 csv 파일로 출력
with open('listfile.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(a)
    writer.writerow(b)
    writer.writerow(c)
    writer.writerow(d)
    writer.writerow(e)
    writer.writerow(g)
    writer.writerow(h)


# 각 군집 개수 출력
print(len(result.index[result['cluster']==0]))
print(len(result.index[result['cluster']==1]))
print(len(result.index[result['cluster']==2]))
print(len(result.index[result['cluster']==3]))
print(len(result.index[result['cluster']==4]))
print(len(result.index[result['cluster']==5]))
print(len(result.index[result['cluster']==6]))


# -------------최적 군집 찾기--------------------------
# 1. 실루엣 점수(모델평가 지표)
scores = []
cluster_results = {}

for _n_clusters in np.arange(2, 11):
    kmeans.n_clusters = _n_clusters
    cluster_results[_n_clusters] = kmeans.fit(df2)
    scores.append(silhouette_score(df2, kmeans.labels_))

# 실루엣 점수 출력
print('실루엣 점수')
print(scores)

plt.figure(figsize=(12, 6))
plt.xlabel('clusters')
plt.ylabel('score')


plt.plot(np.arange(2, 11), scores, marker='s')
plt.show()


# 2. 엘보우 기법
def elbow(X):
    sse = []
    for i in range(1,11):
        km = KMeans(n_clusters=i, init='k-means++', n_init=20, random_state=0)
        km.fit(X)
        sse.append(km.inertia_)
    plt.plot(range(1,11),sse,marker='o')
    plt.xlabel('클러스터 개수')
    plt.ylabel('SSE')
    plt.show()

elbow(df2)


# -------------상관계수 테이블--------------------

# 입력변수 상관계수 구하기
corr = df2.corr()

# 히트맵 사이즈 설정
plt.figure(figsize = (15, 9))

# 히트맵 형태
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# 히트맵 그리기
sns.heatmap(data = corr,    # 'corr' = 상관계수 테이블
            annot = True,  # 히트맵에 값 표시
            mask=mask,   # 히트맵 형태. 여기서는 위에서 정의한 삼각형 형태
            fmt = '.2f',   # 값 표시 방식. 소숫점 2번째자리까지
            linewidths = 1.,  # 경계면 실선 구분 여부
            cmap = 'RdYlBu_r')  # 사용할 색 지정 ('python colormap 검색')

plt.title('상관계수 히트맵')

plt.show()

