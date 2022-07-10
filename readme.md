# Notas python

## Crear entorno 

```bash
python -m venv venv
. venv/Script/activate
pip install -r requirements.txt

# Previamente.
pip freeze > requirements.txt
```

## Ejemplo Base
main.py
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola nanos"}
```

## Arranca servidor
```bash
uvicorn main:app --host "0.0.0.0" --port 8000 --reload
```

## Prueba endpoints desde linea comandos
```bash
janrax@JANRAX-HOME MINGW64 ~/PycharmProjects/fastAPI (master)
$ http localhost:8000
HTTP/1.1 200 OK
content-length: 24
content-type: application/json
date: Sun, 10 Jul 2022 09:08:13 GMT
server: uvicorn

{
    "message": "Hola nanos"
}


$ http POST localhost:8000
HTTP/1.1 405 Method Not Allowed
allow: GET
content-length: 31
content-type: application/json
date: Sun, 10 Jul 2022 09:12:18 GMT
server: uvicorn

{
    "detail": "Method Not Allowed"
}

```

## Prueba endpoints desde navegador ( open api )

localhost:8000/docs