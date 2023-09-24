from flask import Flask, request, render_template
import PyPDF2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        print("hola")
        uploaded_file = request.files["formFile"]
        if uploaded_file.filename != "":
            # Check if the file is a PDF
            if uploaded_file.filename.endswith(".pdf"):
                pdf_file = PyPDF2.PdfReader(uploaded_file)
                num_pages = len(pdf_file.pages)
                text = ""
                for page_num in range(num_pages) : 
                    page = pdf_file.pages[page_num]
                    text = page.extract_text()
                    print(text)

                return text
            else:
                return "Uploaded file is not a PDF."
        else:
            return "No file uploaded."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)