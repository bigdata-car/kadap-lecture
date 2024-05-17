from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse, Response
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from starlette import status
# Bearer token을 사용하기 위한 라이브러리
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Depends, HTTPException

# cloud ide는 리버스 프록시를 사용하기 때문에 prefix 별도 지정
app = FastAPI(openapi_prefix="/proxy/8000")
# 일반적인 경우 아래와 같이 사용
# app = FastAPI()

# 인증을 위한 토큰 리스트
tokenList = [
    "thisisasampletokenfor23rdMay"
]

get_bearer_token = HTTPBearer(auto_error=False)
ERROR = "Bearer token missing or unknown"

# 토큰을 입력받고, 해당 토큰이 인증을 위한 토큰 리스트에 있는지 여부 판단하여 인증 진행
async def get_token(
    auth: Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token),
) -> str :
    if auth is None or (token := auth.credentials) not in tokenList :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=ERROR
        )

    return token

# 기본적인 GET 방식 API에 인증을 위한 토큰 적용
@app.get('/api/v1/tutorial/get')
async def hello(token: str = Depends(get_token)) :
    if token in tokenList :
        return JSONResponse({
            'success': 'True',
            'data': {
                'msg': 'Hello world'
            }
        })
    else :
        raise ERROR

class Item(BaseModel) :
    user: str
    msg: str

@app.post('/api/v1/tutorial/post')
async def mypost(item: Item) :
    return JSONResponse({
        'success': 'True',
        'data': {
            'user': item.user,
            'msg': item.msg
        }
    })

@app.put('/api/v1/tutorial/put')
async def myput(item: Item) :
    return JSONResponse({
        'success': 'True',
        'data': {
            'user': item.user,
            'msg': item.msg
        }
    })

@app.delete('/api/v1/tutorial/delete')
async def mydelete() :
    return Response(status_code=204)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
