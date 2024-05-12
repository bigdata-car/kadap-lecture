# 가상 머신에 설치 하여 사용하기 

```bash
$ curl -fsSL get.docker.com -o get-docker.sh #도커 설치 스크립트 다운로드 
$ sh get-docker.sh #스크립트 실행 하여 설치 하기 
$ docker –v  #설치 여부 확인 하기 
```

# 컨테이너 관리SW Portainer 설치 하기 (옵션) 
```bash
$ mkdir -p /data/portainer #작업 폴더 생성하기
$ sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v /data/portainer:/data portainer/portainer-ce:latest #도커로 설치 하기 
```

> https://[IP]:9443 로 접속 하기 (포트포워딩 설정 필요, 211.199.20.7)
