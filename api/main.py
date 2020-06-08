from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from api.errors import ApiError, InvalidFizzBuzzInput, WrongFizzBuzzAnswer, DontSetDummyParameter, error_response
from api.fizzbuzz import fizzbuzz

app = FastAPI()


class FizzBuzzRequest(BaseModel):
    input: int  # fizzbuzz の入力
    answer: str  # fizzbuzz の結果
    dummy: Optional[str]  # 値をいれたらエラー


class FizzBuzzResponse(BaseModel):
    passed: bool = True
    message: str = ''


@app.exception_handler(ApiError)
async def api_error_handler(request, err: ApiError):
    raise HTTPException(status_code=err.status_code, detail=f'{err.detail}\n{err.reason}')


@app.post("/check_fizzbuzz", response_model=FizzBuzzRequest,
          responses=error_response([DontSetDummyParameter, InvalidFizzBuzzInput, WrongFizzBuzzAnswer]))
def check_fizzbuzz(req: FizzBuzzRequest):
    if req.dummy:
        # 実際は validator でやると綺麗
        raise DontSetDummyParameter()
    try:
        expected = fizzbuzz(req.input)
    except ValueError:
        # 実際は validator でやると綺麗
        raise InvalidFizzBuzzInput(reason=f'{req.input} is invalid range.')
    if expected != req.answer:
        raise WrongFizzBuzzAnswer(reason=f'`{req.answer}` is wrong. Expected: `{expected}`')
    return FizzBuzzResponse(message='Good!')
