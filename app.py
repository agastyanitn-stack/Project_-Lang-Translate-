from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from deep_translator import GoogleTranslator
from PyPDF2 import PdfReader
from collections import Counter
import re

app = Flask(__name__)

# ===== LOAD MODEL =====
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


# ===== READ PDF FUNCTION =====
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


# ===== SUMMARIZE FUNCTION =====
def summarize_text(text):
    if len(text.split()) < 25:
        return text

    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)

    summary_ids = model.generate(
        inputs["input_ids"],
        num_beams=4,
        max_length=150,
        min_length=60,
        no_repeat_ngram_size=3,
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


# ===== TRANSLATE FUNCTION =====
def translate_text(text, lang):
    return GoogleTranslator(source="en", target=lang).translate(text)


# ===== HEADING DETECTION =====
def extract_headings(text):
    lines = text.split("\n")
    headings = []

    for line in lines:
        line = line.strip()

        if len(line) < 4:
            continue

        # Numbered headings
        if re.match(r'^\d+[\.\)]\s+[A-Z]', line):
            headings.append(line)

        # ALL CAPS headings
        elif line.isupper() and len(line.split()) <= 8:
            headings.append(line.title())

        # Title Case headings
        elif line.istitle() and len(line.split()) <= 8:
            headings.append(line)

    return list(dict.fromkeys(headings))[:10]


# ===== TOPIC EXTRACTION (Fallback) =====
def extract_topics(text, top_n=6):
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()

    stopwords = {
        "the","is","in","and","to","of","a","for","on","with",
        "as","by","an","at","from","that","this","it","are","be",
        "was","were","has","have","had","but","not","or","if"
    }

    filtered = [w for w in words if w not in stopwords and len(w) > 4]
    most_common = Counter(filtered).most_common(top_n)

    return [word.capitalize() for word, count in most_common]


@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    translated = ""
    reduced_words = None
    reading_time_saved = None
    reduction_percent = None
    topics = []

    if request.method == "POST":

        text = request.form.get("text", "")
        language = request.form.get("language")
        mode = request.form.get("mode")

        # PDF Upload
        if "pdf_file" in request.files and request.files["pdf_file"].filename != "":
            pdf_file = request.files["pdf_file"]
            text = extract_text_from_pdf(pdf_file)

        original_word_count = len(text.split())

        # Summarization
        summary = summarize_text(text)

        summary_word_count = len(summary.split())
        reduced_words = original_word_count - summary_word_count
        reading_time_saved = round(reduced_words / 200, 2)

        if original_word_count > 0:
            reduction_percent = int((reduced_words / original_word_count) * 100)
        else:
            reduction_percent = 0

        # Heading detection first
        topics = extract_headings(text)

        # If headings not found, fallback to keyword topics
        if not topics:
            topics = extract_topics(text)

        # Translation
        if mode == "online":
            translated = translate_text(summary, language)

    return render_template(
        "index.html",
        summary=summary,
        translated=translated,
        reduced_words=reduced_words,
        reading_time_saved=reading_time_saved,
        reduction_percent=reduction_percent,
        topics=topics
    )


if __name__ == "__main__":
    app.run(debug=True)
