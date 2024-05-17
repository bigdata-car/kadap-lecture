# 1. 연비예측모델
## 연비예측모델 API로 만들기

* Day01-Class01에서 진행한 **[머신러닝을 이용한 선형회귀 모델 구현 실습](https://github.com/bigdata-car/kadap-lecture/tree/main/20240522-katech-python-with-kadap-cloud/Day01-Class01)** 코드를 이용하여 API를 만든다.
* 알고리즘의 입력과 출력이 무엇인지 파악하고, 각각을 API의 request와 response로 구현한다.
<br/>

## 연비예측모델 분석 : API를 GET 방식으로 구현 및 호출해보기

![image](https://github.com/bigdata-car/kadap-lecture/assets/105857557/dd233db8-6fce-443d-9157-221a87998189)

1. 모델 입력/출력 데이터
  * 입력 : 차량 가속도(Vehicle acceleration), 차량 현재속도(Vehicle speed), 엔진 RPM(Engine RPM)
  * 출력 : 리터당 예상 이동 가능 거리(KmPL)

2. (서버) API 구현 - GET 방식
```python
app = FastAPI()

@app.get('/api/v1/automotive_regression')
async def GET(acceleration, velocity, rpm) :
  # model: 연비예측모델
  result = model(acceleration, velocity, rpm)
  return JSONResponse({
    'result': result
  })
```

3. (클라이언트) API 호출 - GET 방식
```python
import requests
import json

url = "www.example.com/api/v1/automotive_regression"
params = {
  "acceleration": 0.082192,
  "velocity": 45,
  "rpm": 2111
}

res = requests.get(url=url, params=params)
```
<br/>

## 연비예측모델 분석 : API를 POST 방식으로 구현 및 호출해보기

1. 모델 입력/출력 데이터 : GET 방식과 동일
2. (서버) API 구현 - POST 방식
