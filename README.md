# CareerFolio

CareerFolio is an AI-powered career guidance platform that helps students and professionals analyze resumes, identify skill gaps, explore suitable career paths, and forecast career readiness.[1]

## Overview

The project is designed as a data-driven platform for career planning. It focuses on resume understanding, career path prediction, skill recommendation, skill gap analysis, and career growth forecasting through a web-based interface.[1]

Core goals of the project include:
- Automatic resume analysis to extract skills, experience, certifications, and project-related signals.[1]
- Career path recommendation based on extracted skills and profile features.[1]
- Skill gap identification against a selected target role.[1]
- Career readiness forecasting and estimation of time to become job-ready.[1]
- Personalized learning and improvement guidance for continuous growth.[1]

## Features

- Resume-based skill extraction using NLP and rule-based heuristics.[1]
- Career path prediction using a Random Forest classifier.[1]
- Skill recommendation using embedding-based nearest neighbour search with FAISS.[1]
- Skill gap analysis using weighted role-skill matching.[1]
- Career growth forecasting using Linear Regression with hybrid rule logic.[1]
- Component-based Angular dashboard for uploading resumes and viewing results.[1]

## Architecture

CareerFolio follows a three-part architecture built around a frontend, an application backend, and an ML service.[1]

### Frontend
- **Angular** frontend built with TypeScript, HTML, and CSS for a modular and responsive user interface.[1]

### Backend
- **Node.js** backend for authentication, user management, session handling, and API routing.[1]

### ML Service
- **Flask** microservice for model inference, skill analysis, recommendation, and forecasting APIs.[1]

### Service Communication
- The Node.js backend and Flask ML service communicate through REST APIs using JSON payloads.[1]

## Machine Learning Modules

### 1. Resume Skill Extraction
Extracts technical and soft skills, experience, certifications, and project information from uploaded resumes using NLP preprocessing and rule heuristics.[1]

### 2. Career Path Prediction
Uses a Random Forest classifier trained on role-skill data to predict suitable career roles and confidence scores from extracted features.[1]

### 3. Skill Recommendation
Uses embeddings with FAISS-based nearest neighbour search to recommend related or missing skills based on the user's current profile.[1]

### 4. Skill Gap Analysis
Compares a user's extracted skills with target-role skill requirements and computes missing skills, readiness, and weighted importance.[1]

### 5. Career Growth Forecasting
Uses Linear Regression plus rule-based post-processing to estimate readiness score and time to become job-ready.[1]

## Tech Stack

| Layer | Technologies |
|---|---|
| Frontend | Angular, TypeScript, HTML, CSS [1] |
| Backend | Node.js, Express-style API routing [1] |
| ML Service | Flask, Scikit-learn, Pandas, NumPy [1] |
| ML Retrieval | Embeddings, FAISS [1] |
| Deployment | AWS used in the original project deployment setup [1] |
| Tooling | Git, GitHub, VS Code, Angular CLI [1] |

## Repository Structure

```text
CareerFolio_Final/
├── frontend/       # Angular application
├── backend/        # Node.js backend
├── ml-service/     # Flask ML service and trained models
└── README.md
```

A practical structure for the ML service is:

```text
ml-service/
├── app.py
├── requirements.txt
├── models/
├── data/
└── scripts/
```

## Setup

### Prerequisites
- Node.js 14+ for frontend and backend development.[1]
- Angular CLI for Angular development.[1]
- Python environment for the Flask ML service and model dependencies.[1]
- Git for version control.[1]

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd CareerFolio_Final
```

### 2. Run the frontend
```bash
cd frontend
npm install
ng serve
```

### 3. Run the backend
```bash
cd backend
npm install
npm start
```

### 4. Run the ML service
```bash
cd ml-service
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Workflow

The development followed an Agile approach with iterative development, testing, integration, and user feedback cycles.[1] The system was built with modular separation between Angular, Node.js, and Flask so that frontend logic, core backend operations, and ML inference could evolve independently.[1]

## Testing

The report describes testing at three levels:[1]
- Unit testing for ML models, API endpoints, and UI components.[1]
- Integration testing across Angular, Node.js, and Flask services.[1]
- User testing to refine prediction quality and dashboard clarity.[1]

## Future Improvements

- Add a stronger Skill Value Index (SVI) for richer skill evaluation.[1]
- Integrate real-time job market analysis.[1]
- Develop a mobile application.[1]
- Add personalized learning paths and goal-based recommendations.[1]
- Improve personalization with user activity analytics and gamified features.[1]

## Notes

The project report states that trained models were deployed as serialized `.pkl` files through Flask routes, so model artifacts and related runtime files should remain available to the ML service in deployment.[1]
