# AnalyzeQuestion - AI-Powered Coding Problem Analyzer

![AI-Powered](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=ai) ![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-green?style=for-the-badge&logo=fastapi) ![Ollama](https://img.shields.io/badge/Ollama-Mistral-informational?style=for-the-badge)

AnalyzeQuestion is an advanced AI-powered platform designed to help developers, students, and competitive programmers efficiently analyze and solve complex coding challenges using cutting-edge Retrieval-Augmented Generation (RAG) technology.

## 🚀 Features

- **🤖 RAG-Powered Analysis**: Uses retrieval-augmented generation for context-aware problem analysis
- **🎯 Pattern Detection**: Identifies algorithmic patterns and data structures efficiently
- **📊 Difficulty Assessment**: Accurately assesses problem difficulty based on historical data
- **📝 Step-by-Step Approach**: Provides detailed solution approaches tailored to each problem
- **🌙 Dark/Light Mode**: Beautiful, responsive UI with theme toggle functionality
- **💾 History Tracking**: Saves analyzed problems for future reference and RAG context

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **AI Processing**: Ollama with Mistral model
- **Database**: SQLite with RAG implementation
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Deployment**: Uvicorn ASGI server

## 🛠️ How to Use

Follow these steps to set up and run AnalyzeQuestion:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Yuvakunaal/AnalyzeQuestion.git
   cd AnalyzeQuestion (or) open vscode -> open this folder
   ```

2. **Download Ollama**

   - Visit the [Ollama website](https://ollama.ai) and download the application.
   - Open your terminal and run:
     ```bash
     ollama pull mistral:instruct
     ```
   - The Ollama model is now downloaded on your system.

3. **Create a Virtual Environment (venv)**

   - **For Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **For Mac/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**

   ```bash
   uvicorn app:app --reload
   ```

6. **Open Browser** : Navigate to http://127.0.0.1:8000/
7. Start using AnalyzeQuestion to analyze your coding problems!

## 🎯 How It Works

1. **Input Problem**: Paste your coding problem into the text area
2. **AI Analysis**: Our RAG system retrieves context from similar past problems
3. **Pattern Recognition**: The AI identifies relevant algorithms and data structures
4. **Solution Generation**: Step-by-step approach is generated with optimal efficiency
5. **Results Display**: Clean, organized presentation of patterns, difficulty, and approach

## 🔮 Usage Example

Input a coding problem like:
"Given an array of integers, find the maximum sum of a contiguous subarray."

Get analysis results:

- **Patterns**: Kadane's Algorithm, Dynamic Programming
- **Difficulty**: Medium
- **Approach**:
  1. Initialize variables to track current and maximum sum
  2. Iterate through the array, updating current sum
  3. Reset current sum if it becomes negative
  4. Update maximum sum when current sum is greater

## 🌟 Advanced Features

- **Retrieval-Augmented Generation**: Enhances AI responses with context from past problems
- **Adaptive Learning**: Improves over time as more problems are analyzed
- **Enterprise-Ready Architecture**: Scalable backend with efficient processing
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 👨‍💻 Developer

Kunaal - GenAI, AI, Python Enthusiast

## 🙏 Acknowledgments

- Ollama team for the excellent local LLM framework
- FastAPI for the high-performance web framework
- The open-source community for various libraries and tools
