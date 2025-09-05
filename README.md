# MCP CV Chat & Email

A **Model Context Protocol (MCP) server** with a **React/Next.js frontend** that lets users:

- Ask questions about a resume (CV) with answers powered by an **LLM (OpenAI GPT)**.  
- Send emails directly via **Gmail** securely with an **app password**.  

---

## ✨ Features
- **Resume Querying:** Interact with your CV by asking natural language questions.  
- **Email Sending:** Compose and send emails via SMTP (Gmail).  
- **Frontend Interface:** Minimal and interactive UI built with React/Next.js.  

---

## 🛠 Tech Stack
- **Backend:** FastAPI + MCP tools  
- **Frontend:** React/Next.js  
- **Integration:** OpenAI GPT + Gmail SMTP  

---

## 📋 Requirements
- **Python:** 3.10+  
- **Node.js:** 18+  

---

## 🚀 Getting Started

### 1. Run Backend
pip install -r requirements.txt
uvicorn bridge:app --reload --host 0.0.0.0 --port 8001

### 2. Run Frontend
npm install
npm run dev

### 3. Browser
http://localhost:3000

