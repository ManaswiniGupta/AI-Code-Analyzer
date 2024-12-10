# AI Code Analyzer

The **AI Code Analyzer** is a Flask-based web application that allows users to upload code files(supported files types are .cpp, .java, .txt, .py, .c) or paste code snippets for analysis. The app provides insights into potential bottlenecks, optimizations, and best practices to improve the quality of the submitted code.

## Features

- **File Upload**: Upload a code file for analysis.
- **Code Snippet Input**: Directly paste code snippets for immediate evaluation.
- **Code Analysis**: Identifies potential bottlenecks, suggests optimizations, and highlights best practices.
- **Syntax Highlighting**: Displays analyzed code snippets with syntax highlighting using [Highlight.js](https://highlightjs.org/).
- **User-Friendly Interface**: Responsive design for seamless use across devices.

---

## How It Works

1. **Upload or Paste Code**: Choose between uploading a file or pasting your code snippet directly into the provided text area.
2. **Analyze Code**: Click the "Analyze Code" button.
3. **View Results**: Get a detailed analysis of your code, including:
   - Potential bottlenecks.
   - Suggested optimizations.
   - Refactored code examples.

---

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Highlight.js for syntax highlighting.
- **Deployment**: [Render](https://ai-code-analyzer-app.onrender.com/) 

---
## Getting Started

### Prerequisites
- Python 3.10
- `pip` (Python package manager)
- A `.env` file containing necessary environment variables

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ManaswiniGupta/AI-Code-Analyzer.git
   cd AI-Code-Analyzer
2. **Install dependencies:** Use `pip` to install the required dependencies
    ```bash
    pip install -r requirements.txt
3. **Set up environment variables:**
  - Create a `.env` file in the root directory and add your environment variables, such as the API key.
    ```bash
    GROQ_API_KEY=your-api-key-here
    ```
  - Ensure `.env` is listed in .gitignore to keep it private.

### Running the Application
To start the Flask server, run the following command:
```bash
    flask run
```
    


The application will be available at `http://127.0.0.1:5000`.

## Running in Production
This application is configured to use Gunicorn for production environments. To run with Gunicorn:
```bash
  gunicorn app:app
```
## Deployment
This application can be deployed on Render. Be sure to include gunicorn in requirements.txt to ensure compatibility.

## Project Structure
- `app.py`: Main application file for Flask server setup and endpoints
- `templates/`: HTML templates for the web interface
- `static/`: Static files such as CSS for styling
- `requirements.txt`: Python dependencies
- `.env`: Contains environment variables (should be added to .gitignore)




