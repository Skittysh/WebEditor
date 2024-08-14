from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    os.makedirs("Notes", exist_ok=True)
    notes_dir = os.path.join(os.getcwd(), 'Notes')
    files = os.listdir(notes_dir)
    return render_template('index.html', files=files)

@app.route('/file/<name>')
def get_file_content(name):
    file_path = os.path.join("Notes", name)
    
    if not os.path.exists(file_path):
        return jsonify({"error": "No such file!"}), 404
    
    with open(file_path, "r") as file:
        content = file.read()
    
    return jsonify({"name": name, "content": content})

@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    content = request.form['content']
    file_path = os.path.join("Notes", name)
    
    if not os.path.exists(file_path):
        return jsonify({"error": "No such file!"}), 404
    
    with open(file_path, "w") as file:
        file.write(content)
    
    return jsonify({"success": True})

@app.route('/delete/<name>', methods=['POST'])
def delete(name):
    file_path = os.path.join("Notes", name)
    
    if not os.path.exists(file_path):
        return jsonify({"error": "No such file!"}), 404
    
    try:
        os.remove(file_path)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    file_path = os.path.join("Notes", name)

    if os.path.exists(file_path):
        return jsonify({"error": "File already exists :("}), 400

    try:
        with open(file_path, "w") as file:
            pass
        return jsonify({"success": True, "message": "File created!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
