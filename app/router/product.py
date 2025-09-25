from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from schemas.product import ProductCreate, ProductUpdate, ProductPatch, ProductOut, BaseResponse
from crud import product as crud
from schemas.user import UserOut
from api.deps import get_db, get_current_user

router = APIRouter()

# List all products
@router.get("/", response_model=List[ProductOut])
def list_products(current_user: UserOut = Depends(get_current_user), db: Session = Depends(get_db)):
    return crud.get_products(db)

# Get specific product
@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    return crud.get_product(db, product_id)

# Create Products
@router.post("/", response_model=BaseResponse[ProductOut])
def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    created_product = crud.create_product(db, product)
    return BaseResponse(message="Product Created Successfully", data=created_product)

# Update specific product
@router.put("/{product_id}", response_model=BaseResponse[ProductOut])
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    db_product = crud.update_product(db, product_id, product)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product Didn't Found")
    return BaseResponse(message="Product Updated ✅", data=db_product)

# Update Patch Specific product 
@router.patch("/{product_id}", response_model=BaseResponse[ProductOut])
def update_patch_product(product_id: int, product: ProductPatch, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    db_product = crud.patch_product(db, product_id, product)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product Didn't Found")
    return BaseResponse(message="Product Patched ✅", data=db_product)   

# Delete Specific product
@router.delete("/{product_id}", response_model=BaseResponse[ProductOut])
def remove_product(product_id: int, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    db_product = crud.delete_product(db, product_id)
    if not db_product: 
        raise HTTPException(status_code=404, detail="Product Didn't Found")
    return BaseResponse(message="Product Has Removed 🗑️", data=db_product)
