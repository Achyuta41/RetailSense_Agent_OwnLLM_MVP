from pydantic import BaseModel

class InventorySchema(BaseModel):
    store_id: int
    weeks: int = 3

class SalesSchema(BaseModel):
    store_id: int

class OfferSchema(BaseModel):
    store_id: int
