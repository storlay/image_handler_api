from fastapi import FastAPI

app = FastAPI(
    title='Image handler API',
    version='1.0.0',
    root_path='/api'
)
