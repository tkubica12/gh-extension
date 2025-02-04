from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import os

app = FastAPI(title="GitHub demo extension", description="This is example GitHub extension code")

@app.get("/", include_in_schema=False)
def get_openapi_spec():
    return app.openapi()

@app.post("/")
async def handle_post(request: Request):
    # Print the request body
    print(await request.body())

    def generate():
        yield "hello, I am here"

    return StreamingResponse(generate(), media_type="text/plain")