from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Directory containing themes
THEME_DIR = os.path.join(os.getcwd(), "static/themes")

@app.route("/")
def index():
    return """
    <h2>Theme Selector</h2>
    <p>Select a theme: <a href='/theme?name=default'>Default</a> |
    <a href='/theme?name=dark'>Dark</a> |
    <a href='/theme?name=../../../../etc/passwd'>Try Hacking!</a></p>
    """

@app.route("/theme")
def theme():
    theme_name = request.args.get("name", "default")

    # ⚠️ Vulnerable: Allows path traversal via theme_name input
    theme_path = os.path.join(THEME_DIR, theme_name, "style.css")

    if not os.path.exists(theme_path):
        return "Theme not found!", 404

    with open(theme_path, "r") as f:
        content = f.read()

    return render_template_string(f"<pre>{content}</pre>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

