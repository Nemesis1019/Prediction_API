from fastapi import FastAPI

from app.routes.main import api_router

app = FastAPI(
    title='Prediction API',
    summary="API que retorne la predicción de un modelo de machine learning basado en las características de entrada.",
    version="0.0.1",
    contact={
        "name": "Carlos Arcos",
        "url": "https://github.com/Nemesis1019",
    }
)
app.include_router(api_router)


@app.get("/", tags=['Welcome'])
def welcome():
    return {"message": "Welcome to the Iris Classifier API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
