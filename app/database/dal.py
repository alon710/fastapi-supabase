from pydantic import UUID4, BaseModel

from app.database.db import Database


class DataAccessLayer:
    def __init__(self, db: Database):
        self.db = db.SessionLocal()

    def get_one(self, model: BaseModel, id: int):
        return self.db.query(model).filter(model.id == id).first()

    def get_many(self, model: BaseModel, skip: int = 0, limit: int = 100):
        return self.db.query(model).offset(skip).limit(limit).all()

    def create(self, model: BaseModel, schema: BaseModel):
        db_model = model(**schema.dict())
        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)
        return db_model

    def update(self, model: BaseModel, id: UUID4, schema: BaseModel):
        db_model = self.get_one(model, id)
        for key, value in schema.dict().items():
            setattr(db_model, key, value)
        self.db.commit()
        self.db.refresh(db_model)
        return db_model

    def delete(self, model: BaseModel, id: UUID4):
        db_model = self.get_one(model, id)
        self.db.delete(db_model)
        self.db.commit()
        return db_model
