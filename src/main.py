from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import json

app = FastAPI(title="GitHub demo extension", description="This is example GitHub extension code")

@app.get("/", include_in_schema=False)
def get_openapi_spec():
    return app.openapi()

@app.post("/")
async def handle_post(request: Request):
    body = await request.body()
    body_json = json.loads(body.decode('utf-8'))
    print(body_json)

    def generate():
        message_content = f"""
        Hello! This is message from Tomas Kubica AI agent.

        Here is context I have received from Copilot platform:

        {json.dumps(body_json, indent=4)}

        Let's do something
        """
        data = {
            "choices": [
                {
                    "index": 0,
                    "delta": {"content": message_content, "role": "assistant"},
                },
            ],
        }
        yield f"data: {json.dumps(data)}\n\n"
        # yield "hello, I am here"

    return StreamingResponse(generate(), media_type="text/plain")