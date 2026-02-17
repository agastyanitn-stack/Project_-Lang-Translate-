# 📝 Text Summarizer & Translator

> A powerful web application that summarizes long texts and translates them into multiple languages using state-of-the-art NLP models.

![Flask](https://img.shields.io/badge/Flask-3.1-blue?style=flat-square&logo=flask)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Transformers](https://img.shields.io/badge/Transformers-Latest-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## ✨ Features

- **🔄 Text Summarization** - Compress lengthy texts into concise summaries using Facebook's BART model
- **🌍 Multi-Language Translation** - Translate summaries into 100+ languages
- **📄 PDF Support** - Extract text directly from PDF files
- **⚡ Real-time Processing** - Fast and efficient text processing
- **🎨 User-Friendly Interface** - Clean, responsive web interface
- **🛡️ Robust Chunk Processing** - Handle large texts with intelligent chunking
- **📊 Smart Summarization** - Configurable summary length and beam search parameters

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd Project_Text_Summarizer
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv ml_env
ml_env\Scripts\activate

# macOS/Linux
python3 -m venv ml_env
source ml_env/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download required models**
```bash
python download_models.py
```

5. **Run the application**
```bash
python app.py
```

Visit `http://localhost:5000` in your browser to access the application.

## 📖 Usage

### Web Interface

1. **Enter or paste text** in the text area
2. **Upload a PDF** (optional) to extract and summarize content
3. **Click Summarize** to generate a concise summary
4. **Select a language** from the dropdown
5. **Translate** to get the summary in your chosen language

### Python API

```python
from summarize import summarize_text
from translate import translate_text

# Summarize text
text = "Your long text here..."
summary = summarize_text(text)

# Translate to another language
translated = translate_text(summary, 'es')  # Spanish
```

## 📁 Project Structure

```
Project_Text_Summarizer/
├── app.py                    # Main Flask application
├── summarize.py             # Text summarization logic
├── translate.py             # Translation logic
├── download_models.py       # Model download script
├── requirements.txt         # Project dependencies
├── README.md               # This file
├── .gitignore              # Git ignore rules
│
├── models/
│   └── nllb/               # NLLB model files
│       ├── config.json
│       ├── tokenizer.json
│       ├── model.safetensors
│       └── generation_config.json
│
├── static/
│   └── style.css           # CSS styling
│
├── templates/
│   └── index.html          # Web interface
│
└── ml_env/                 # Virtual environment
```

## 🔧 Configuration

Key parameters in `app.py`:

- **Model**: Facebook's BART (facebook/bart-large-cnn)
- **Max Input Length**: 1024 tokens
- **Max Summary Length**: 150 tokens
- **Min Summary Length**: 60 tokens
- **Beam Size**: 4

Adjust these parameters in the `summarize_text()` function for different results.

## 🧠 Models Used

### Summarization
- **BART Large CNN** (facebook/bart-large-cnn)
  - Pre-trained on CNN/Daily Mail dataset
  - Optimized for news and article summarization

### Translation
- **Google Translator API** (via deep-translator library)
  - Supports 100+ languages
  - Auto-detection of source language

## 📊 Technical Details

### How Summarization Works

1. **Text Preprocessing** - Clean and normalize input text
2. **Tokenization** - Convert text to model-compatible tokens
3. **Beam Search** - Generate multiple candidate summaries
4. **Selection** - Choose the best summary based on scores
5. **Decoding** - Convert tokens back to readable text

### Handling Large Texts

For texts exceeding 400 words:
- Split into manageable chunks
- Summarize each chunk independently
- Combine summaries for final output

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Models not loading | Run `python download_models.py` to ensure models are downloaded |
| Port already in use | Change port in `app.py`: `app.run(port=5001)` |
| Memory issues | Reduce `max_length` and `min_length` parameters in summarize.py |
| Translation fails | Check internet connection; Google Translate requires online access |

## 📋 Requirements

See [requirements.txt](requirements.txt) for complete list:
- Flask 3.1+
- Transformers (HuggingFace)
- PyTorch
- Deep-Translator
- PyPDF2
- BeautifulSoup4

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest enhancements
- Submit pull requests

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💼 Author

Created as part of NLP Project (6th Semester)

## 🙏 Acknowledgments

- [Facebook Research - BART Model](https://huggingface.co/facebook/bart-large-cnn)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Deep-Translator Library](https://github.com/nidhaloff/deep-translator)

## 📞 Support

For questions or issues, please create an issue in the repository.

---

**Happy Summarizing! 🎉**
