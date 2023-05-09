from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

class IntermediateCodeGenerator:
    # ... Same code as before ...

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_intermediate_code():
    cpp_code = request.json["code"]
    generator = IntermediateCodeGenerator()
    generator.generate(cpp_code)
    intermediate_code = generator.get_code()
    return jsonify(intermediate_code)

if __name__ == "__main__":
    app.run(debug=True)
