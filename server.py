from distutils.log import debug
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database
import uvicorn

app=FastAPI()

# 让app可以跨域
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/api/hello')
def get_root():
    return {'hello':"world"}

@app.get('/api/queryAll')
def query_all():
    return database.query_data()

if __name__=="__main__":
    uvicorn.run(app=app,debug=True,reload=True, host="127.0.0.1", log_level="info")