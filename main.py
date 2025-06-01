from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routes import upload, generate_code, run_code
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Root route to avoid 404 on "/"
@app.get("/")
async def root():
    return {"message": "Welcome to SifraAI Backend!"}

# Serve static files (put your favicon.ico inside ./static folder)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Favicon route to avoid 404 on "/favicon.ico"
@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")

# Include routers
app.include_router(upload.router)
app.include_router(generate_code.router)
app.include_router(run_code.router)
