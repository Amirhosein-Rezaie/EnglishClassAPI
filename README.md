# 📘 EnglishClass

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/Django-4.x-darkgreen?logo=django&logoColor=white)](https://www.djangoproject.com/) 
[![DRF](https://img.shields.io/badge/DRF-API-red?logo=django&logoColor=white)](https://www.django-rest-framework.org/) 
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-blue?logo=postgresql)](https://www.postgresql.org/)  

<p>
  <img src="https://skillicons.dev/icons?i=python,django,git,github,windows,vscode,postman,postgres">
</p>

## 📖 Description
**EnglishClass** is a mini project developed with **Django** and **Django REST Framework (DRF)**.  
It provides APIs to manage **classes, students, and teachers**, supports **reporting**, and allows exporting reports to **Excel files**.  

🔑 Key points:
- Backend built with **Django** + **DRF**  
- API documentation generated with **drf-spectacular**  
- **JWT authentication system** for secure access  

---

## ✨ Features
- 📚 Manage **Classes, Students, Teachers, Books, Levels, Terms**
- 🎬 You can do **Trade books, set grades for students, set point or score for teachers, set profiles of people**
- 📊 Generate detailed **Reports**  
- 📑 Export reports to **Excel**  
- 🔐 Secure authentication with **JWT**  
- 📖 Auto-generated API docs with **drf-spectacular**  

---

## 🛠️ Requirements
- **Python 3.9+**  
- **PostgreSQL** (running locally or remote)  
- Virtual environment tool: `venv`

---

## ⚙️ Installation & Usage
```bash
1️⃣ Clone the repository
`git clone https://github.com/YourUserName/EnglishClassAPI.git`
`cd EnglishClassAPI`

2️⃣ Create a virtual environment
`python -m venv .venv`
# Activate:
source `.venv/bin/activate`   # Linux/Mac
`.venv\Scripts\activate`     # Windows

3️⃣ Install dependencies
`pip install -r requirements.txt`

4️⃣ Apply migrations
`python manage.py makemigrations`
`python manage.py migrate`

5️⃣ Run the server
`python manage.py runserver`

6️⃣ use documents
after running the server open your browser and go to `http://127.0.0.1:8000/api/docs`
```
