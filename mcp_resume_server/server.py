import json
import asyncio
import os
from email.message import EmailMessage
from aiosmtplib import send
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import openai

load_dotenv()

with open("resume.json", "r", encoding="utf-8") as f:
    resume = json.load(f)

openai.api_key = os.getenv("OPENAI_API_KEY")

mcp = FastMCP("resume-server")


def query_resume_tool(question: str) -> str:
    """
    Sends resume JSON + user question to OpenAI GPT.
    Handles greetings and arbitrary input.
    """
    try:
        system_prompt = (
            "You are a helpful assistant that answers questions about a resume. "
            "If the user says something unrelated (like 'Hi' or 'Hello'), "
            "greet politely and suggest they ask about the resume. "
            "Only use information from the resume JSON provided."
        )

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Resume JSON: {json.dumps(resume)}\nQuestion: {question}"}
            ],
            temperature=0
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"LLM Error: {e}"


async def send_email_async(recipient: str, subject: str, body: str) -> str:
    msg = EmailMessage()
    msg["From"] = os.getenv("EMAIL_ADDRESS")
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)
    try:
        await send(
            msg,
            hostname="smtp.gmail.com",
            port=587,
            start_tls=True,
            username=os.getenv("EMAIL_ADDRESS"),
            password=os.getenv("EMAIL_PASSWORD")
        )
        return f"Email successfully sent to {recipient}!"
    except Exception as e:
        return f"Failed to send email: {e}"

def send_email_tool(recipient: str, subject: str, body: str) -> dict:
    """
    Returns a dict for MCP reasoning.
    """
    result = asyncio.run(send_email_async(recipient, subject, body))
    return {"status": result}

mcp.tool()(query_resume_tool)
mcp.tool()(send_email_tool)

if __name__ == "__main__":
    mcp.run()
