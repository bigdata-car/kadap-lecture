# 가상머신(VM)에서 연비 예측 Streamlit 서비스 하기

```bash
$ (ubuntu) su root #사용자 변경(비밀번호 kadap1234), ubuntu는 관리용 입니다.  
$ sudo apt update; sudo apt install python3-pip wget #python 및 python 패키지 설치 툴(pip) 설치, 최초 설치시 시간 소요 
#이전 시간에 작성한 streamlit 코드 및 로고 이미지 다운로드  (패키지 설치 시간 단축을 위해 머신러닝 부분은 제거 하였습니다.)
$ wget https://raw.githubusercontent.com/bigdata-car/kadap-lecture/main/20240522-katech-python-with-kadap-cloud/Day02-Class02/streamlit-final.py $ wget https://raw.githubusercontent.com/bigdata-car/kadap-lecture/main/20240522-katech-python-with-kadap-cloud/Day02-Class02/kadap.png 
$ pip install streamlit#필요 패키지 설치 하기 
$ streamlit run streamlit-final.py --server.port 30001 #코드 실행 하기 
```
> 접속하기 위해서는 포트 포워딩을 해주어야 합니다. 
