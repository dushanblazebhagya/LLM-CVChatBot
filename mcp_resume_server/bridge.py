from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from server import query_resume_tool, send_email_tool

app = FastAPI()

# Enable CORS for frontend on localhost and remote IP
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # can be restricted to your domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Resume query endpoint
@app.post("/query_resume")
async def query_resume_endpoint(payload: dict):
    question = payload.get("question", "")
    loop = asyncio.get_event_loop()
    try:
        answer = await loop.run_in_executor(None, lambda: query_resume_tool(question))
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}

# Send email endpoint
@app.post("/send_email")
async def send_email_endpoint(payload: dict):
    recipient = payload.get("recipient", "")
    subject = payload.get("subject", "")
    body = payload.get("body", "")
    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(None, lambda: send_email_tool(recipient, subject, body))
        return result
    except Exception as e:
        return {"error": str(e)}
