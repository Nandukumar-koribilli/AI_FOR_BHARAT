"""
AI Learning & Developer Productivity Tool
Built for AI for Bharat Hackathon 2026

A comprehensive AI-powered solution that helps people:
- Learn faster with personalized tutoring
- Understand complex code and concepts
- Improve developer productivity
- Organize and summarize knowledge
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from datetime import datetime
import time

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Groq AI (Free tier with generous limits)
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')

def get_ai_client():
    """Initialize and return Groq AI client"""
    if not GROQ_API_KEY:
        return None
    return OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

def generate_with_retry(prompt, max_retries=3):
    """Generate content with retry logic for rate limits"""
    client = get_ai_client()
    if not client:
        return None
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            error_str = str(e)
            if '429' in error_str or 'rate' in error_str.lower():
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 5
                    time.sleep(wait_time)
                    continue
            raise e
    return None

# Store learning sessions (in production, use a database)
learning_sessions = {}
chat_history = []

# ============== AI FEATURE HANDLERS ==============

def explain_code(code, language="auto"):
    """Explain code in simple terms with line-by-line breakdown"""
    if not GROQ_API_KEY:
        return {"error": "API key not configured. Please add GROQ_API_KEY to .env file"}
    
    prompt = f"""You are an expert programming tutor. Explain the following code in a clear, beginner-friendly way.

**Code ({language}):**
```
{code}
```

Provide:
1. **Overview**: What does this code do overall? (2-3 sentences)
2. **Step-by-Step Breakdown**: Explain each important section
3. **Key Concepts**: List any programming concepts used (with brief explanations)
4. **Potential Improvements**: Suggest any improvements or best practices
5. **Common Mistakes**: What mistakes might beginners make with similar code?

Use simple language and analogies where helpful. Format your response in Markdown."""

    try:
        response = generate_with_retry(prompt)
        return {"explanation": response, "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


def tutor_topic(topic, level="beginner", learning_style="visual"):
    """Provide personalized tutoring on any topic"""
    if not GROQ_API_KEY:
        return {"error": "API key not configured. Please add GROQ_API_KEY to .env file"}
    
    style_instructions = {
        "visual": "Use diagrams descriptions, flowcharts, and visual analogies. Include ASCII art where helpful.",
        "practical": "Focus on hands-on examples, real-world applications, and coding exercises.",
        "theoretical": "Emphasize underlying principles, mathematical foundations, and academic concepts.",
        "storytelling": "Teach through stories, real-world scenarios, and relatable examples."
    }
    
    level_instructions = {
        "beginner": "Assume no prior knowledge. Use simple words and lots of examples.",
        "intermediate": "Assume basic understanding. Build on fundamentals with more depth.",
        "advanced": "Assume strong foundation. Focus on nuances, edge cases, and expert techniques."
    }
    
    prompt = f"""You are a world-class tutor specialized in adaptive learning. Teach the following topic:

**Topic**: {topic}
**Student Level**: {level}
**Learning Style**: {learning_style}

{level_instructions.get(level, level_instructions['beginner'])}
{style_instructions.get(learning_style, style_instructions['visual'])}

Structure your lesson as:
1. **Introduction** (Hook the learner with why this matters)
2. **Core Concepts** (Main ideas explained clearly)
3. **Examples** (At least 2-3 practical examples)
4. **Practice Questions** (3 questions to test understanding, with answers hidden in spoiler format)
5. **Summary** (Key takeaways in bullet points)
6. **Next Steps** (What to learn next)

Make it engaging and memorable! Use emojis sparingly to add personality. Format in Markdown."""

    try:
        response = generate_with_retry(prompt)
        return {"lesson": response, "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


def summarize_content(content, summary_type="concise"):
    """Summarize documentation, articles, or any text"""
    if not GROQ_API_KEY:
        return {"error": "API key not configured. Please add GROQ_API_KEY to .env file"}
    
    summary_instructions = {
        "concise": "Create a brief 3-5 bullet point summary capturing the essence.",
        "detailed": "Create a comprehensive summary with all key points preserved.",
        "eli5": "Explain it like I'm 5 years old - use simple words and fun analogies.",
        "actionable": "Focus on action items, steps to follow, and practical takeaways.",
        "technical": "Preserve technical accuracy while making it more digestible."
    }
    
    prompt = f"""Summarize the following content:

**Content:**
{content}

**Summary Style:** {summary_type}
{summary_instructions.get(summary_type, summary_instructions['concise'])}

Provide:
1. **Summary** (in the requested style)
2. **Key Points** (bullet list of most important facts)
3. **Keywords** (important terms to remember)

Format in Markdown."""

    try:
        response = generate_with_retry(prompt)
        return {"summary": response, "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


def debug_helper(code, error_message, language="auto"):
    """Help debug code and explain errors"""
    if not GROQ_API_KEY:
        return {"error": "API key not configured. Please add GROQ_API_KEY to .env file"}
    
    prompt = f"""You are an expert debugging assistant. Help fix this code issue.

**Code ({language}):**
```
{code}
```

**Error/Problem:**
{error_message}

Provide:
1. **Problem Identification**: What exactly is wrong?
2. **Root Cause**: Why is this happening? Explain the underlying issue.
3. **Solution**: Show the corrected code with explanations
4. **Prevention Tips**: How to avoid similar issues in the future
5. **Related Concepts**: What should the developer learn to understand this better?

Be encouraging and educational. Format in Markdown."""

    try:
        response = generate_with_retry(prompt)
        return {"solution": response, "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


def generate_documentation(code, doc_style="comprehensive"):
    """Generate documentation for code"""
    if not GROQ_API_KEY:
        return {"error": "API key not configured. Please add GROQ_API_KEY to .env file"}
    
    prompt = f"""Generate professional documentation for this code:

**Code:**
```
{code}
```

**Documentation Style:** {doc_style}

Create:
1. **Overview**: What does this code do?
2. **Function/Class Documentation**: Document each function/class with:
   - Purpose
   - Parameters (with types and descriptions)
   - Return values
   - Example usage
3. **Dependencies**: What does this code depend on?
4. **Usage Examples**: Show how to use this code
5. **Notes**: Any important considerations

Format as proper documentation (use docstring format where appropriate). Output in Markdown."""

    try:
        response = generate_with_retry(prompt)
        return {"documentation": response, "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


def chat_assistant(message, context="general"):
    """Interactive AI chat for learning and productivity"""
    global chat_history
    if not GROQ_API_KEY:
        return {"error": "API key not configured. Please add GROQ_API_KEY to .env file"}
    
    # Build conversation context
    history_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history[-10:]])
    
    system_prompt = """You are an AI learning assistant and developer productivity helper. 
You help users:
- Learn programming concepts and technologies
- Understand and debug code
- Improve their productivity
- Explain complex topics simply

Be friendly, encouraging, and thorough. Use examples when helpful.
If the user asks something you're unsure about, be honest and suggest resources.
Keep responses focused and actionable."""

    prompt = f"""{system_prompt}

**Recent Conversation:**
{history_text}

**User's Message:**
{message}

**Context:** {context}

Respond helpfully in Markdown format."""

    try:
        response = generate_with_retry(prompt)
        
        # Update chat history
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": response})
        
        return {"response": response, "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


def create_learning_path(goal, current_level="beginner", time_available="1 month"):
    """Generate a personalized learning path"""
    if not GROQ_API_KEY:
        return {"error": "API key not configured. Please add GROQ_API_KEY to .env file"}
    
    prompt = f"""Create a personalized learning path:

**Learning Goal:** {goal}
**Current Level:** {current_level}
**Time Available:** {time_available}

Create a structured learning path with:
1. **Prerequisites**: What should they know first?
2. **Learning Phases**: Break down into phases/weeks
3. **For Each Phase**:
   - Topics to cover
   - Recommended resources (be specific)
   - Practice projects
   - Milestones to achieve
4. **Assessment Checkpoints**: How to know they're progressing
5. **Tips for Success**: Study strategies and motivation tips
6. **Common Pitfalls**: What to avoid

Make it realistic and actionable. Format in Markdown with clear organization."""

    try:
        response = generate_with_retry(prompt)
        return {"learning_path": response, "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


# ============== ROUTES ==============

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/explain-code', methods=['POST'])
def api_explain_code():
    data = request.json
    code = data.get('code', '')
    language = data.get('language', 'auto')
    
    if not code:
        return jsonify({"error": "No code provided"}), 400
    
    result = explain_code(code, language)
    return jsonify(result)


@app.route('/api/tutor', methods=['POST'])
def api_tutor():
    data = request.json
    topic = data.get('topic', '')
    level = data.get('level', 'beginner')
    learning_style = data.get('learning_style', 'visual')
    
    if not topic:
        return jsonify({"error": "No topic provided"}), 400
    
    result = tutor_topic(topic, level, learning_style)
    return jsonify(result)


@app.route('/api/summarize', methods=['POST'])
def api_summarize():
    data = request.json
    content = data.get('content', '')
    summary_type = data.get('summary_type', 'concise')
    
    if not content:
        return jsonify({"error": "No content provided"}), 400
    
    result = summarize_content(content, summary_type)
    return jsonify(result)


@app.route('/api/debug', methods=['POST'])
def api_debug():
    data = request.json
    code = data.get('code', '')
    error_message = data.get('error_message', '')
    language = data.get('language', 'auto')
    
    if not code or not error_message:
        return jsonify({"error": "Code and error message required"}), 400
    
    result = debug_helper(code, error_message, language)
    return jsonify(result)


@app.route('/api/document', methods=['POST'])
def api_document():
    data = request.json
    code = data.get('code', '')
    doc_style = data.get('doc_style', 'comprehensive')
    
    if not code:
        return jsonify({"error": "No code provided"}), 400
    
    result = generate_documentation(code, doc_style)
    return jsonify(result)


@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.json
    message = data.get('message', '')
    context = data.get('context', 'general')
    
    if not message:
        return jsonify({"error": "No message provided"}), 400
    
    result = chat_assistant(message, context)
    return jsonify(result)


@app.route('/api/learning-path', methods=['POST'])
def api_learning_path():
    data = request.json
    goal = data.get('goal', '')
    current_level = data.get('current_level', 'beginner')
    time_available = data.get('time_available', '1 month')
    
    if not goal:
        return jsonify({"error": "No learning goal provided"}), 400
    
    result = create_learning_path(goal, current_level, time_available)
    return jsonify(result)


@app.route('/api/clear-chat', methods=['POST'])
def api_clear_chat():
    global chat_history
    chat_history = []
    return jsonify({"success": True, "message": "Chat history cleared"})


@app.route('/api/health', methods=['GET'])
def health_check():
    api_configured = bool(GROQ_API_KEY)
    return jsonify({
        "status": "healthy",
        "api_configured": api_configured,
        "timestamp": datetime.now().isoformat()
    })


if __name__ == '__main__':
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║         AI Learning & Developer Productivity Tool            ║
    ║              Built for AI for Bharat Hackathon               ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  Features:                                                   ║
    ║  • Code Explainer - Understand any code instantly            ║
    ║  • AI Tutor - Learn any topic with personalized lessons      ║
    ║  • Debug Helper - Fix errors with detailed explanations      ║
    ║  • Doc Generator - Auto-generate documentation               ║
    ║  • Summarizer - Condense complex content                     ║
    ║  • Learning Paths - Get structured learning roadmaps         ║
    ║  • AI Chat - Interactive learning assistant                  ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    if not GROQ_API_KEY:
        print("⚠️  Warning: GROQ_API_KEY not set in .env file")
        print("   Get your FREE API key from: https://console.groq.com/keys")
        print("   Add it to .env file as: GROQ_API_KEY=your_key_here\n")
    
    print("🚀 Starting server at http://localhost:5000")
    app.run(debug=True, port=5000)
