# Group-22---CITS5206  
Information Technology Capstone Project  

# 🏛️ AI Museum – Western Australia  
*A Virtual Museum of A.I. Software Technology*

---

## 📌 Project Overview

The **AI Museum – Western Australia** is a full-stack web application designed to present the history of artificial intelligence through an interactive virtual museum experience.

The system enables users to explore **10 major paradigm shifts in AI (1950–present)** using guided exhibits, multimedia content, search functionality, and structured storytelling.

This project transforms complex AI concepts into an engaging and accessible learning experience, with a focus on **Western Australian contributions** to computing and AI research.

---

## 👥 Team Members

| Name            | Student ID | GitHub Username |
|-----------------|------------|-----------------|
| Roshini Vadla   | 24324533   | RoshiniVadla75  |
| Weiyu Xu        | 24233679   | Hannah-X0206    |
| Shanin Rashid   | 24117314   | kdmars0168      |
| Noah Ning       | 24120321   | NingNoah        |
| Xi Qin          | 24235608   | xiqin2049       |

---

## 🎯 Purpose

- Provide an interactive museum-style learning experience  
- Present historical and modern AI developments  
- Highlight Western Australia’s contributions  
- Support visual and multimedia-based education  

---

## 🧠 AI Paradigm Shifts Covered

1. Turing’s AI Foundations (1950)  
2. Learning Machines (1960s)  
3. Game Playing Systems (1970s)  
4. Expert Systems (1980s)  
5. Artificial Neural Networks (1980–2000)  
6. Internet-Driven AI / IBM Watson (2010)  
7. Evolutionary Computing & Genetic Algorithms  
8. Synthetic Media / Deepfakes  
9. Natural Language Processing (NLP)  
10. Large Language Models (LLMs)  

---

## 🧭 Application Pages

### 🏠 Home
- Entry point of the virtual museum  
- Overview of the project  
- Navigation hub  

### ⏳ Timeline
- Chronological AI development  
- Filter by decade, category, and status  
- Interactive exploration  

### 🌏 Explore WA
- Focus on Western Australian contributions  
- Local institutions and research  

### 🧭 Guided Tour
- Step-by-step structured learning  
- Educational explanations and examples  

### 🔍 Search
- Search across all topics  
- Real-time filtering  
- Archive-style browsing  

### 📄 Topic Detail
- Full topic breakdown  
- Includes:
  - Introduction  
  - How it works  
  - Examples  
  - WA context  
  - References  
  - Media  

---

## 🎥 Multimedia and Learning Features

- Image-based explanations  
- Concept visualisation  
- Structured educational content  
- Interactive UI components  

---

## 🛠️ Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript  

### Backend
- Flask  
- Flask-Login  
- Flask-WTF  
- Flask-Migrate  
- SQLAlchemy  

### Database
- SQLite  

---

## 🚀 How to Launch the Application

### 1. Clone the repository
```bash
git clone https://github.com/RoshiniVadla75/Group-22---CITS5206.git
cd Group-22---CITS5206
```

### 2. Create a virtual environment
MacOS/Linux
```bash
source venv/bin/activate
```

### 3. Activate environment
MacOS/Linux
```bash
source venv/bin/activate
```
Windows
```bash
venv\Scripts\activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run database migrations (first time only)
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Seed the database
```bash
python init_db.py
```

### 7. Run the application
```bash
python app.py
```

### 8. Open in browser
```bash
http://127.0.0.1:5000/
```

## 🧪 How to Run Tests

This project includes both **unit tests** and **Selenium tests**.

### 1. Install dependencies
Make sure all required packages are installed:

```bash
pip install -r requirements.txt
pip install pytest selenium
```

### 2. Run all tests
From the project root directory, run:

```bash
pytest
```

### 3. Run only unit tests
```bash
pytest tests/Unit
```

4. Run only Selenium tests
Before running Selenium tests, start the Flask application in a separate terminal:

```bash
python app.py
```

Then run:
```bash
pytest tests/Selenium
```
### Notes
	•	Run tests from the project root directory.
	•	Selenium tests require Chrome and ChromeDriver to be installed and working correctly.
	•	The Guided Tour, Home, Timeline, and Search Selenium tests depend on the application being available at http://127.0.0.1:5000.


## 🔐 Authentication

This project includes a user authentication system using **Flask-Login**.

### Features
- User registration  
- User login  
- Session management  
- Authentication-aware navigation  

> You may need to register a user before testing login features.

---

## 🔌 API Endpoints

The backend provides API routes for dynamic content:

- **GET /api/topics**  
  → Returns all topics  

- **GET /api/topics/<slug>**  
  → Returns a single topic  

These APIs are used by frontend JavaScript for dynamic rendering.

---

## 🧪 Database Notes

- Database is managed using **Flask-Migrate (Alembic)**  
- Initial data is seeded via `init_db.py`  

### Includes:
- 10 AI topics  
- Media (images)  
- References  
- WA context  

## 🗂️ Project Structure
```
GROUP-22---CITS5206/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   ├── auth.css
│   │   │   ├── explore-wa.css
│   │   │   ├── guided-tour.css
│   │   │   ├── home.css
│   │   │   ├── search.css
│   │   │   ├── timeline.css
│   │   │   └── topic-detail.css
│   │   └── js/
│   │       ├── explore-wa.js
│   │       ├── guided-tour.js
│   │       ├── home.js
│   │       ├── navbar.js
│   │       ├── search.js
│   │       ├── timeline.js
│   │       ├── topic_data.js
│   │       └── topic-detail.js
│   └── templates/
│       ├── explore_WA.html
│       ├── guided_tour.html
│       ├── home.html
│       ├── login.html
│       ├── search.html
│       ├── signup.html
│       ├── timeline.html
│       └── topic_detail.html
├── instance/
│   └── ai_museum.db
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── tests/
│   ├── Selenium/
│   │   ├── test_guided_tour.py
│   │   ├── test_home.py
│   │   ├── test_search.py
│   │   └── test_timeline.py
│   ├── Unit/
│   │   ├── test_app.py
│   │   ├── test_models.py
│   │   └── test_routes.py
│   └── conftest.py
├── .gitignore
├── app.py
├── init_db.py
├── models.py
├── README.md
├── requirements.txt
└── routes.py
```

## ✅ Features Implemented

- Full Flask backend  
- SQLite database integration  
- Flask-Migrate database version control  
- API-driven frontend  
- Timeline filtering system  
- Guided Tour system  
- Search functionality  
- Topic detail pages  
- User authentication  
- Responsive UI  
- Shared navigation system  

---

## 📄 License

This project is developed for academic purposes (CITS5206).

---

## ✨ Summary

The AI Museum – Western Australia demonstrates how complex artificial intelligence concepts can be transformed into an interactive digital museum experience.

By combining backend data, structured UI design, and educational storytelling, the system provides an engaging and accessible way to explore the evolution of AI.
