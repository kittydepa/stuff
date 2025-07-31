# Define a route
@app.post("/items", response_model=ForageItem, status_code=201)
def create_item(item: ForageItem):
    # Check for duplicates by ID
    if any(existing.id == item.id for existing in fake_db):
        raise HTTPException(status_code=400, detail="Item with this ID already exists.")

    # Add the item to the fake database
    fake_db.append(item)

    return item