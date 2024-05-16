from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse, Response
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from model import *

app = FastAPI(openapi_prefix="/proxy/8000")
mydistance = MyDistance()

@app.get("/api/v1/automotive_regression")
async def GET(acceleration: float, velocity: float, rpm: int) :
    result = mydistance.cal_distance(acc=acceleration, vel=velocity, rpm=rpm)

    return JSONResponse({
        'success': 'True',
        'data': {
            'msg': 'Success',   
            'result': result
        }
    })

class DISTANCE(BaseModel) :
    acceleration: float
    velocity: int
    rpm: int

@app.post('/api/v1/automotive_regression/post')
async def POST(param: DISTANCE) :
    result = mydistance.cal_distance(acc=param.acceleration, vel=param.velocity, rpm=param.rpm)

    return JSONResponse({
        'success': 'True',
        'data': {
            'msg': 'Success',
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
