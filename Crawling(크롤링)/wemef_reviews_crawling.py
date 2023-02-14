from selenium import webdriver
import time
import random
import pandas as pd
import openpyxl
from selenium.webdriver.common.keys import Keys

# 새로운 워크북 만들기
wb = openpyxl.Workbook()

# 현재 시트 선택
sheet = wb.active

# ---------- 변수정의, 리스트 정의 -------------------#
global productName_list
productName_list = []

global star1_list
star1_list = []

global written_date_list
written_date_list = []

global review_helpful_list
review_helpful_list = []

global image_list
image_list = []

global review_grade_list
review_grade_list = []

global reviewText_list
reviewText_list = []


# webdriver 사용
browser = webdriver.Chrome("./chromedriver.exe")

# 내용확인 유무 함수
def check(address, browser):

    try:
        time.sleep(random.uniform(1, 3))
        check_pro = browser.find_element_by_css_selector(address)
        time.sleep(random.uniform(1, 4))
    except:
        return "None"

    else:
        if check_pro.text == "":
            return "0"
        else:
            return check_pro.text

# 이미지 존재여부 판단 함수
def image_check(address, browser):

    try:
        browser.find_element_by_css_selector(address)
        time.sleep(2)
    except:
        return "0"

    else:
        return "1"

# 아이스팩
browser.get("https://front.wemakeprice.com/deal/600078643")

# 구매후기 페이지 클릭
time.sleep(1)
browser.find_element_by_css_selector("div.wrap_tab li:nth-child(2)").click()

# 필터버튼 클릭
time.sleep(3)
browser.find_element_by_css_selector(".review_filter_txt").click()

# 별점 선택
time.sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[3]/div/div/div[3]/div[1]/div[2]/div/div/div[1]/div/button[5]").click()

# 적용버튼 클릭
time.sleep(1)
browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[3]/div/div/div[3]/div[1]/div[2]/div/div/div[2]/a[2]/span").click()


# 상품페이지 넘기기
for p in range(1,11):
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[3]/div/div/div[3]/div[3]/a["+ str(p) +"]").click()

    time.sleep(1.5)

    for j in range(1,10):

        # 첫번째 데이터 프레임을 위한 리스트, 컬럼 선언
        df1_columns = ['사용자 ID', '랭킹', '총 도움이 돼요 수', '총 작성리뷰 수']

        # 리스트 초기화
        df1_list = []
        productName_list = []
        review_grade_list = []
        written_date_list = []
        image_list = []
        reviewText_list = []
        review_helpful_list = []

        # 페이지별 사용자 선택
        n = j
        time.sleep(2)
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[3]/div/div/div[3]/div[2]/ul/li["+str(n)+"]/div[1]/button[2]").click()

        # 사용자 이름
        time.sleep(1)
        reviewer_name = browser.find_element_by_css_selector(".title .name").text

        time.sleep(0.5)
        print("리뷰어 이름: ", reviewer_name)

        # 랭킹
        ranking = browser.find_element_by_css_selector("div.review_num dd:nth-child(2)").text

        time.sleep(1.5)
        print("랭킹: ", ranking)

        # 총 도움이 돼요 수
        total_helpful = browser.find_element_by_css_selector("div.review_num dd:nth-child(4)").text

        time.sleep(1)
        print("총 도움이 돼요 수: ", total_helpful)

        # 총 작성 리뷰 수
        # time.sleep(random.uniform(1, 10))
        total_written_reviews = browser.find_element_by_css_selector("div.review_num dd:nth-child(6)").text

        time.sleep(2)
        print("총 작성 리뷰 수: ", total_written_reviews)

        person_review_num = int(total_written_reviews) + 1

        # 리스트에 요소 추가
        df1_list.append(reviewer_name)
        df1_list.append(ranking)
        df1_list.append(total_helpful)
        df1_list.append(total_written_reviews)

        # df1 생성 (첫번째 데이터 프레임)
        df1 = pd.DataFrame([df1_list], columns=df1_columns)
        print(df1)

        for i in range(1, person_review_num):
            # 상품평 클릭
            time.sleep(2.4)
            per_review_tag = "div.thumbnail ul.thumb_list li:nth-child("+str(i)+")"
            browser.find_element_by_css_selector(per_review_tag).click()

            # 페이지 스크롤 다운
            body = browser.find_element_by_css_selector('.review_slt')
            for i in range(2):
                body.send_keys(Keys.PAGE_DOWN)
                time.sleep(2)

            # 리뷰 상품명
            time.sleep(1)
            review_product_name = browser.find_element_by_css_selector("div.review_slt div.review_wrap div.area_cont span.opt").text

            time.sleep(2)
            print("리뷰 상품명: ", review_product_name)

            # 이미지 여부
            time.sleep(0.5)
            image = image_check("div.review_slt .review_swp .wrap_banner ul li div", browser)

            print("이미지 여부(0/1) : ", image)

            # 리뷰 별점
            review_grade = browser.find_element_by_css_selector("div.review_slt .review_wrap .report .area_star.star strong").text

            time.sleep(1)
            print("리뷰 별점: ", review_grade)

            # 리뷰 작성날짜
            time.sleep(0.7)
            review_written_date = browser.find_element_by_css_selector("div.review_slt .review_wrap .report span.time").text

            time.sleep(0.5)
            print("리뷰 작성날짜: ", review_written_date)

            # 리뷰 내용
            time.sleep(2)
            # review_text = browser.find_element_by_css_selector("div.review_slt .review_wrap .area_cont p").text
            review_text = check("div.review_slt .review_wrap .area_cont p", browser)

            time.sleep(1)
            print("리뷰 내용: ", review_text)

            review_helpful = check("div.review_slt div.review_wrap div.area_like span strong", browser)
            print("도움이 돼요 : ", review_helpful)

            # 리스트에 요소 추가
            productName_list.append(review_product_name)
            review_grade_list.append(review_grade)
            written_date_list.append(review_written_date)
            image_list.append(image)
            reviewText_list.append(review_text)
            review_helpful_list.append(review_helpful)

        # 사용자 페이지 x 버튼 클릭
        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[5]/div/div[1]/a").click()


        # df2 생성 (두번쨰 데이터 프레임)
        df2 = pd.DataFrame({'리뷰 상품명': productName_list, "리뷰평점": review_grade_list, "작성날짜": written_date_list,
                            "이미지 여부(0/1)": image_list, "리뷰 내용": reviewText_list, "도움이 돼요": review_helpful_list})
        print(df2)

        # df1,df2 합치기
        result1 = pd.concat([df1,df2], axis=1)
        print(result1)

        # 파일명
        name = reviewer_name.replace('*', '')

        # 데이터프레임 엑셀 저장
        result1.to_excel(excel_writer='C:\\Users\\mingyeongkim\\Desktop\\데이터\\{0}_customer_data_1_{1}_{2}.xlsx'.format(name, p, n))
        time.sleep(1.5)
