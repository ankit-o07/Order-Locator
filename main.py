from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
import requests
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URL"))
db = client["order_db"]
collection = db["orders"]

# Template setup
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")  # Store this in .env or your environment

@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit")
async def submit_order(
    request: Request,
    name: str = Form(...),
    phone: str = Form(...),
    address: str = Form(...),
    delivery_time: str = Form(...)
):
    # Save to MongoDB
    order = {"name": name, "phone": phone, "address": address, "delivery_time": delivery_time}
    collection.insert_one(order)
    
    # Redirect to map display
    return RedirectResponse(url=f"/map?address={address}", status_code=303)

@app.get("/map", response_class=HTMLResponse)
async def show_map(request: Request, address: str):
    return templates.TemplateResponse("map.html", {
        "request": request,
        "address": address,
        "google_maps_api_key": GOOGLE_MAPS_API_KEY
    })
