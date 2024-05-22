```bash
# 1. Ubuntu 20.04 다운로드 받기 
$ docker pull ubuntu:20.04  

#2. 다운 받은 도커 이미지 확인 하기 
$ docker images 

#3. Ubuntu 20.04 설치 하기 
$ docker run -d -it --network=host –-name os ubuntu 

#4. 생성 되어 있는 컨테이너 확인 하기 
$ docker ps –a  

#5. Ubuntu 20.04 컨테이너에 접속하기 
$ docker exec -it os /bin/bash 

#6. 개발한 알고리즘을 도커에서 서비스 하기
$ pwd #현재 작업 폴더 확인
 
$ apt update
$ apt install python3-pip wget; rm /usr/lib/python3.12/EXTERNALLY-MANAGED   #에러 처리용

$ wget https://raw.githubusercontent.com/bigdata-car/kadap-lecture/main/20240522-katech-python-with-kadap-cloud/Day02-Class02/streamlit-final.py
$ wget https://raw.githubusercontent.com/bigdata-car/kadap-lecture/main/20240522-katech-python-with-kadap-cloud/Day02-Class02/kadap.png 

#필요 패키지 설치 하기  
$ pip install streamlit
$ /usr/local/bin/streamlit run ./streamlit-final.py --server.port 30002 #코드 실행 하기 

```
