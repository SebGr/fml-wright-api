from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return "Healthy"
