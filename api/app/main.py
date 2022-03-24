from typing import Optional

import pandas as pd
from fastapi import FastAPI

from app.model import Model

app = FastAPI()
model = Model("xgboost", "Production")

@app.get("/")
def read_root():
    data = pd.read_csv('casas_X.csv')

    return { "model_name" : model.make_predictions(data) }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# @app.post("/predict")
# async def create_upload_file(file: UploadFile = File(...)):
#     if file.filename.endswith(".csv"):
#         with open(file.filename, "wb")as f:
#             f.write(file.file.read())
#         data = pd.read_csv(file.filename)
#         os.remove(file.filename)

#         return {
#             "Labels": model.predict(data)
#         }
#     else:
#         raise HTTPException(status_code=400, detail="Invalid file format. Only CSV Files accepted.")
