from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from prometheus_client import make_asgi_app, Counter

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")

metrics_app = make_asgi_app()
hello_counter = Counter("worlds_helloed", "Total number of worlds we have helloed")
app.mount("/metrics", metrics_app)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    hello_counter.inc()
    return templates.TemplateResponse(name="index.html", request=request)
