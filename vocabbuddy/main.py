from fastapi import FastAPI

app = FastAPI(title="vocabbuddy")


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "ok", "app": "vocabbuddy"}
