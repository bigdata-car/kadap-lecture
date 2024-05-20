from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse, Response
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from marketapi import Mycar

app = FastAPI(openapi_prefix="/proxy/8000")

@app.get('/api/v1/mycar/carinfo_get')
async def carinfo_get(apikey: str, ownername: str, reginumber: str) :
    mycar = Mycar(apikey=apikey)
    result = mycar.carinfo(ownername=ownername, reginumber=reginumber)


    return JSONResponse({
        'success': 'True',
        'data': {
            'result': result
        }
    })

@app.get('/api/v1/mycar/owner_verify_get')
async def carinfo_get(apikey: str, ownername: str, reginumber: str) :
    mycar = Mycar(apikey=apikey)
    result = mycar.reginumber(ownername=ownername, reginumber=reginumber)

    return JSONResponse({
        'success': 'True',
        'data': {
            'result': result
        }
    })

class Item(BaseModel) :
    apikey: str
    ownername: str
    reginumber: str

@app.post('/api/v1/mycar/carinfo_post')
async def carinfo(item: Item) :
    try :
        mycar = Mycar(apikey=item.apikey)
        print(item)

        result = mycar.carinfo(ownername=item.ownername, reginumber=item.reginumber)

        print(result)

        return JSONResponse({
            'success': 'True',
            'data': {
                'result': result
            }
        })
    except exception:
        return JSONResponse({
            'success': 'False',
            'data': {
                'result': exception.idError
            }
        })


@app.post('/api/v1/mycar/owner_verify_post')
async def carinfo(item: Item) :
    mycar = Mycar(apikey=item.apikey)
    result = mycar.owner_verify(ownername=item.ownername, reginumber=item.reginumber)

    return JSONResponse({
        'success': 'True',
        'data': {
            'result': result
        }
    })

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
