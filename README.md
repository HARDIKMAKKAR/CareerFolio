# CareerFolio 🚀

An AI-powered career guidance and resume analysis platform that helps students and professionals identify skill gaps, predict career paths, receive personalized recommendations, and forecast career readiness using Machine Learning and NLP.

## 🌐 Live Demo

https://careerfolio-qpc0.onrender.com/

---

# 📌 Overview

CareerFolio is designed to provide intelligent career guidance through resume understanding, skill analysis, and predictive career modeling.

The platform enables users to:

- Upload resumes for automatic skill extraction
- Predict suitable career roles using ML models
- Identify missing skills for target job roles
- Get AI-powered skill recommendations
- Forecast career readiness and job preparedness
- Track career growth through data-driven insights

---

# ✨ Features

## 📄 Resume Analysis
- Resume parsing and preprocessing
- Skill extraction using NLP techniques
- Detection of certifications, projects, and technologies

## 🤖 Career Prediction
- Predicts suitable career paths using Machine Learning
- Uses trained Random Forest classification models

## 🧠 Skill Recommendation Engine
- Semantic skill matching using sentence embeddings
- FAISS-powered nearest neighbor search
- Recommends related and high-demand skills

## 📊 Skill Gap Analysis
- Compares user skills with target role requirements
- Calculates readiness percentage
- Displays missing skills with importance levels

## 📈 Career Growth Forecasting
- Estimates career readiness score
- Predicts approximate time to become job-ready
- Uses Linear Regression with hybrid rule-based logic

## 🎨 Interactive Dashboard
- Modern Angular-based responsive UI
- Resume upload interface
- Dynamic charts and result visualization

---

# 🏗️ System Architecture

CareerFolio follows a microservice-based architecture.

```text
Angular Frontend
        ↓
Node.js / Express Backend
        ↓
Flask ML Service
        ↓
MongoDB Database
```

---

# ⚙️ Tech Stack

| Layer | Technologies |
|---|---|
| Frontend | Angular, TypeScript, HTML, CSS |
| Backend | Node.js, Express.js |
| ML Service | Flask, Scikit-learn, Pandas, NumPy |
| ML & NLP | Sentence Transformers, FAISS |
| Database | MongoDB |
| Deployment | Render |
| Version Control | Git, GitHub |

---

# 🧠 Machine Learning Modules

## 1️⃣ Resume Skill Extraction
Extracts:
- Technical skills
- Soft skills
- Certifications
- Projects
- Experience indicators

using NLP preprocessing and heuristic-based analysis.

---

## 2️⃣ Career Path Prediction
Uses a trained Random Forest Classifier to predict:
- Suitable career roles
- Career alignment
- Domain suitability

---

## 3️⃣ Skill Recommendation System
Uses:
- Sentence embeddings
- Semantic similarity
- FAISS vector search

to recommend related and missing skills.

---

## 4️⃣ Skill Gap Analysis
Compares:
- User skills
- Role-specific required skills

and computes:
- Missing skills
- Matching skills
- Readiness percentage
- Skill importance

---

## 5️⃣ Career Growth Forecasting
Forecasts:
- Career readiness score
- Learning progression
- Estimated months to become job-ready

using hybrid ML + rule-based scoring.

---

# 📂 Project Structure

```text
CareerFolio/
│
├── frontend/          # Angular frontend
├── backend/           # Node.js backend
├── ml-service/        # Flask ML microservice
│
├── README.md
```

---

# 🚀 Deployment Architecture

| Service | Platform |
|---|---|
| Angular Frontend | Render Static Site |
| Node.js Backend | Render Web Service |
| Flask ML Service | Render Web Service |
| Database | MongoDB Atlas |

---

# 🔌 API Architecture

## Backend APIs
- Authentication APIs
- Resume upload APIs
- File management APIs
- Route orchestration APIs

## ML APIs
- `/recommend-skills`
- `/predict-career`
- `/api/skills/gap`
- `/forecast-growth`

---

# 🛠️ Installation & Setup

## Prerequisites

- Node.js
- Angular CLI
- Python 3.x
- MongoDB
- Git

---

# 1️⃣ Clone Repository

```bash
git clone https://github.com/HARDIKMAKKAR/CareerFolio.git
cd CareerFolio
```

---

# 2️⃣ Frontend Setup

```bash
cd frontend
npm install
ng serve
```

Frontend runs on:

```text
http://localhost:4200
```

---

# 3️⃣ Backend Setup

```bash
cd backend
npm install
npm start
```

Backend runs on:

```text
http://localhost:5000
```

---

# 4️⃣ ML Service Setup

```bash
cd ml-service

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

python app.py
```

ML Service runs on:

```text
http://localhost:5001
```

---

# 📦 Core Libraries Used

## Frontend
- Angular
- RxJS
- TypeScript

## Backend
- Express.js
- Mongoose
- Multer
- JWT Authentication

## ML/NLP
- Scikit-learn
- Sentence Transformers
- FAISS
- NumPy
- Pandas

---

# 🧪 Testing

The platform includes:
- Unit testing
- API testing
- Integration testing
- User interface testing

---

# 📈 Future Enhancements

- Real-time job market integration
- AI learning roadmap generation
- Personalized course recommendations
- Gamified career tracking
- Mobile application support
- Advanced analytics dashboard

---

# 👨‍💻 Author

**Hardik Makkar**  
B.Tech CSE — JC Bose University YMCA  
AI/ML • Full Stack • Cloud • Data-Driven Systems

---

# 📄 License

This project is developed for educational and research purposes.
