# backend/main.py

from flask import Flask, request, jsonify
import openai, os
import json

# create app instance
app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

# Endpoint for /analyze
@app.route('/analyze', methods=['POST'])
def analyze_file():
    # read incoming JSON data
    data = request.json
    # extract content from the data, if available
    content = data.get('content', '')
    prompt = f"""You are a file assistant. Suggest a filename and folder:
    
    Content:
    {content}

    Reply in JSON: {{ "filename": "name.py", "folder": "PythonScripts" }}
    """

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    msg = res.choices[0].message['content']
    # parse the response and return it as JSON
    return jsonify(json.loads(msg))

if __name__ == '__main__':
    app.run(port=5000)