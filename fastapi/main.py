from fastapi import FastAPI, Depends, Path
from db import schema, models
from db.db_config import Base, engine, get_db
from sqlalchemy.orm import Session


# initialize the application and modify default api details
app = FastAPI(
    title="Todo - FastAPI",
    description="Todo api for managing scheduled task",
    version="0.0.1",
    openapi_url="/docs",
    contact={
        "name": "Peter Oyelegbin",
        "email": "peteroyelegbin@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)


# create the database if not exist
Base.metadata.create_all(engine)


# get all items
@app.get("/")
async def getItems(session: Session = Depends(get_db)):
    items = session.query(models.Item).all()
    if items == []:
        return "No data found"
    else:
        return items


# get one item by its id
@app.get("/{id}")
async def getItem(id:int = Path(..., description="task ID you want to retrieve", gt=0), session: Session = Depends(get_db)):
    item = session.query(models.Item).get(id)
    if item is None:
        return "No data found"
    else:
        return item


# add a new item
@app.post("/add")
async def addItem(item:schema.Item, session: Session = Depends(get_db)):
    item = models.Item(task=item.task, description=item.description, done=item.done)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


# update an existing item
@app.put("/edit/{id}")
async def updateItem(id:int, item:schema.Item, session: Session = Depends(get_db)):
    item_obj = session.query(models.Item).get(id)
    if item_obj is None:
        return "No data found"
    else:
        if item.task != None:
            item_obj.task = item.task
        if item.description != None:
            item_obj.description = item.description
        if item.done != None:
            item_obj.done = item.done
        session.commit()
        return item_obj


# delete an existing item
@app.delete("/delete/{id}")
async def deleteItem(id:int, session: Session = Depends(get_db)):
    item_obj = session.query(models.Item).get(id)
    if item_obj is None:
        return "No data found"
    else:
        session.delete(item_obj)
        session.commit()
        session.close()
        return "Item was deleted..."


# search for an item by its task
@app.get("/search/")
async def searchItem(task: str, session: Session = Depends(get_db)):
    items = session.query(models.Item).all()
    foundItem = []
    for item in items:
        if task in item.task:
            foundItem.append(item)
    return foundItem
