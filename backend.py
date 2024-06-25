from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

def execute_code(language, code):
    # Implement code execution logic for each language
    if language == 'python':
        process = subprocess.run(['python3', '-c', code], capture_output=True, text=True)
    elif language == 'javascript':
        process = subprocess.run(['node', '-e', code], capture_output=True, text=True)
    elif language == 'ruby':
        process = subprocess.run(['ruby', '-e', code], capture_output=True, text=True)
    else:
        return "Language not supported", 400

    return process.stdout or process.stderr

@app.route('/run', methods=['POST'])
def run():
    data = request.get_json()
    language = data['language']
    code = data['code']
    output = execute_code(language, code)
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
