# Gemini AI Playground
Gemini AI Playground is a sleek Streamlit web app that integrates Google's Gemini Pro API to offer multiple AI-powered features like chatbot interaction, image captioning, text embedding, and open-ended Q&A.
The app provides a clean, minimal UI with sidebar navigation, personalized greetings, and seamless session management.

## 🚀 Features

🤖 ChatBot – Talk to Gemini Pro like a friend or assistant.
🖼️ Image Captioning – Upload any image and get intelligent captions.
🔡 Embed Text – Convert text into meaningful embeddings.
❓ Ask Me Anything – A versatile Q&A interface powered by LLM.
👤 Personalized Experience – Name-based greetings with session state tracking.
🧠 Multi-functional UI – Sidebar-based mode switching.

## 🛠️ Tech Stack

Frontend: Streamlit
Backend: Python
LLM API: Google Gemini Pro API
Tools: OpenAI, Pillow, JSON, etc.

## 📂 Project Structure

Copy code
Gemini_AI_Playground/
│
├── main.py               # Main Streamlit app
├── gemini_utility.py     # API interaction & processing
├── config.json           # API keys and configuration
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignore files (e.g. .venv/)
└── README.md             # Project description

## 🔧 Installation & Run Locally

# 1. Clone the repository
git clone https://github.com/sharvaritarte/gemini_playground.git
cd gemini_playground

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Gemini Pro API key to config.json

# 5. Run the app
streamlit run main.py

## 🔑 API Setup

You'll need an API key from Google Gemini.
Add it in config.json as:
json
{
  "api_key": "your-gemini-api-key"
}
