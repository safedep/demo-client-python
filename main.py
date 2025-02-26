from fastapi import FastAPI
import uvicorn

from data_loader import fetch_data
from config_parser import load_config
from template_renderer import render_report

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the (Deliberately) Vulnerable App!"}

@app.get("/report")
def get_report():
    # Fetch some external data
    data = fetch_data()
    # Load configuration from a YAML source
    config = load_config()
    # Render a final textual "report" with Jinja2
    report = render_report(data, config)
    return {"report": report}

if __name__ == "__main__":
    # Start the server
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

