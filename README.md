# Enterprise Customer Support Ticket System

**Hands-On Learning Project – Started March 7, 2026**

Personal project to build practical AWS, Docker, Kubernetes & Agentic AI skills  
Inspired by my daily work at Samsung: L2 issue tracking, FER registration, customer onboarding & REST API integrations.

## Project Goal
Create a 3-tier SaaS-style Customer Support portal (Flask backend + MySQL DB)  
→ Containerize with Docker → Deploy to Kubernetes → Add AI agent for ticket triage

## Week 1 Progress (March 7–15, 2026)
- [x] VS Code + Python venv setup
- [x] Flask installed & first local web app running (Day 1)
- [ ] AWS account creation & IAM (Day 2)
- [ ] EC2 launch + live deployment (Day 3+)

## Tech Stack (Building Step-by-Step)
- Backend: Python + Flask
- Database: MySQL (RDS later)
- Cloud: AWS Free Tier (ap-south-1)
- Tools: VS Code, GitHub, Docker (later), Kubernetes (later)

## Screenshots
<image-card alt="Day 1 Local Flask App" src="screenshots/day1-local-app.png" ></image-card>

## How to Run Locally (Updated after each day)
```bash
# Activate venv
.venv\Scripts\activate

# Install dependencies (only once)
pip install flask

# Run the app
python app.py