# Gemini AI Playground

Gemini AI Playground is a modern Streamlit-based web app powered by Google’s Gemini Pro API. It offers a suite of interactive AI features including chatbot interaction, image captioning, text embedding, and an open-ended Q&A interface. 
---

## ✨ Features

- 🤖 **ChatBot** – Talk to Gemini Pro like a friend or assistant.
- 🖼️ **Image Captioning** – Upload any image and get intelligent captions.
- 🧾 **Embed Text** – Convert text into meaningful embeddings.
- ❓ **Ask Me Anything** – A versatile Q&A interface powered by LLM.

---

## 🎨 UI Highlights

- 🔹 Sidebar navigation using `streamlit-option-menu`
- 🖼️ Gemini logo branding and modern dark theme
- 💬 Personalized greeting with user name (stored in session state)
- 🚀 Clean layout with icons, feedback messages, and smart flow

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit + Tailored CSS
- **Backend AI:** Gemini Pro API (Text & Vision models)
- **Image Handling:** Pillow (PIL)
- **Session Management:** `st.session_state`

---

## 🚀 Getting Started

1. Clone the repository**
   ```bash
   git clone https://github.com/your-username/gemini-ai-playground.git
   cd gemini-ai-playground
   Install dependencies
2. Install dependencies
   ```bash
   pip install -r requirements.txt
3. Add your Gemini API key
   Create a .streamlit/secrets.toml file:
   ```toml
   [api] gemini_key = "your_gemini_api_key"
4. Run the app
   ```bash
   streamlit run main.py

## 📜 License
This project is licensed under the MIT License.
   
