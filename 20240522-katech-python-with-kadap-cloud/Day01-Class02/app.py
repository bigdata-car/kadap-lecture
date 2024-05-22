import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


#### OBD 데이터를 활용한 연비 예측 Web Application 만들기 실습 ####

## 1. 웹페이지 Title 및 설명 작성하기
st.title("OBD 데이터 시각화 및 머신러닝 활용")
st.subheader("OBD 데이터란?")
st.write("On-board diafnostics의 약자로 \"차량에 내장된 진단기\"로 알려져있다. \n\n차량 스스로 주행 문제를 유발할 수 있는 부분에 대해 운전자에게 경고하여 점검 및 정비를 받을 수 있도록 하는 시스템이다.")
st.image(image="kadap.png")

## 2. 파일 업로드 위젯 
choice = st.selectbox('업로드 파일 포맷을 선택하세요.', ["Text", "CSV", "Image"])
if choice == 'Text':
    uploaded_file = st.file_uploader("Text 파일을 선택해주세요.", type=['txt'], accept_multiple_files=False)
elif choice == "CSV":
    uploaded_file = st.file_uploader("CSV 파일을 선택해주세요.", type=['csv'], accept_multiple_files=False)
elif choice == "Image":
    uploaded_file = st.file_uploader("IMG 파일을 선택해주세요.", type=['png, jpg, jpeg'], accept_multiple_files=False)

## 3. 업로드 파일 마이디스크 저장
#- 파일 중복 방지를 위해 업로드 파일마다 고유값 생성 및 전달
#- 생성된 고유값 활용을 통해 파일 이름 변경
#- 업로드 파일 저장

if uploaded_file is not None and choice == "Text":  # 파일 미없로드 시, uploaded_file == False
    current_time        = datetime.now()            # 파일 업로드 시간으로 고유값 설정
    filename            = current_time.isoformat().replace(':', "_").split('.')[0] + '.txt'
    uploaded_file.name  = filename                  # 업로드 파일 이름 재설정
    save_dir            = './uploaded_files'

    if not os.path.exists(save_dir):                # "save_dir" 디렉토리 파일 유무 확인
        os.makedirs(save_dir)                       # "save_dir" 디렉토리 생성
    
    with open(os.path.join(save_dir, uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())          # uploaded_file의 내용을 파일로 저장

    st.success("파일 저장 성공")

## 4. 데이터 시각화
st.header(" OBD데이터 시각화 ")
visual = False

if uploaded_file: 
    # (1) 업로드 데이터로부터 columns 리스트 추출하기 
    data_path = os.path.join('./uploaded_files', uploaded_file.name)
    data = pd.read_csv(data_path)
    columns = list(data.columns)

    # (2) 추출한 columns 리스트를 선택할 수 있는 select box 만들기
    with st.form(key="columns"):
        column = st.selectbox("시각화 대상 column을 선택하세요.", columns)
        vis    = st.selectbox("시각화 유형을 선택하세요.", ["violin_plot", "boxplot"])
        button = st.form_submit_button()

    # (3) 선택한 column의 데이터 분포 시각화
    if button:
        st.write("You selected: ", column)
        with st.spinner("시각화 생성 중"):
            fig, ax = plt.subplots()
            if vis == "violin_plot":
                ax = sns.violinplot(data=data[column]) 
            elif vis == "boxplot":
                ax = data.boxplot(column) 
            st.pyplot(fig, use_container_width=200)
        st.success('시각화 성공') 
    visual = True

st.divider()

# 5. 머신러닝 활용하기

#(3)-2 함수 생성 및 호출
def get_min_max(val):
    data_path = os.path.join('./uploaded_files', uploaded_file.name)
    data = pd.read_csv(data_path)
    min_v = data[val].min()
    max_v = data[val].max()
    return min_v, max_v

st.header(" 머신러닝 모델을 활용한 연비 예측 APP 구현 ")

if uploaded_file and visual:
    # (1) 머신러닝 모델-XGBRegression 모델 불러오기
    import xgboost as xgb
    import torch
    xgb_reg = xgb.XGBRegressor()

    # (2) 모델 학습 파일 load하기
    xgb_reg.load_model('./xgb_reg_model.json')

    # (3) 연비 예측을 위한 입력값 받기
    val = ["Vehicle acceleration (g)", "Vehicle speed (mph)", "Engine RPM (rpm)"]

    with st.form(key="predict"):
        min, max = get_min_max(val[0])
        accel = st.slider(val[0], min, max)

        min, max = get_min_max(val[1])
        speed = st.slider(val[1], min, max)

        min, max = get_min_max(val[2])
        rpm = st.slider(val[2], min, max)

        button = st.form_submit_button()

    # (4) 연비 예측 결과 출력하기
    if button:
        input_data = [[accel, speed, rpm]]      
        result = xgb_reg.predict(input_data)
        val    = result.item()
        st.subheader(f'연비 예측 결과: {val:.3f}Km/L')