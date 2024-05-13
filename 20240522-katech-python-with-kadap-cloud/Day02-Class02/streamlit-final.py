import os
import streamlit as st

# 1. 웹페이지 Title 및 설명 작성하기
st.title("OBD 데이터 시각화 및 머신러닝 활용")
st.write("OBD 데이터란? \n\n On-board diafnostics의 약자로 \"차량에 내장된 진단기\"로 알려져있다. \n차량 스스로 주행 문제를 유발할 수 있는 부분에 대해 운전자에게 경고하여 점검 및 정비를 받을 수 있도록 하는 시스템이다.")
st.image(image="kadap.png")

# 2. 파일 업로드 위젯 
menu = ['Image', 'CSV']
choice = st.selectbox('업로드 파일 포맷을 선택하세요.', menu)
if choice == 'Image':
    uploaded_file = st.file_uploader("Image파일을 선택해주세요.", type=['png', 'jpg', 'jpeg'], accept_multiple_files=False)
else:
    uploaded_file = st.file_uploader("CSV파일을 선택해주세요.", type=['csv'], accept_multiple_files=False)
