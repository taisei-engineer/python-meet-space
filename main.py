import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field

# 予約情報を管理するモデル
class Booking(BaseModel):
  booking_id: int
  user_id: int
  room_id: int
  booked_num: int
  start_datetime: datetime.datetime
  end_datetime: datetime.datetime

# ユーザー情報を管理するモデル
class User(BaseModel):
  user_id: int
  user_name: str = Field(max_length=12)

class Room(BaseModel):
  room_id: int
  room_name: str = Field(max_length=12)
  capacity: int

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Success"}

@app.post("/users")
async def user(users: User):
  return {"users": users}

@app.post("/rooms")
async def rooms(rooms: Room):
  return {"rooms": rooms}

@app.post("/bookings")
async def bookings(bookings: Booking):
  return {"bookings": bookings}

