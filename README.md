# Group-22---CITS5206
Information Technology Capstone Project

# 🏛️ AI Museum – Western Australia
*A Virtual Museum of A.I. Software Technology*

---

## 📌 Project Overview
The **AI Museum – Western Australia** is a full-stack Flask web application designed to present the history of artificial intelligence software through an interactive virtual museum experience.

The platform allows users to explore **10 major paradigm shifts in AI**, view educational content with images and references, search exhibits, follow a guided tour, and examine the role of **Western Australia** in the broader history of AI.

This project was developed as part of the **CITS5206 Information Technology Capstone Project**.

---

## 👥 Team Members
| Name | Student ID | GitHub Username |
|------|------------|-----------------|
| Roshini Vadla | 24324533 | RoshiniVadla75 |
| Weiyu Xu | 24233679 | Hannah-X0206 |
| Shanin Rashid | 24117314 | kdmars0168 |
| Noah Ning | 24120321 | NingNoah |
| Xi Qin | 24235608 | xiqin2049 |

---

## 🎯 Project Purpose
- Provide an interactive museum-style learning experience  
- Present historical and modern AI developments in a structured way  
- Highlight Western Australia’s contributions to AI and computing  
- Support educational storytelling through multimedia and exhibit-style pages  
- Transform complex AI concepts into accessible content for students and general users  

---

## 🧠 AI Paradigm Shifts Covered
1. Alan Turing’s Thoughts on AI  
2. Learning Machines  
3. Game Playing AI  
4. Expert Systems  
5. Artificial Neural Networks  
6. Internet-Driven AI / IBM Watson  
7. Evolutionary Computing & Genetic Algorithms  
8. Synthetic Media Technology / Deep Fakes  
9. Natural Language Processing  
10. Large Language Models  

---

## 🧭 Main Application Pages

### 🏠 Home
- Entry point of the virtual museum  
- Introduces the project and navigation  
- Displays preview of AI topics  

### ⏳ Timeline
- Displays AI evolution chronologically  
- Supports filtering by decade, category, and status  
- Shows structured exhibit summaries  

### 🌏 Explore WA
- Highlights Western Australian contributions  
- Connects local institutions to global AI development  

### 🧭 Guided Tour
- Provides structured walkthrough of exhibits  
- Presents each topic as a museum exhibit  

### 🔍 Search
- Allows users to search across topics  
- Filters by title, category, year, and content  

### 📄 Topic Detail
- Displays full exhibit content including:
  - introduction  
  - summary  
  - explanation  
  - examples  
  - WA context  
  - references  
  - media  

### 🔐 Authentication
- Login and signup functionality  
- Session handling using Flask-Login  
- Dynamic navbar based on user state  

---

## 🖼️ Multimedia and Educational Content
- Images and captions  
- Topic references  
- WA-specific contextual information  
- Structured exhibit explanations  
- Educational storytelling sections  

---

## 🛠️ Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript  

### Backend
- Flask  
- Flask-Login  
- Flask-SQLAlchemy  
- Flask-WTF  
- Flask-Migrate  

### Database
- SQLite  

### ORM / Migrations
- SQLAlchemy  
- Alembic  

---

## 🚀 How to Launch the Application

### 1. Clone the repository
```bash
git clone https://github.com/RoshiniVadla75/Group-22---CITS5206.git
cd Group-22---CITS5206
```
2. Create a virtual environment
```bash
python -m venv venv
```
3. Activate the environment

MacOS / Linux
```bash
source venv/bin/activate
```
Windows
```bash
venv\Scripts\activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Initialise and seed the database
```bash
python init_db.py
```
6. Run the application
```bash
python app.py
```
7. Open in browser

http://127.0.0.1:5000/


⸻

🔐 Authentication

This project includes a user authentication system using Flask-Login.

Features:
	•	User registration
	•	User login
	•	Session management
	•	Authentication-aware navigation

You may need to register a user before testing login features.

⸻

🔌 API Endpoints

The backend provides API routes for dynamic content:
	•	GET /api/topics
→ Returns all topics
	•	GET /api/topics/<slug>
→ Returns a single topic

These endpoints are used by frontend JavaScript to render data dynamically.

⸻

🗂️ Project Structure

Group-22---CITS5206/
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│
├── migrations/
│
├── instance/
│   └── ai_museum.db
│
├── app.py
├── init_db.py
├── models.py
├── routes.py
├── requirements.txt
├── .gitignore
└── README.md


⸻

🧪 Database Notes
	•	Database is seeded via init_db.py
	•	Includes:
	•	10 AI topics
	•	media (images)
	•	references
	•	WA context

⸻

✅ Features Implemented
	•	Full Flask backend
	•	SQLite database integration
	•	API-driven frontend rendering
	•	Timeline with filters
	•	Guided Tour system
	•	Search functionality
	•	Topic detail pages
	•	User authentication
	•	Responsive UI
	•	Shared navigation system

⸻

📄 License

This project is developed for academic purposes (CITS5206).

⸻

✨ Summary

The AI Museum – Western Australia demonstrates how complex AI concepts can be transformed into an interactive digital museum experience. By combining backend data, structured UI, and educational storytelling, the system provides an engaging and accessible way to explore the history of artificial intelligence.

---