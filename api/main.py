from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from receiver import session
from models import ProductDB, ProductAPI

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products/{product_id}")
def get_product_by_id_(product_id: int):
    item = session.query(ProductDB).filter(ProductDB.id == product_id).first()
    print(item)

@app.get("/products/")
def get_all_products_():
    items = session.query(ProductDB).all()
    print(items)

@app.post("/products/new/")
async def post_product_(data: ProductAPI):
    # img_data = await img.read()

    item = ProductDB(name=data.name, 
                   description=data.description, 
                   price=data.price)
    session.add(item)
    session.commit()
    session.refresh(item)
    return {"status": "ok", "data": item}