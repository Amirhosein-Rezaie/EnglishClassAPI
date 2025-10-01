# 📘 EnglishClass

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/Django-4.x-darkgreen?logo=django&logoColor=white)](https://www.djangoproject.com/) 
[![DRF](https://img.shields.io/badge/DRF-API-red?logo=django&logoColor=white)](https://www.django-rest-framework.org/) 
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-DB-blue?logo=postgresql)](https://www.postgresql.org/)  

---

## 📖 Description
**EnglishClass** is a mini project developed with **Django** and **Django REST Framework (DRF)**.  
It provides APIs to manage **classes, students, and teachers**, supports **reporting**, and allows exporting reports to **Excel files**.  

🔑 Key points:
- Backend built with **Django** + **DRF**  
- API documentation generated with **drf-spectacular**  
- **JWT authentication system** for secure access  

---

## ✨ Features
- 📚 Manage **Classes, Students, Teachers**  
- 📊 Generate detailed **Reports**  
- 📑 Export reports to **Excel**  
- 🔐 Secure authentication with **JWT**  
- 📖 Auto-generated API docs with **drf-spectacular**  

---

## 🛠️ Requirements
- **Python 3.9+**  
- **PostgreSQL** (running locally or remote)  
- Virtual environment tool: `venv` / `pipenv` / `poetry`  

---

## ⚙️ Installation & Usage

```bash
1️⃣ Clone the repository
git clone https://github.com/YourUserName/EnglishClass.git
cd EnglishClass

2️⃣ Create a virtual environment
python -m venv .venv
# Activate:
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run the server
python manage.py runserver
```
