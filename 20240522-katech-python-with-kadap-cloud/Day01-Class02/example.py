import streamlit as st

## 1. 웹페이지 타이틀 작성
## st.title(string)
## 예시:
st.title("OBD 데이터 시각화 및 머신러닝 활용")

## 2. 웹페이지 텍스트 작성
## st.write(string)
## 예시: 
st.write("OBD 데이터란? \n 자동차의 전기/전자적인 작동 상태를 확인할 수 있는 데이터를 의미한다.")

## 3. 이미지 삽입하기
## st.image(image="path")
## 예시: 
st.image(image="kadap.png")

## 4. 선택박스 삽입
## st.selectbox(label, list)
## 예시: 
st.selectbox("업로드 파일 포맷을 선택하세요.", ["Image","CSV"])

## 5. 파일 업로드 위젯
# st.file_uploader(label, type, accept_multiple_files)
## 예시_1: 
st.file_uploader("업로드 파일을 선택해주세요.", type=['png', 'jpg', 'jpeg'], accept_multiple_files=False)
## 예시_2: 
# st.file_uploader("업로드 파일을 선택해주세요.", type=['txt', 'csv'], accept_multiple_files=False)
## 예시_3: 
# st.file_uploader("업로드 파일을 선택해주세요.", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

## 6. 성공 메세지 
# st.success(body)
# body: 성공 메세지
# 예시
st.success("파일 업로드 성공")

## 7. form 
# st.form(key, clear_on_submit=False, border=True)
# key: 해당 form의 label로 각 form은 하나의 key를 갖는다.
# clear_on_submit: True일 경우, Submit 버튼 클릭 시, 
# form안에 모든 위젯 값이 default 값으로 reset 된다.
# border: form의 경계선
# 예시
with st.form(key="example"):
    menu   = st.selectbox("메뉴를 선택하세요", ["돈까스", "제육볶음", "짜장면", "삼겹살"])
    button = st.form_submit_button()
    if button:
        st.write(f"오늘 저녁메뉴는 {menu}입니다.")

## 8. 로딩spinner
import time 
# time 라이브러리의 sleep함수를 사용하면 일정시간 프로세스를 정지할 수 있다.

# st.spinner(text)
# 예시:
with st.spinner(text="로딩중"):
    time.sleep(3)
st.success("로딩 완료!")

## 9. matplotlib 삽입
import matplotlib.pyplot as plt
import numpy as np
# st.pyplot(fig=None, clear_figure=None, use_container_width=True)

# 예시:
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

## 10. slider
# st.slider(label, min_value=None, max_value=None, value=None)
# 예시
age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")