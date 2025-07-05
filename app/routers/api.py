from fastapi import APIRouter, Request

router = APIRouter()

sample_data_store = [
    {"id": 1, "name": "Sample Data 1"},
]

@router.post("/data")
async def create_data(request: Request):
    payload = await request.json()
    sample_data_store.append(payload)
    return {"message": "Data received", "data": payload}

@router.get("/data")
def read_data():
    return {"data": sample_data_store}
