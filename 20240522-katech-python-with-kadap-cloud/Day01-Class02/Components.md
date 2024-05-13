# 1. Write and Magic

- Write arguments to the app
- Multiple arguments를 지원하기 때문에 다양한 표현 가능

## 1.1 write(string)

```python
import streamlit as st

st.write("Hello. *World!* : sunglasses:')
```
![image](https://github.com/bigdata-car/kadap-lecture/assets/105857557/aefc4194-2169-42f3-b510-b74c56e5f57b)

## 1.2 write_stream(string)

```python
import streamlit as st

string = "KADaP Cloud는 자동차 데이터 분석과 기술 개발에 필요한 IT 인프라를 가상화 기술을 활용하여 대여해 주는 서비스입니다. 사용자는 원하는 사양의 서버를 직접 생성하거나 제공되는 시뮬레이션, 분석, 개발 환경에 접속하여 바로 사용할 수 있습니다."

def stream_data():
    for word in string.split(" "):
        yield word + " "
        time.sleep(0.1)

st.write_stream(stream_data)
```
[https://katech2021-my.sharepoint.com/:v:/g/personal/mjbang_bigdata-car_kr/EZOaKEpOlShOhlqYLTdouUABSsC9IhBqyDlxPQkgErQdpA?e=2wxfof
](https://private-user-images.githubusercontent.com/153149491/330029935-c2e4d9f1-cb89-438e-8661-7678b4aebed2.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTU1OTg2NTAsIm5iZiI6MTcxNTU5ODM1MCwicGF0aCI6Ii8xNTMxNDk0OTEvMzMwMDI5OTM1LWMyZTRkOWYxLWNiODktNDM4ZS04NjYxLTc2NzhiNGFlYmVkMi5naWY_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNTEzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDUxM1QxMTA1NTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01OWEwNmMxYTRlOThlYmU1ZTAwMTgwM2JjMjBlN2YyMzQyMzJlMzVkM2UwZmMwOWFjMThmYTdmZmQxODUwYzQ2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.CevkQxCjh-znlVKY1hpnAMivnCGL-aiZYV0RFzMmrVo)
# 2. Text elements

## 2.1 Markdown
## 2.2 Title
## 2.3 Header
## 2.4 Caption
## 2.5 Code block

# 3. Data elements

## 3.1 Dataframes
## 3.2 Metrics
## 3.3 Static tables

# 4. Chart elements

## 4.1 Simple area charts
## 4.2 Simple line charts
## 4.3 Matplotlib

# 5. Input widgets

## 5.1 Button
## 5.2 Download button
## 5.3 Form button
## 5.4 Slider
## 5.5 File uploader
