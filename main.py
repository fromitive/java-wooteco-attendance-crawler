
from fastapi.staticfiles import StaticFiles
from auth.credential import Credential
from api.spreedsheet import SpreedSheet
from repository.crew_repository import CrewRepository
from datetime import datetime
from typing import List
from fastapi import FastAPI

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

def crawl():
    today = datetime.now().date()
    values = SpreedSheet.get_values(Credential.get_credential())
    crews = CrewRepository.find_all()
    for value in values:
      if value.isattended(today):
         if value.name in crews:
            crews.remove(value.name)

    return crews



@app.get("/crews", response_model=List[str])
async def get_crews():
    return crawl()

