# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model=joblib.load('linear_regression_model.pk')

# 2. 모델 설명
st.title('
st.subheader('
st.write('
st.write('
st.write('
st.write('
st.write('
st.write('
# 3. 데이터시각화
col1, col2, col3=st.columns(3)
with col1:
         st.subheader('데이터시각화1')
         st.image('시각화_1_스캐터_b (1).PNG')             
with col2:
         st.subheader('데이터시각화2')
         st.image('시각화_1_스캐터_b (2).PNG')             
with col3:
         st.subheader('데이터시각화3')
         st.image('시각화_1_스캐터_b.PNG')             

# 4. 모델 활용
st.subheader('모델활용')

a=st.number_input('범죄율 입력',value=0)
b=st.number_input('비소매상업지역 토지점유율 입력',value=0)
c=st.number_input('주택 1가구당 방 개수 입력',value=0)
d=st.number_input('1940이전 주택 소유 비율 입력',value=0)
e=st.number_input('보스턴 직업 센터 접근성 지수 입력',value=0)
f=st.number_input('10000$달러 당 재산세율 입력',value=0)
g=st.number_input('자치 시별 학생 교사 비율 입력',value=0)
h=st.number_input('지역 흑인 비율 입력',value=0)
i=st.number_input('모집단의 하위계층 비율 입력',value=0)

if st.button('예측하기'):
input_data=[[a,b,c,d,e,f,g,h,i]]
p=model.predict(input_data)
st.write('인공지능의 예측결과는',p,'$입니다.')
