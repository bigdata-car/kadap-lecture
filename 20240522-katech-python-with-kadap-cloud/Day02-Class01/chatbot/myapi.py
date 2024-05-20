from fastapi import FastAPI, APIRouter
from starlette.responses import JSONResponse, Response
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from marketapi import Mychatbot

app = FastAPI(openapi_prefix="/proxy/8000")
# mychatbot = Mychatbot(apikey="ae344476-9b50-436b-83a1-22c9c9c089be")

class Item(BaseModel) :
    apikey: str
    user_id: str
    prompt: str

@app.post('/api/v1/chatbot')
async def carinfo(item: Item) :
    mychatbot = Mychatbot(apikey=item.apikey)
    result = mychatbot.chatbot(user_id=item.user_id, prompt=item.prompt)

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