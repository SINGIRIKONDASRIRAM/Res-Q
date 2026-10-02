# 🚨 ResQ - Smart Disaster Response & Resource Allocation System

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.2-61DAFB.svg?style=flat&logo=React&logoColor=black)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-5.1-646CFF.svg?style=flat&logo=Vite&logoColor=white)](https://vitejs.dev/)
[![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-3.4-38B2AC.svg?style=flat&logo=Tailwind-CSS&logoColor=white)](https://tailwindcss.com/)
[![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E.svg?style=flat&logo=Supabase&logoColor=white)](https://supabase.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat&logo=Python&logoColor=white)](https://www.python.org/)

**ResQ** is a comprehensive, real-time disaster management and emergency resource allocation platform designed to optimize crisis response operations. By combining live spatial visualization, automated urgency scoring, linear-programming resource allocation, multi-channel citizen reporting (Web, SMS, WhatsApp), and real-time weather intelligence, ResQ empowers emergency commanders and response teams to make fast, data-driven decisions when every second counts.

---

## ✨ Key Features

### 🗺️ Live Interactive Command & Disaster Map
- **Spatial Tracking**: View active disasters, affected zones, shelters, citizen emergency requests, and deployed rescue teams on an interactive Leaflet map.
- **Dynamic Layer Controls**: Filter by disaster severity, resource availability, and risk radius.
- **Real-Time Updates**: Live websocket updates for active incidents and personnel locations.

### 🧠 Intelligent Priority & Urgency Engine
- **NLP Disaster Parser**: Automatically parses free-form emergency descriptions from citizens into structured crisis data.
- **Risk & Urgency Scoring**: Evaluates severity based on casualty counts, vulnerability indices, environmental parameters, and time elapsed.

### ⚡ Optimized Resource Allocation & Route Optimization
- **Linear Programming Allocation**: Uses `PuLP` optimization models to mathematically assign vehicles, rescue personnel, and inventory (food, medical, shelter) to critical zones.
- **Route Optimization**: Computes safe, efficient paths and evacuation routes avoiding hazard zones.

### 📱 Multi-Channel Citizen Reporting & Alerts
- **Public Emergency Portal**: Self-service emergency report submission, request tracking, and safe shelter locator.
- **SMS & WhatsApp Integration**: Twilio-powered incoming report handler for low-connectivity environments where web access is unavailable.
- **Emergency Broadcasts**: Instant weather alerts and evacuation advisories sent via SMS/WhatsApp.

### 🌤️ Weather Insights & Predictive Analytics
- **OpenWeatherMap Integration**: Live weather monitoring (wind speed, precipitation, pressure, temperature) and forecast warnings.
- **Analytics Dashboards**: Visual charts tracking incident trends, resource utilization, and emergency response efficiency over time using Recharts.

---

## 🛠️ Tech Stack

| Domain | Technologies Used |
| :--- | :--- |
| **Frontend Framework** | React 18, Vite |
| **Styling & UI** | Tailwind CSS, Framer Motion, Lucide React Icons |
| **Mapping & Charts** | Leaflet, React-Leaflet, Recharts |
| **Backend API** | FastAPI (Python 3.10+), Uvicorn |
| **Database & Auth** | Supabase (PostgreSQL) |
| **Optimization & Science** | PuLP (Linear Programming), SciPy, NumPy, Pandas |
| **Messaging & Telecom** | Twilio API (SMS & WhatsApp Cloud API) |
| **Weather Data** | OpenWeatherMap API |
| **Deployment** | Vercel Serverless / Docker Ready |

---

## 📂 Project Architecture

```
ResQ/
├── api/                    # Vercel serverless entry point
│   └── index.py
├── backend/                # FastAPI Application Core
│   ├── main.py             # FastAPI App Entrypoint
│   ├── database.py         # Supabase Connection & Queries
│   ├── schema.sql          # PostgreSQL Database Schema
│   ├── requirements.txt    # Python Dependencies
│   ├── routes/             # REST & Webhook Routers
│   │   ├── citizen_reports.py
│   │   ├── disaster_reports.py
│   │   ├── sms.py
│   │   └── weather.py
│   └── services/           # Business Logic & Algorithms
│       ├── disaster_parser.py
│       ├── optimizer.py
│       ├── priority_engine.py
│       ├── resource_allocator.py
│       ├── route_optimizer.py
│       ├── twilio_service.py
│       └── weather_service.py
├── frontend/               # React (Vite) Application
│   ├── src/
│   │   ├── components/     # Reusable UI & Map Components
│   │   ├── context/        # React Context Providers
│   │   ├── pages/          # App Pages (Dashboard, Map, Citizen Portal, etc.)
│   │   ├── services/       # API Services
│   │   └── App.jsx
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
├── .env.example            # Environment Variables Template
├── package.json            # Root Package Configuration
└── vercel.json             # Vercel Deployment Configuration
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your machine:
- **Node.js**: v18.0 or higher
- **npm**: v9.0 or higher
- **Python**: v3.10 or higher
- **Git**

---

### 1. Clone the Repository

```bash
git clone https://github.com/chaaru-hub/ResQ-.git
cd ResQ-
```

---

### 2. Environment Setup

Copy `.env.example` to create your local `.env` configuration file:

```bash
cp .env.example .env
```

Configure your credentials in `.env`:
- **Supabase**: `SUPABASE_URL`, `SUPABASE_KEY`, `VITE_SUPABASE_URL`, `VITE_SUPABASE_ANON_KEY`
- **Twilio**: `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_WHATSAPP_NUMBER`
- **OpenWeather**: `OPENWEATHER_API_KEY`, `VITE_OPENWEATHER_API_KEY`

---

### 3. Backend Setup (FastAPI)

Navigate to the `backend` directory and set up a virtual environment:

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start FastAPI development server
uvicorn main:app --reload --port 8000
```

The FastAPI backend server will be running at `http://localhost:8000`. Interactive API docs (Swagger UI) are available at `http://localhost:8000/docs`.

---

### 4. Frontend Setup (React + Vite)

In a new terminal window, navigate to the `frontend` directory:

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start Vite dev server
npm run dev
```

The web application will be accessible at `http://localhost:5173`.

---

## 📡 Key API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/disasters` | Fetch active disaster incidents |
| `POST` | `/api/disasters` | Report a new disaster incident |
| `GET` | `/api/citizen-reports` | Retrieve citizen emergency reports |
| `POST` | `/api/citizen-reports` | Submit a public emergency report |
| `POST` | `/api/sms/webhook` | Twilio inbound SMS webhook handler |
| `GET` | `/api/weather/insights` | Fetch weather hazards & forecasts for location |
| `POST` | `/api/allocate` | Trigger PuLP LP resource allocation engine |

---

## 🌐 Deployment

The project is configured for deployment on **Vercel**:
- `vercel.json` routes static requests to the built React frontend (`frontend/dist`) and API requests to `/api`.

To deploy via Vercel CLI:
```bash
npm run build
vercel --prod
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
