# 🚀 LearnAI - AI Learning & Developer Productivity Tool

> Built for **AI for Bharat Hackathon 2026**

An AI-powered solution that helps people learn faster, work smarter, and become more productive while building or understanding technology.

![LearnAI Banner](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge) ![Flask](https://img.shields.io/badge/Flask-2.3-red?style=for-the-badge)

---

## 🎯 Problem Statement

Build an AI-powered solution that helps people:
- Learn faster with personalized tutoring
- Work smarter with developer productivity tools
- Understand complex code and concepts easily
- Organize and summarize knowledge effectively

---

## ✨ Features

### 🔍 **Code Explainer**
Paste any code and get a detailed, beginner-friendly explanation with:
- Step-by-step breakdown
- Key concepts identification
- Best practice suggestions
- Common mistakes to avoid

### 📚 **AI Tutor**
Learn any topic with personalized lessons based on:
- Your skill level (Beginner/Intermediate/Advanced)
- Your learning style (Visual/Practical/Theoretical/Storytelling)
- Interactive practice questions
- Structured lesson format

### 🐛 **Debug Helper**
Get help fixing errors with:
- Root cause analysis
- Corrected code with explanations
- Prevention tips
- Related concepts to learn

### 📝 **Documentation Generator**
Automatically generate professional documentation:
- Function/class documentation
- Usage examples
- API-style documentation
- Comprehensive or concise formats

### 📋 **Content Summarizer**
Condense long content into digestible summaries:
- Concise bullet points
- Detailed summaries
- ELI5 (Explain Like I'm 5)
- Actionable takeaways

### 🗺️ **Learning Path Generator**
Get a personalized roadmap to master any skill:
- Phased learning plan
- Recommended resources
- Practice projects
- Milestone checkpoints

### 💬 **AI Chat Assistant**
Interactive chat for learning and productivity:
- Ask questions about programming
- Get explanations and examples
- Continuous conversation context

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key (free)

### Installation

1. **Clone or download the project**
   ```bash
   cd AI_FOR_BHARAT
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your free Gemini API key**
   - Visit: https://makersuite.google.com/app/apikey
   - Create a new API key
   - Copy the key

4. **Configure the API key**
   - Open `.env` file
   - Replace `your_gemini_api_key_here` with your actual API key:
     ```
     GEMINI_API_KEY=AIzaSy...your_key_here
     ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   - Navigate to: http://localhost:5000

---

## 🎨 Screenshots

### Home Page
Modern, clean interface with all features accessible from the sidebar.

### Code Explainer
Paste code → Get detailed explanations with best practices.

### AI Tutor
Select topic, level, and learning style → Get personalized lessons.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Backend logic |
| **Flask** | Web framework |
| **Google Gemini AI** | AI/LLM capabilities |
| **HTML/CSS/JS** | Modern frontend |
| **Marked.js** | Markdown rendering |

---

## 📁 Project Structure

```
AI_FOR_BHARAT/
├── app.py              # Flask backend with AI features
├── requirements.txt    # Python dependencies
├── .env               # API key configuration
├── README.md          # Project documentation
└── templates/
    └── index.html     # Frontend UI
```

---

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/api/explain-code` | POST | Explain code |
| `/api/tutor` | POST | AI tutoring |
| `/api/debug` | POST | Debug helper |
| `/api/document` | POST | Generate docs |
| `/api/summarize` | POST | Summarize content |
| `/api/learning-path` | POST | Generate learning path |
| `/api/chat` | POST | Chat with AI |
| `/api/clear-chat` | POST | Clear chat history |
| `/api/health` | GET | Health check |

---

## 🌟 Why LearnAI?

1. **All-in-One Solution**: Multiple learning and productivity tools in one place
2. **Personalized Learning**: Adapts to your level and learning style
3. **Developer-Focused**: Built by developers, for developers
4. **Free & Open**: Uses free Gemini API, fully open source
5. **Modern UI**: Clean, intuitive interface
6. **Beginner-Friendly**: Makes complex concepts easy to understand

---

## 🔮 Future Enhancements

- [ ] User accounts and learning progress tracking
- [ ] Code execution sandbox
- [ ] Spaced repetition for learning
- [ ] Integration with GitHub for codebase analysis
- [ ] Voice-based tutoring
- [ ] Mobile app

---

## 👥 Team

Built with ❤️ for **AI for Bharat Hackathon 2026**

---

## 📄 License

MIT License - Feel free to use, modify, and distribute!

---

## 🙏 Acknowledgments

- Google Gemini AI for powerful LLM capabilities
- The open source community
- AI for Bharat Hackathon organizers

---

**Made in India 🇮🇳 for the World 🌍**
