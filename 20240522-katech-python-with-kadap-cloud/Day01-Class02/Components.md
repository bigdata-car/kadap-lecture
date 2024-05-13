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




