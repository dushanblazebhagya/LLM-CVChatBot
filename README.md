MCP CV Chat & Email

A Model Context Protocol (MCP) server with a React/Next.js frontend that lets users:

Ask questions about a resume (CV) with answers powered by an LLM (OpenAI GPT).

Send emails directly via Gmail securely with an app password.

Features: Resume querying, email sending via SMTP, and a minimal frontend interface.

Backend: FastAPI + MCP tools
Frontend: React/Next.js for interactive UI

Requirements: Python 3.10+, Node.js 18+

Run Backend:
pip install -r requirements.txt
uvicorn bridge:app --reload --host 0.0.0.0 --port 8001

Run Frontend:
npm install
npm run dev

Open http://localhost:3000 in your browser.