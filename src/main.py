from fastapi import FastAPI, Depends, HTTPException
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "welcome to VR dart backend"}

@app.post("/players/", response_model = schemas.PlayerCreate)
async def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db)):
    data = jsonable_encoder(crud.create_player(player = player, db = db))
    return JSONResponse(data)



@app.put("/players/", response_model = schemas.Player)
async def edit_player(player: schemas.Player, db: Session = Depends(get_db)):
    data = jsonable_encoder(crud.update_player(player = player, db = db))
    return JSONResponse(data)

@app.get("/players/")
async def read_all_player(db: Session = Depends(get_db)):
    return crud.get_all_player(db=db)

@app.get("/players/{player_id}")
async def read_player(player_id, db: Session = Depends(get_db)):
    return crud.get_player(db=db, player_id = player_id)
