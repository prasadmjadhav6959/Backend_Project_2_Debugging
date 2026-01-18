# 📔 Sentiment Journal

A smart, AI-powered note-taking application with **real-time sentiment analysis** that helps you track your mood and emotional patterns over time.

![version](https://img.shields.io/badge/version-2.0-blue)
![python](https://img.shields.io/badge/python-3.8+-green)
![flask](https://img.shields.io/badge/flask-2.0+-lightgrey)
![license](https://img.shields.io/badge/license-MIT-orange)

---

## ✨ Overview

**Sentiment Journal** allows you to write daily notes while an AI model analyzes the emotional tone of each entry. Over time, the app helps you understand mood patterns using visual feedback and statistics.

---

## 🚀 Features

### 🐛 Bug Fixes (From Original Version)
- ✅ Fixed **Session Management** – Notes persist across page reloads  
- ✅ Proper **POST Handling** – Form submissions work reliably  
- ✅ **Input Validation** – Prevents blank or spam entries  
- ✅ **Session Security** – Encrypted using Flask secret key  
- ✅ Fully functional **Template System** with HTML  

---

### 🤖 New AI-Powered Features
- 🧠 **Real-time Sentiment Analysis** using NLP  
- 🎨 **Visual Mood Feedback** with color-coded notes  
- 📊 **Statistics Dashboard** to track emotional trends  
- ⏱ **Reverse Chronological Order** – Latest notes first  
- 📱 **Responsive Design** – Mobile & desktop friendly  

---

## 🎨 Sentiment Color Mapping

| Sentiment | Description | Color |
|---------|------------|-------|
| 🟢 Positive | Happy, excited, confident | Green |
| ⚪ Neutral | Balanced, calm, ordinary | Gray |
| 🔴 Negative | Sad, stressed, overwhelmed | Red |

---

## 📊 Sentiment Analysis Examples

| Your Note | Emotion Detected | Color |
|---------|----------------|-------|
| "I aced my exam! 🎉" | Positive (+0.62) | 🟢 Green |
| "Just another ordinary day" | Neutral (+0.03) | ⚪ Gray |
| "Feeling overwhelmed..." | Negative (-0.58) | 🔴 Red |

---

## 🧠 Backend Architecture

- **Framework:** Flask (Lightweight Python web framework)  
- **NLP Engine:** TextBlob (Built on NLTK)  
- **Session Storage:** Flask sessions with server-side encryption  
- **Data Persistence:** In-memory session storage  
  > ⚠️ *Upgrade to a database (SQLite/PostgreSQL) for production use*

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|-------|-------|------------|
| `/` | GET | Render main page with notes & statistics |
| `/` | POST | Add new note, analyze sentiment, update session |

---

## 📱 User Interface

### Dashboard Features
- ✍️ **Note Input Form** – Clean textarea with character counter  
- 📈 **Mood Statistics** – Real-time sentiment percentages  
- 🗂 **Note Display** – Color-coded cards with timestamps & scores  
- 📱 **Responsive UI** – Built with Bootstrap 5  

---

## 🎯 Color Psychology

- **Green (#dcfce7):** Calm, positive reinforcement  
- **Gray (#f3f4f6):** Neutral, balanced state  
- **Red (#fee2e2):** Alerting, encourages reflection  

---

## 📂 Project Structure

```
sentiment-journal/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html            # Main HTML template (Bootstrap)
├── static/                   # Optional CSS/JS files
├── README.md                 # Project documentation
└── .gitignore
```

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/sentiment-journal.git
cd sentiment-journal

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Open your browser and visit:
```
http://127.0.0.1:5000/
```

---

## 📝 Quick Tip

> ✨ Try writing notes at different times of the day to observe how your mood fluctuates!

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute.

---

## ❤️ Start Journaling!

Write your thoughts, reflect on your emotions, and let AI help you understand yourself better.
