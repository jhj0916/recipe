from flask import Flask, render_template
import markdown

app = Flask(__name__)

@app.route("/")
def index():
    with open("example.md", "r", encoding="utf-8") as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content)
    
    return render_template("layout.html", content=html_content)

if __name__ == "__main__":
    app.run(debug=True)
