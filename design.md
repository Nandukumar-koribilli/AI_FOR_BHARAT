# 🎨 Design Document

## LearnAI - AI Learning & Developer Productivity Tool
**AI for Bharat Hackathon 2026**

---

## 1. System Architecture

### 1.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         CLIENT (Browser)                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Frontend (HTML/CSS/JS)                │   │
│  │  • Modern Dark Theme UI                                  │   │
│  │  • Sidebar Navigation                                    │   │
│  │  • Feature Panels                                        │   │
│  │  • Markdown Rendering (Marked.js)                        │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                               │
                               │ HTTP/REST API
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SERVER (Flask Backend)                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                     API Routes                           │   │
│  │  • /api/explain-code    • /api/tutor                     │   │
│  │  • /api/debug           • /api/document                  │   │
│  │  • /api/summarize       • /api/learning-path             │   │
│  │  • /api/chat            • /api/health                    │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   AI Feature Handlers                    │   │
│  │  • explain_code()       • tutor_topic()                  │   │
│  │  • debug_helper()       • generate_documentation()       │   │
│  │  • summarize_content()  • create_learning_path()         │   │
│  │  • chat_assistant()                                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    AI Client Layer                       │   │
│  │  • get_ai_client()      • generate_with_retry()          │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                               │
                               │ OpenAI-Compatible API
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      AI PROVIDER (Groq)                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              LLM: llama-3.3-70b-versatile                │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Component Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                        LearnAI System                         │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────┐    ┌────────────────┐    ┌────────────┐ │
│  │   Presentation │    │    Business    │    │    Data    │ │
│  │      Layer     │◄──►│     Layer      │◄──►│   Layer    │ │
│  └────────────────┘    └────────────────┘    └────────────┘ │
│         │                     │                    │        │
│         ▼                     ▼                    ▼        │
│  ┌────────────────┐    ┌────────────────┐    ┌────────────┐ │
│  │ • index.html   │    │ • Flask Routes │    │ • Groq API │ │
│  │ • CSS Styles   │    │ • AI Handlers  │    │ • .env     │ │
│  │ • JavaScript   │    │ • Retry Logic  │    │ • Sessions │ │
│  └────────────────┘    └────────────────┘    └────────────┘ │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 2. Data Flow

### 2.1 Request Flow

```
User Input ──► Frontend ──► API Request ──► Flask Route ──► AI Handler
                                                               │
                                                               ▼
User Display ◄── Frontend ◄── API Response ◄── Flask Route ◄── LLM Response
```

### 2.2 Sequence Diagram (Code Explainer Example)

```
┌──────┐          ┌──────────┐          ┌─────────┐          ┌──────┐
│ User │          │ Frontend │          │ Backend │          │ Groq │
└──┬───┘          └────┬─────┘          └────┬────┘          └──┬───┘
   │                   │                     │                  │
   │ 1. Paste code     │                     │                  │
   │──────────────────►│                     │                  │
   │                   │                     │                  │
   │ 2. Click Explain  │                     │                  │
   │──────────────────►│                     │                  │
   │                   │                     │                  │
   │                   │ 3. POST /api/       │                  │
   │                   │    explain-code     │                  │
   │                   │────────────────────►│                  │
   │                   │                     │                  │
   │                   │                     │ 4. Generate      │
   │                   │                     │    Content       │
   │                   │                     │─────────────────►│
   │                   │                     │                  │
   │                   │                     │ 5. LLM Response  │
   │                   │                     │◄─────────────────│
   │                   │                     │                  │
   │                   │ 6. JSON Response    │                  │
   │                   │◄────────────────────│                  │
   │                   │                     │                  │
   │ 7. Render         │                     │                  │
   │    Markdown       │                     │                  │
   │◄──────────────────│                     │                  │
   │                   │                     │                  │
```

---

## 3. UI/UX Design

### 3.1 Design Principles
- **Dark Theme**: Reduces eye strain for developers
- **Minimalist**: Clean interface without clutter
- **Intuitive Navigation**: Sidebar for quick feature access
- **Responsive**: Works on desktop, tablet, and mobile
- **Consistent**: Unified design language across features

### 3.2 Color Palette

| Color | Hex Code | Usage |
|-------|----------|-------|
| Primary | `#6366f1` | Buttons, highlights, accents |
| Primary Dark | `#4f46e5` | Hover states |
| Secondary | `#10b981` | Success states, user avatars |
| Accent | `#f59e0b` | Warnings |
| Background Dark | `#0f172a` | Main background |
| Card Background | `#1e293b` | Cards, panels |
| Input Background | `#334155` | Form inputs |
| Text Primary | `#f1f5f9` | Main text |
| Text Secondary | `#94a3b8` | Muted text |
| Border | `#475569` | Borders, dividers |
| Success | `#22c55e` | Success messages |
| Error | `#ef4444` | Error messages |

### 3.3 Typography

| Element | Font | Weight | Size |
|---------|------|--------|------|
| Body | Inter | 400 | 16px |
| Headings | Inter | 600-700 | 24-40px |
| Code | Fira Code | 400-500 | 14px |
| Labels | Inter | 500 | 14px |

### 3.4 Layout Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                           HEADER                                 │
│  ┌─────────────┐                              ┌───────────────┐ │
│  │    Logo     │                              │    Badge      │ │
│  └─────────────┘                              └───────────────┘ │
├─────────────────────────────────────────────────────────────────┤
│          │                                                      │
│          │                                                      │
│  ┌───────┴───────┐    ┌─────────────────────────────────────┐  │
│  │               │    │                                     │  │
│  │   SIDEBAR     │    │           CONTENT AREA              │  │
│  │               │    │                                     │  │
│  │  • Home       │    │   ┌─────────────────────────────┐   │  │
│  │  • Explainer  │    │   │      Feature Panel          │   │  │
│  │  • Tutor      │    │   │                             │   │  │
│  │  • Debug      │    │   │   • Input Form              │   │  │
│  │  • Docs       │    │   │   • Options                 │   │  │
│  │  • Summarize  │    │   │   • Submit Button           │   │  │
│  │  • Path       │    │   │                             │   │  │
│  │  • Chat       │    │   └─────────────────────────────┘   │  │
│  │               │    │                                     │  │
│  │               │    │   ┌─────────────────────────────┐   │  │
│  │               │    │   │      Result Area            │   │  │
│  │               │    │   │                             │   │  │
│  │               │    │   │   • Rendered Markdown       │   │  │
│  │               │    │   │   • Copy Button             │   │  │
│  │               │    │   │                             │   │  │
│  │               │    │   └─────────────────────────────┘   │  │
│  │               │    │                                     │  │
│  └───────────────┘    └─────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.5 Component Library

| Component | Description |
|-----------|-------------|
| `.card` | Container with rounded corners and subtle border |
| `.btn-primary` | Gradient button with hover animation |
| `.btn-secondary` | Subtle button for secondary actions |
| `.option-card` | Selectable card for options (level, style) |
| `.result-area` | Container for AI-generated content |
| `.nav-item` | Sidebar navigation item |
| `.message` | Chat message bubble |
| `.loading` | Loading spinner with text |

---

## 4. API Design

### 4.1 REST Endpoints

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/` | Serve main page | - |
| POST | `/api/explain-code` | Explain code | `{code, language}` |
| POST | `/api/tutor` | AI tutoring | `{topic, level, learning_style}` |
| POST | `/api/debug` | Debug helper | `{code, error_message}` |
| POST | `/api/document` | Generate docs | `{code, doc_style}` |
| POST | `/api/summarize` | Summarize content | `{content, summary_type}` |
| POST | `/api/learning-path` | Learning roadmap | `{goal, current_level, time_available}` |
| POST | `/api/chat` | Chat assistant | `{message, context}` |
| POST | `/api/clear-chat` | Clear chat history | - |
| GET | `/api/health` | Health check | - |

### 4.2 Response Format

```json
// Success Response
{
  "success": true,
  "explanation": "... markdown content ...",
  // or "lesson", "solution", "documentation", "summary", "learning_path", "response"
}

// Error Response
{
  "success": false,
  "error": "Error message here"
}

// Health Check Response
{
  "status": "healthy",
  "api_configured": true,
  "timestamp": "2026-01-21T10:30:00"
}
```

---

## 5. Error Handling Design

### 5.1 Error Types

| Error Type | HTTP Code | Handling |
|------------|-----------|----------|
| Missing Input | 400 | Return validation error |
| API Key Missing | 500 | Return configuration error |
| Rate Limit | 429 | Retry with exponential backoff |
| API Error | 500 | Return user-friendly message |
| Network Error | 500 | Display connection error |

### 5.2 Retry Logic

```python
def generate_with_retry(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            return api_call(prompt)
        except RateLimitError:
            wait_time = (attempt + 1) * 5  # 5s, 10s, 15s
            time.sleep(wait_time)
    raise Exception("Max retries exceeded")
```

---

## 6. Security Design

### 6.1 Security Measures

| Measure | Implementation |
|---------|----------------|
| API Key Storage | Environment variables (.env) |
| CORS | Flask-CORS with appropriate headers |
| Input Validation | Server-side validation of all inputs |
| No Data Persistence | Chat history in-memory only |
| HTTPS | Recommended for production |

### 6.2 Environment Variables

```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx
```

---

## 7. Scalability Considerations

### 7.1 Current Design (MVP)
- Single server architecture
- In-memory session storage
- Direct API calls to LLM provider

### 7.2 Future Scalability

```
                    ┌─────────────┐
                    │   Load      │
                    │  Balancer   │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
     ┌─────┴─────┐   ┌─────┴─────┐   ┌─────┴─────┐
     │  Server 1 │   │  Server 2 │   │  Server 3 │
     └─────┬─────┘   └─────┬─────┘   └─────┬─────┘
           │               │               │
           └───────────────┼───────────────┘
                           │
                    ┌──────┴──────┐
                    │    Redis    │
                    │   (Cache)   │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │  Database   │
                    │ (PostgreSQL)│
                    └─────────────┘
```

---

## 8. File Structure

```
AI_FOR_BHARAT/
├── app.py                 # Main Flask application
│   ├── Configuration      # API key, model setup
│   ├── AI Client          # Groq client initialization
│   ├── Feature Handlers   # 7 AI feature functions
│   ├── API Routes         # REST endpoints
│   └── Main Entry         # Server startup
│
├── templates/
│   └── index.html         # Single-page frontend
│       ├── <style>        # CSS styles (embedded)
│       └── <script>       # JavaScript (embedded)
│
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
├── requirements.md        # Requirements document
├── design.md             # Design document (this file)
└── README.md             # Project overview
```

---

## 9. Technology Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Backend Framework | Flask | Lightweight, easy to deploy |
| AI Provider | Groq | Free tier, fast inference |
| AI Model | Llama 3.3 70B | High quality, versatile |
| API Client | OpenAI SDK | Standard, works with multiple providers |
| Frontend | Vanilla HTML/CSS/JS | No build step, simple deployment |
| Markdown | Marked.js | Fast, reliable rendering |
| Icons | Font Awesome | Comprehensive icon library |
| Fonts | Inter, Fira Code | Modern, readable |

---

## 10. Testing Strategy

| Test Type | Scope | Tools |
|-----------|-------|-------|
| Manual Testing | UI, UX, Features | Browser |
| API Testing | Endpoints | Postman, curl |
| Error Testing | Edge cases, failures | Manual |
| Performance | Response times | Browser DevTools |

---

*Document Version: 1.0*  
*Last Updated: January 21, 2026*
