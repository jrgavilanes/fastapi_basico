import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def root():
    x = 2
    y = 2
    z = x + y
    return {"message": z}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
