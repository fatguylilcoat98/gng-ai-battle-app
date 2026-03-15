from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import random

app = FastAPI(title="The Good Neighbor Guard")

templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

MISSIONS = [
"Tell someone you appreciate them today.",
"Send a message to someone you haven't talked to in a while.",
"Help someone solve a small problem.",
"Leave a positive comment on someone's post.",
"Thank someone who usually goes unnoticed.",
"Share a skill you know with someone.",
"Do something kind for a neighbor.",
"Encourage someone who seems discouraged.",
"Take five minutes to make someone smile.",
"Remind someone that they're doing a good job."
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/mission")
async def get_mission():
    mission = random.choice(MISSIONS)
    return {"mission": mission}
