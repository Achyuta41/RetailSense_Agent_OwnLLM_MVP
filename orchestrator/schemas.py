from pydantic import BaseModel

class InventoryRequest(BaseModel):
    store_id: int
    weeks: int = 3
