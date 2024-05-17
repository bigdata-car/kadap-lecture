# pip install --upgrade pip
# pip install --no-cache-dir -r ./requirements.txt

from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse, Response
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# cloud ide는 리버스 프록시를 사용하기 때문에 prefix 별도 지정
app = FastAPI(openapi_prefix="/proxy/8000")
# 일반적인 경우 아래와 같이 사용
# app = FastAPI()

# 기본적인 GET 방식 API
@app.get('/api/v1/tutorial/get')
async def hello() :
    return JSONResponse({
        'success': 'True',
        'data': {
            'msg': 'Hello world'
        }
    })

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
