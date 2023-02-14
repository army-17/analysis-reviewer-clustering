# ------------------- 코드 파일 설명 -------------------#
'''
- 모든 입력변수 한 파일로 합치기 위한 코드 (두 개의 데이터 프레임 합치기)
    -> customer_data2_x_variables_df1(325).xlsx (1~22번 입력변수 엑셀파일, 데이터 프레임1)
    -> customer_data2_pos_neg_ratio_results(325).xlsx (23~28번 입력변수 엑셀파일, 데이터 프레임2)
    -> get_x_variable_Discord(325).xlsx (29번 입력변수 엑셀파일, 데이터 프레임3)

- 키 값 기준으로 합침!

- final_x_variables_results2_(325).xlsx 최종 입력변수 파일!
'''

import pandas as pd
import os
import openpyxl
from openpyxl import load_workbook


# ------------------- main -------------------#

x_vars_df_1 = pd.read_excel('customer_data_x_variables_df1(1250).xlsx')
print(x_vars_df_1)

x_vars_df_2 = pd.read_excel('customer_data_pos_neg_ratio_results(1250).xlsx')
print(x_vars_df_2)

x_vars_df_3 = pd.read_excel('get_x_variable_Discord(1250).xlsx')
print(x_vars_df_3)

final_results_1 = pd.merge(x_vars_df_1, x_vars_df_2, left_on='2. 리뷰어 키(넘버)', right_on='Customer_key', how='left',
                           left_index=False, right_index=False)
print(final_results_1)


final_results_2 = pd.merge(final_results_1, x_vars_df_3, left_on='2. 리뷰어 키(넘버)', right_on='2. 리뷰어 키(넘버)', how='left',
                           left_index=False, right_index=False)
print(final_results_2)

final_results = final_results_2.sort_values("2. 리뷰어 키(넘버)")

final_results.to_excel(excel_writer='final_x_variables_results_(1250).xlsx')
