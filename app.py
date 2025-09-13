from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from schemas import ProblemRequest, ProblemResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from services.problem_analyzer import analyze_problem

app = FastAPI(title="AnalyzeQuestion Backend")

templates = Jinja2Templates(directory="templates")

# Optional: Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze", response_model=ProblemResponse)
async def analyze(problem: ProblemRequest):
    return analyze_problem(problem.text)
