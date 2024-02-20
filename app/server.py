import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.database.dal import DataAccessLayer
from app.database.db import Database
from app.routes import user

load_dotenv()

app = FastAPI(
    title="FastAPI Demo",
    description="A simple demo of a FastAPI & Supabase application",
    version="0.1",
    debug=True if os.getenv("ENV") == "DEBUG" else False,
)


def get_connection():
    return DataAccessLayer(db=Database)


@app.on_event("startup")
async def startup():
    Database.Base.metadata.create_all(bind=Database.engine)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    app.include_router(user.router)

    uvicorn.run(
        app,
        port=8000 if os.getenv("ENV") == "DEBUG" else 80,
    )
