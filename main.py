from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import get_db, City
import os

app = FastAPI(title="Serbian Cities Explorer", description="Explore beautiful cities of Serbia")

templates = Jinja2Templates(directory="templates")

os.makedirs("templates", exist_ok=True)
os.makedirs("static/images", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def cities(request: Request, db: Session = Depends(get_db)):
    query = select(City)
    cities = db.execute(query).scalars().all()
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "cities": cities}
    )

@app.get("/{city_name}")
async def city_detail(request: Request, city_name: str, db: Session = Depends(get_db)):
    query = select(City).where(City.name == city_name)
    city = db.execute(query).scalar_one_or_none()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    
    return templates.TemplateResponse(
        "city_detail.html", 
        {"request": request, "city": city}
    )

@app.get("/api/cities")
async def get_cities(db: Session = Depends(get_db)):
    query = select(City)
    cities = db.execute(query).scalars().all()
    return cities

@app.get("/api/cities/{city_name}")
async def get_city(city_name: str, db: Session = Depends(get_db)):
    query = select(City).where(City.name == city_name)
    city = db.execute(query).scalar_one_or_none()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city
