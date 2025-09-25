from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate, ProductUpdate, ProductPatch

def get_products(db: Session):
    return db.query(Product).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        name=product.name, 
        description=product.description,
        price=product.price,
        stock=product.stock
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = get_product(db, product_id)
    if db_product: 
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.stock = product.stock
        db.commit()
        db.refresh(db_product)
    return db_product

def patch_product(db: Session, product_id: int, product: ProductPatch):
    db_product = get_product(db, product_id)
    if db_product:
        if product.name is not None:
            db_product.name = product.name
        if product.description is not None:
            db_product.description = product.description
        if product.price is not None:
            db_product.price = product.price
        if product.stock is not None:
            db_product.stock = product.stock
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product





