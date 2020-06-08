# FastAPI Error Sample

[FastAPI](https://fastapi.tiangolo.com/) を使って、
アプリケーションで独自に作成したエラーも
OpenAPI の定義として管理できるようにしてみたサンプルです。

## 動かし方

python3.7で動作確認してます。


```sh
pip install -r requirements.txt

uvicorn api.main:app --reload
```

## OpenAPI

SwaggerEditor で見る
http://editor.swagger.io/?raw=https://raw.githubusercontent.com/pistatium/fastapi_error_sample/master/openapi.json
