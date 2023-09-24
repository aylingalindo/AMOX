from flask import Flask, request, render_template
import PyPDF2
from softtek_llm.chatbot import Chatbot, Filter, InvalidPrompt
from softtek_llm.models import OpenAI

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        response = ""
        model,chatbot = setUp()
        uploaded_file = request.files["formFile"]
        if uploaded_file.filename != "":
            # Check if the file is a PDF
            if uploaded_file.filename.endswith(".pdf"):
                pdf_file = PyPDF2.PdfReader(uploaded_file)
                num_pages = len(pdf_file.pages)
                text = ""
                for page_num in range(num_pages) : 
                    page = pdf_file.pages[page_num]
                    text = text + " " + page.extract_text()

                response = response(chatbot, text)
                print(response)
                return text
            else:
                return "Uploaded file is not a PDF."
        else:
            return "No file uploaded."
    return render_template("index.html")


def setUp():
    model = OpenAI(
    api_key="6b25369971534252bbcee5e488ce59f1",
    model_name="InnovationGPT2",
    api_type="azure",
    api_base="https://openaistkinno.openai.azure.com/"
    )

    chatbot = Chatbot(model=model)

    return model, chatbot

def response(chatbot, text):
    prompt = text
    response = chatbot.chat(prompt)
    return response

if __name__ == "__main__":
    app.run(debug=True)