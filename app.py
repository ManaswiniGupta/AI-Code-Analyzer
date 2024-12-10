import os
import json
import markdown
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from flask import Flask, render_template, request, jsonify
from markdown.extensions.codehilite import CodeHiliteExtension  # Highlight code
from markdown.extensions.fenced_code import FencedCodeExtension  

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the uploads directory exists



# Load environment variables
load_dotenv()
GROQ_API_KEY= os.getenv('GROQ_API_KEY')

# Defining LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)




def extract_text_from_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension not in ['.cpp', '.java', '.txt', '.py', '.c']:
        raise ValueError(f"Unsupported file type: {file_extension}")
    elif file_extension in ['.cpp', '.java', '.txt', '.py', '.c']:
        with open(file_path, 'r' , encoding='utf-8') as file:
            return file.read()
    else:
        raise ValueError("Unsupported file type")



def analyze_code(code_snippet):
    """
    Analyze the code snippet and return potential bottlenecks and optimization suggestions.
    """
    if code_snippet:
        # Send the code snippet to an AI model for analysis
        prompt = (
        f"You are an AI assistant that analyzes code for performance issues."
        f"Identify potential bottlenecks in the following code and provide optimization suggestions:"
        
        f"""Code:
        {code_snippet}
        
        Please return a concise analysis and actionable suggestions.
        """
        )
        messages= [
        ("system", "You are a helpful ai coding assistant that analyze the code snippet and return potential bottlenecks and optimization suggestions."),
        ("human", prompt),
        ]
    
        # Assuming 'llm.invoke' generates the response from the model
        ai_msg = llm.invoke(messages)

    
    # Output from the model should contain both title and bio
    try:
        return "Code Analysis", ai_msg.content        
        
    except Exception as e:
        return "Error:", e
        



@app.route("/", methods=["GET", "POST"])
def index():
    analysis_result = None
    error_message = None

    if request.method == "POST":
        code_snippet = None

        # Check if a file was uploaded
        code_file = request.files.get("code_file")
        if code_file and code_file.filename:
            # Handle file upload
            file_path = os.path.join(UPLOAD_FOLDER, code_file.filename)
            code_file.save(file_path)
            try:
                code_snippet = extract_text_from_file(file_path)
            except Exception as e:
                error_message = f"Error processing file: {e}"

        # Check if a code snippet was pasted
        elif request.form.get("code_snippet"):
            code_snippet = request.form["code_snippet"].strip()

        # Handle cases with no input
        if not code_snippet:
            error_message = "Please upload a file or paste a code snippet."
        else:
            try:
                analysis_result_tuple = analyze_code(code_snippet)
                if analysis_result_tuple and isinstance(analysis_result_tuple, tuple):
                    # Render Markdown with syntax highlighting
                    md_content = analysis_result_tuple[1]
                    analysis_result = markdown.markdown(
                        md_content,
                        extensions=[
                            CodeHiliteExtension(linenums=True, css_class="highlight"),
                            FencedCodeExtension(),
                        ],
                    )
                else:
                    error_message = "Unexpected analysis result format."
            except Exception as e:
                error_message = f"Error analyzing code: {e}"

    return render_template(
        "index.html",
        analysis_result=analysis_result,
        error_message=error_message,
    )




if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

