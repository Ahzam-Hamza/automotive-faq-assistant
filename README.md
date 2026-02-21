# Automotive FAQ Assistant 🚗

An AI-powered Automotive FAQ Assistant designed to answer vehicle-related queries using car manual data and intelligent information retrieval.

This project demonstrates the practical implementation of Generative AI and Retrieval-Augmented Generation (RAG) to build a domain-specific assistant.

👤 Developer

Ahzam

Platform: Windows
Editor: VS Code

## Project Overview

The Automotive FAQ Assistant allows users to ask vehicle-related questions in natural language.  
The system retrieves relevant information from structured car manual data and generates clear, context-aware responses.

This project focuses on:
- Domain-specific AI assistant design
- Retrieval-based response generation
- Practical implementation of AI in real-world use cases

## How It Works

1. The user submits a vehicle-related question through the frontend interface.
2. The request is sent to the FastAPI backend via REST API.
3. The backend processes the query and retrieves relevant information from structured car manual data.
4. The retrieved context is used to generate a meaningful and domain-specific response.
5. The response is returned to the frontend and displayed to the user.

This architecture follows a Retrieval-Augmented Generation (RAG) approach to ensure relevant and context-aware answers.

## AI & Retrieval Details

- The system uses a Generative AI model to generate responses to user queries.
- Vehicle-related data is structured and used as contextual input.
- The backend retrieves relevant information before generating responses.
- The design follows a Retrieval-Augmented Generation (RAG)-style workflow.

Note: This project focuses on practical implementation and educational demonstration of domain-specific AI systems.

🏗️ Architecture
🔹 Backend

Framework: FastAPI

Server: Uvicorn

Language: Python

Features:

REST API endpoints

VIN decoding route

Custom middleware (Logging & Security Headers)

Exception handling

CORS configuration

Runs on:

http://localhost:8000
🔹 Frontend

Framework: React

Build Tool: Vite

Language: JavaScript

Runs on:

http://localhost:5173
📁 Project Structure
automotive-faq-assistant/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       └── vin.py
│   ├── core/
│   │   ├── config.py
│   │   ├── middleware.py
│   │   └── exceptions.py
│
├── venv/
├── requirements.txt
├── README.md
│
└── frontend/
    ├── src/
    │   └── App.jsx
    ├── package.json
    └── vite.config.js
⚙️ Backend Setup Instructions
1️⃣ Create Virtual Environment
python -m venv venv
2️⃣ Activate Virtual Environment (Windows)
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Backend Server
python -m uvicorn app.main:app --reload

Backend will be available at:

http://localhost:8000
🌐 Frontend Setup Instructions
1️⃣ Navigate to Frontend Folder
cd frontend
2️⃣ Install Dependencies
npm install
3️⃣ Start Development Server
npm run dev

Frontend will be available at:

http://localhost:5173
🔌 API Endpoints
🔹 Health Check
GET /

Response:

{
  "status": "healthy",
  "version": "x.x.x"
}
🔹 VIN Endpoint
GET /api/v1/vin/{vin_number}

Returns decoded vehicle information.

🛡️ Features Implemented

FastAPI backend architecture

Custom middleware (logging & security headers)

Structured API routing

CORS configuration

Exception handling

React frontend setup

Frontend-backend connectivity

🧪 Development Status
✅ Completed

Backend architecture

API routing

Middleware implementation

CORS configuration

React project setup

Node.js installation

⏳ In Progress

VIN UI integration

Structured response display

UI improvements

Enhanced error handling

🛠️ Technologies Used

Python

FastAPI

Uvicorn

React

Vite

JavaScript

HTML/CSS

📌 Future Improvements

Better UI styling

Form validation

Enhanced VIN data visualization

Deployment (Docker / Cloud hosting)

Authentication system

FAQ search feature


📄 License

This project is for educational and portfolio purposes.

🎯 Final Notes

This project demonstrates:

Full-stack development skills

REST API architecture

Frontend-backend communication

Modern JavaScript and Python frameworks

Environment setup & debugging skills





