# Group-22---CITS5206  
Information Technology Capstone Project  

# 🏛️ AI Museum – Western Australia  
*A Virtual Museum of A.I. Software Technology*

## 📌 Project Overview
The **AI Museum – Western Australia** is a full-stack web application designed to present the history of artificial intelligence software technologies through an interactive virtual museum experience.

The system enables users to explore **10 major paradigm shifts in AI (1950–present)** through guided exhibits, multimedia content, search functionality, and educational storytelling.

This project transforms complex AI concepts into an engaging and accessible learning experience, with a focus on Western Australian contributions to computing history.

## 👥 Team Members
| Name                   | Student ID | GitHub Username |
|------------------------|------------|-----------------|
| Roshini Vadla          | 24324533   | RoshiniVadla75  |
| Weiyu Xu               | 24233679   | Hannah-X0206    |
| Shanin Rashid          | 24117314   | kdmars0168      |
| Noah Ning              | 24120321   | NingNoah        |
| Xi Qin                 | 24235608   | xiqin2049       |

## 🎯 Purpose
- Provide an interactive museum-style learning experience  
- Present historical and modern AI developments  
- Highlight Western Australia’s contributions  
- Support visual, multimedia-based education  

## 🧠 10 AI Paradigm Shifts Covered
1. Turing’s AI Foundations (1950)  
2. Learning Machines (1960s)  
3. Game Playing Systems (1960–1970)  
4. Expert Systems (1980s)  
5. Artificial Neural Networks & Deep Learning (1980–2000)  
6. Internet-Driven AI & Knowledge Systems (2010)  
7. Evolutionary Computing & Genetic Algorithms (2010)  
8. Synthetic Media Generation (Deepfakes) (2015)  
9. Natural Language Processing (NLP) (2010–2020)  
10. Large Language Models (LLMs) (2020–Present)  

## 🧭 Application Pages
### 🏠 Home Page
- Entry point of the virtual museum  
- Introduces project purpose and navigation  
- Establishes immersive user experience  

### ⏳ Timeline
- Displays AI evolution chronologically  
- Connects technologies across decades  
- Supports structured learning  

### 🌏 Explore WA
- Highlights Western Australian contributions  
- Connects global developments with local context  
- Includes institutions and research milestones  

### 🧭 Guided Tour
- Structured exploration of AI technologies  
- Presents each paradigm as an exhibit  
- Includes explanations, examples, and multimedia  

### 🔍 Search
- Archive-style search system  
- Filter by topics, media, and references  
- Enables independent exploration  

## 🎥 Multimedia and Visual Learning
- Images and conceptual diagrams  
- Educational videos  
- Data visualisation using Chart.js  
- Interactive exhibit elements  

## 🛠️ Tech Stack
### Frontend
- HTML5  
- CSS / TailwindCSS  
- JavaScript  
- jQuery  

### Backend
- Flask  
- SQLAlchemy  
- Flask-WTF  
- Flask-Login  

### Database
- SQLite  

### Visualisation
- Chart.js  

## 🚀 How to Run
### 1. Clone Repository
git clone https://github.com/RoshiniVadla75/Group-22---CITS5206.git  
cd Group-22---CITS5206  

### 2. Create Virtual Environment
python -m venv venv  

### 3. Activate Environment
Mac/Linux:  
source venv/bin/activate  

Windows:  
venv\Scripts\activate  

### 4. Install Dependencies
pip install -r requirements.txt  

### 5. Initialise Database
python init_db.py  

### 6. Run Application
flask run  

### 7. Open in Browser
http://localhost:5050/  

## 📁 Project Structure
Group-22---CITS5206/  
│  
├── static/  
│   ├── css/  
│   ├── js/  
│   └── images/  
│  
├── templates/  
│  
├── app.py  
├── models.py  
├── routes.py  
├── init_db.py  
├── requirements.txt  
└── README.md  

## 📄 License
This project is developed for academic purposes (CITS5206).

## ✨ Summary
The AI Museum demonstrates how complex artificial intelligence concepts can be transformed into an interactive digital learning experience, combining history, technology, and user engagement.