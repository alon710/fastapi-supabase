import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

load_dotenv()

app = FastAPI(
    title="FastAPI Demo",
    description="A simple demo of a FastAPI & Supabase application",
    version="0.1",
    debug=True if os.getenv("ENV") == "DEBUG" else False,
)


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(
        app,
        port=8000 if os.getenv("ENV") == "DEBUG" else 80,
    )
