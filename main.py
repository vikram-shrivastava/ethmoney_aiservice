from fastapi import FastAPI 
from graph import NodeData
from fastapi.middleware.cors import CORSMiddleware
from schemas import mainRequest
import uvicorn
app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/reallocate")
def allocate(req:mainRequest):
    node_data=NodeData()
    base_apy_dict = req.base_apy.model_dump()
    response = node_data.allocate_funds(base_apy_dict)
    return response
    
@app.post("/generate_riskscore")
def generate_riskscore():
    return {"message":"Risk Score Generated"}


if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)