from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import json
import os
import pickle
from flask_cors import CORS
import joblib


app = Flask(__name__)

# ✅ Enable CORS (allow Angular frontend)
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

# ------------------------------
# 1️⃣ Load Embedding Model
# ------------------------------
print("🔹 Loading embedding model...")
embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# ------------------------------
# 2️⃣ Load or Build Skill Index
# ------------------------------
INDEX_PATH = "skill_index.faiss"
EMB_PATH = "skill_embs.npy"
ID_PATH = "skill_ids.json"

if os.path.exists(INDEX_PATH) and os.path.exists(EMB_PATH) and os.path.exists(ID_PATH):
    print("📂 Loading existing FAISS index and embeddings...")
    index = faiss.read_index(INDEX_PATH)
    skill_embs = np.load(EMB_PATH)
    with open(ID_PATH, "r") as f:
        skill_names = json.load(f)
else:
    print("⚙️ Building FAISS index for the first time...")

    skill_names = [
        "Python", "Java", "C++", "HTML", "CSS", "JavaScript", "React", "Angular", "Node.js",
        "Django", "Flask", "Machine Learning", "Deep Learning", "Data Science", "SQL",
        "MongoDB", "AWS", "Docker", "Kubernetes", "Git", "Linux", "TensorFlow", "PyTorch",
        "Computer Vision", "NLP", "Data Analysis", "AI", "DevOps", "Frontend", "Backend",
        "Cloud Computing", "Cybersecurity", "Blockchain", "Flutter", "Android", "iOS",
        "Testing", "Automation", "REST API", "Express", "UI/UX Design"
    ]

    # Generate embeddings for each skill
    skill_embs = np.array(embedder.encode(skill_names, normalize_embeddings=True))

    # Build FAISS index
    index = faiss.IndexFlatIP(skill_embs.shape[1])
    index.add(skill_embs)

    # Save for reuse
    faiss.write_index(index, INDEX_PATH)
    np.save(EMB_PATH, skill_embs)
    with open(ID_PATH, "w") as f:
        json.dump(skill_names, f)

print("✅ FAISS model ready!")

# ------------------------------
# 3️⃣ Skill Recommendation API
# ------------------------------
# ------------------------------


@app.route("/recommend-skills", methods=["POST"])
def recommend_skills():
    data = request.get_json()
    extracted_skills = data.get("skills", [])
    if not extracted_skills:
        return jsonify({"success": False, "message": "No skills provided"}), 400

    print(f"🧠 Received skills: {extracted_skills}")

    # Compute embeddings for input skills
    query_embs = np.array(embedder.encode(extracted_skills, normalize_embeddings=True))

    # Search top 5 nearest for each skill
    D, I = index.search(query_embs, 5)

    recommended = set()
    for neighbors in I:
        for idx in neighbors:
            recommended.add(skill_names[idx])

    # Remove already present skills
    recommended = list(set(recommended) - set(extracted_skills))

    return jsonify({
        "success": True,
        "input_skills": extracted_skills,
        "recommended_skills": recommended
    })


try:
    model = pickle.load(open("career_model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    print("✅ Career model loaded!")
except Exception as e:
    print("⚠️ Could not load model:", e)
    model = None
    vectorizer = None


@app.route('/predict-career', methods=['POST'])
def predict_career():
    try:
        data = request.get_json()
        skills = data.get("skills", [])

        if not skills:
            return jsonify({"success": False, "message": "Please provide skills"}), 400

        # ✅ Convert list of skills → single space-separated string
        skill_text = " ".join(skills)

        # Transform and predict
        X = vectorizer.transform([skill_text])
        prediction = model.predict(X)[0]

        return jsonify({
            "success": True,
            "predicted_role": prediction
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ------------------------------
# 5️⃣ Run the Service
# ------------------------------






# Load the career_skills.json data
with open("career_skills.json", "r") as f:
    career_data = json.load(f)
@app.route('/api/skills/gap', methods=['POST'])
def skill_gap_analysis():
    try:
        data = request.get_json()
        user_skills = [s.strip().lower() for s in data.get("skills", [])]
        target_role = data.get("target_role")

        if not target_role or target_role not in career_data:
            return jsonify({"error": "Invalid or missing target_role"}), 400

        role_info = career_data[target_role]
        required_skills = [s.lower() for s in role_info["required_skills"]]
        importance = role_info["importance"]

        # Calculate missing and matched skills
        matched_skills = [s for s in required_skills if s in user_skills]
        missing_skills = [s for s in required_skills if s not in user_skills]

        # Calculate readiness %
        readiness = round((len(matched_skills) / len(required_skills)) * 100, 2)

        # Prepare detailed report
        missing_details = []
        for i, skill in enumerate(required_skills):
            if skill not in user_skills:
                missing_details.append({
                    "skill": skill,
                    "importance": importance[i]
                })

        response = {
            "target_role": target_role,
            "total_skills_required": len(required_skills),
            "matched_skills_count": len(matched_skills),
            "missing_skills_count": len(missing_skills),
            "readiness_percentage": readiness,
            "matched_skills": matched_skills,
            "missing_skills": missing_details
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/forecast-growth", methods=["POST"])
def forecast_growth():
    import numpy as np
    import joblib
    from flask import jsonify, request

    # Try loading model and encoder (optional)
    try:
        model = joblib.load("career_forecast_model.pkl")
        encoder = joblib.load("career_role_encoder.pkl")
    except:
        model = None
        encoder = None

    data = request.json
    skills = data.get("skills", [])
    target_role = data.get("target_role", "")
    exp = float(data.get("experience_years", 0))
    projects = int(data.get("projects_done", 0))
    certs = int(data.get("certifications", 0))
    learning_rate = len(skills) / (exp + 1)

    # ✅ STEP 1: Complete Skill Map for 40 Career Roles
    role_skill_map = {
        "Data Scientist": ["Python", "R", "Machine Learning", "Pandas", "NumPy", "Statistics", "SQL", "TensorFlow", "Data Visualization", "Matplotlib"],
        "Backend Developer": ["Python", "Java", "C#", "Node.js", "Express", "SQL", "MongoDB", "APIs", "Docker", "Git", "AWS"],
        "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "Angular", "TypeScript", "UI/UX", "Bootstrap", "Redux", "Tailwind"],
        "Full Stack Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js", "Express", "MongoDB", "SQL", "Git", "AWS"],
        "ML Engineer": ["Python", "TensorFlow", "PyTorch", "Machine Learning", "Deep Learning", "SQL", "Data Preprocessing", "NLP", "Computer Vision"],
        "UI/UX Designer": ["Figma", "Adobe XD", "User Research", "Wireframing", "Prototyping", "Design Systems", "Visual Design", "Typography"],
        "Cloud Engineer": ["AWS", "Azure", "Docker", "Kubernetes", "Linux", "Terraform", "Networking", "CI/CD", "Monitoring"],
        "Cybersecurity Analyst": ["Network Security", "Penetration Testing", "Linux", "Firewalls", "SIEM", "Threat Analysis", "Encryption", "Incident Response"],
        "Product Manager": ["Agile", "Scrum", "Roadmaps", "JIRA", "Stakeholder Management", "Market Research", "Data Analysis"],
        "DevOps Engineer": ["Linux", "Docker", "Kubernetes", "Jenkins", "AWS", "Terraform", "CI/CD", "Git", "Monitoring"],

        "Data Analyst": ["Excel", "Python", "SQL", "Power BI", "Tableau", "Statistics", "Data Cleaning", "Visualization"],
        "Business Analyst": ["Excel", "SQL", "Power BI", "Requirement Gathering", "Documentation", "Communication"],
        "AI Engineer": ["Python", "Deep Learning", "TensorFlow", "PyTorch", "ML Algorithms", "Data Pipelines"],
        "Software Engineer": ["C++", "Java", "Python", "DSA", "OOP", "Git", "SQL"],
        "Game Developer": ["C++", "C#", "Unity", "Unreal Engine", "3D Modelling", "Game Physics"],
        "Blockchain Developer": ["Solidity", "Ethereum", "Smart Contracts", "Cryptography", "Web3.js", "Truffle"],
        "Mobile App Developer": ["Java", "Kotlin", "Swift", "Flutter", "React Native", "APIs", "Firebase"],
        "Embedded Systems Engineer": ["C", "C++", "Microcontrollers", "RTOS", "Sensors", "IoT"],
        "IoT Engineer": ["Python", "C", "Arduino", "Raspberry Pi", "Networking", "MQTT"],
        "AR/VR Developer": ["Unity", "C#", "3D Modelling", "OpenXR", "Computer Vision"],

        "Database Administrator": ["SQL", "Oracle", "MySQL", "Backup", "Replication", "Security"],
        "Network Engineer": ["Networking", "CCNA", "Routing", "Switching", "Firewalls", "VPN"],
        "Cloud Architect": ["AWS", "Azure", "GCP", "Terraform", "Networking", "Security", "Scalability"],
        "System Administrator": ["Linux", "Windows Server", "Shell Scripting", "Networking", "Monitoring"],
        "QA Engineer": ["Manual Testing", "Automation", "Selenium", "JMeter", "Postman", "Test Cases"],
        "Data Engineer": ["Python", "Spark", "Hadoop", "ETL", "SQL", "Data Warehousing", "Kafka"],
        "Research Scientist": ["Python", "R", "Statistics", "Mathematics", "Data Modeling", "Experimentation"],
        "Technical Writer": ["Documentation", "Markdown", "Technical Understanding", "Editing", "Research"],
        "Digital Marketer": ["SEO", "Google Ads", "Content Writing", "Analytics", "Social Media"],
        "Cloud Security Engineer": ["AWS", "IAM", "Network Security", "Encryption", "Penetration Testing"],

        "AI Researcher": ["Python", "TensorFlow", "ML", "DL", "NLP", "Research Writing"],
        "Computer Vision Engineer": ["Python", "OpenCV", "Deep Learning", "TensorFlow", "Image Processing"],
        "Data Architect": ["SQL", "ETL", "Data Modeling", "Cloud", "Database Design"],
        "Statistician": ["Statistics", "R", "SPSS", "Excel", "Data Interpretation"],
        "IT Support Engineer": ["Troubleshooting", "Networking", "Hardware", "Windows", "Linux"],
        "Project Manager": ["Agile", "Scrum", "Planning", "Risk Management", "Leadership"],
        "Hardware Engineer": ["Circuit Design", "Microcontrollers", "Testing", "Soldering", "PCB Design"],
        "SEO Specialist": ["SEO", "Analytics", "Keyword Research", "Content Optimization"],
        "Data Engineer": ["Python", "SQL", "ETL", "Spark", "Data Pipelines"],
        "Game Designer": ["Game Mechanics", "Storyboarding", "3D Modelling", "Unity"]
    }

    role_skills = role_skill_map.get(target_role, [])
    total_skills = len(role_skills)

    if total_skills == 0:
        return jsonify({"error": "Unknown or unmapped role"}), 400

    # ✅ STEP 2: Skill matching
    matching_skills = [s for s in role_skills if s in skills]
    missing_skills = [s for s in role_skills if s not in skills]
    skill_coverage = len(matching_skills) / total_skills

    # ✅ STEP 3: Readiness computation (balanced + realistic)
    readiness = (
        (skill_coverage * 70)
        + (min(exp, 5) * 5)
        + (min(projects, 10) * 1.5)
        + (certs * 2)
        + min(learning_rate, 10)
    )

    readiness = max(0, min(100, readiness))
    months_to_job_ready = max(1, 12 * (1 - (readiness / 100)))

    forecast_curve = [
        min(100, round(readiness + i * (100 - readiness) / max(1, months_to_job_ready), 2))
        for i in range(int(months_to_job_ready) + 1)
    ]

    return jsonify({
        "target_role": target_role,
        "career_readiness_score": round(readiness, 2),
        "job_ready_in_months": round(months_to_job_ready, 2),
        "skill_coverage_percent": round(skill_coverage * 100, 2),
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "forecast_curve": forecast_curve
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
