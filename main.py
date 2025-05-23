import os
from email.policy import default

from PIL import Image
import streamlit as st
from streamlit import caption
from streamlit_option_menu import option_menu

# Import all functions from gemini_utility
from gemini_utility import (load_gemini_pro_model,
                            gemini_pro_vision_response,
                            embedding_model_response,
                            gemini_pro_response)

# getting the working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# setting up the page configuration
st.set_page_config(
    page_title="Gemini AI Playground",
    page_icon="😶‍🌫️",
    layout="centered"
)

# Custom CSS for a bit more flair
st.markdown("""
    <style>
    .main-header {
        font-size: 3.5em;
        font-weight: bold;
        color: #4CAF50; /* Green */
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextArea, .stTextInput {
        border-radius: 8px;
        padding: 10px;
    }
    .stChatInputContainer {
        border-radius: 8px;
        padding: 10px;
        background-color: #f0f2f6;
    }
    .stInfo {
        background-color: #e6f7ff;
        color: #0056b3;
        border-left: 5px solid #0056b3;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("😶‍🌫️ Gemini AI Playground")
    selected = option_menu("Explore Features",
                           ["ChatBot",
                            "Image Captioning",
                            "Embed Text",
                            "Ask Me Anything"],
                           menu_icon='robot',
                           icons=['chat-dots-fill', 'image-fill', 'textarea-t', 'patch-question-fill'],
                           default_index=0
                           )

# User Name Personalization
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if st.session_state.user_name == "":
    st.info("👋 Welcome! Please enter your name to personalize your experience.")
    user_name_input = st.text_input("What's your name?", key="name_input")
    if user_name_input:
        st.session_state.user_name = user_name_input
        st.success(f"Hello, {st.session_state.user_name}! Enjoy your Gemini AI experience.")
else:
    st.sidebar.write(f"Hello, {st.session_state.user_name}! 👋")


# Caching the model loading to prevent re-loading on every rerun
@st.cache_resource
def get_gemini_pro_model_cached():
    return load_gemini_pro_model()


@st.cache_data
def get_gemini_pro_vision_response_cached(prompt, _image):
    return gemini_pro_vision_response(prompt, _image)


@st.cache_data
def get_embedding_model_response_cached(input_text):
    return embedding_model_response(input_text)


@st.cache_data
def get_gemini_pro_response_cached(user_prompt):
    return gemini_pro_response(user_prompt)


# function to translate role between gemini pro and streamlit terminology
def translate_role_for_streamlit(user_role):
    if (user_role == "model"):
        return "assistant"
    else:
        return user_role


if selected == "ChatBot":
    st.markdown("<h1 class='main-header'>🤖 AI Chat Companion</h1>", unsafe_allow_html=True)
    st.write(
        "Start a friendly conversation with Gemini Pro! Ask anything you like. Your chat history will be maintained for this session.")

    model = get_gemini_pro_model_cached()

    # Initialize chat session in streamlit if not already present(maintaining chat session(history))
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # input field for user's message
    user_prompt = st.chat_input("Ask Gemini-Pro...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        with st.spinner("Gemini is thinking..."):
            gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # display gemini-pro response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

    if st.session_state.chat_session.history:
        chat_history_text = ""
        for message in st.session_state.chat_session.history:
            chat_history_text += f"{message.role.capitalize()}: {message.parts[0].text}\n\n"

        st.download_button(
            label="Download Chat History",
            data=chat_history_text,
            file_name="gemini_chat_history.txt",
            mime="text/plain"
        )

# Image Captioning Page
if selected == "Image Captioning":
    st.markdown("<h1 class='main-header'>📸 Snap Narrate: Image Captioning</h1>", unsafe_allow_html=True)
    st.write("Upload an image and let Gemini Vision generate a descriptive caption for you!")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    caption_output = ""
    if uploaded_image:
        image = Image.open(uploaded_image)

        st.subheader("Your Uploaded Image:")
        # Replaced use_column_width=True with use_container_width=True
        st.image(image, caption='Uploaded Image', use_container_width=True)

        if st.button("Generate Caption 🚀"):
            with st.spinner("Generating caption..."):
                default_prompt = "write a short, engaging and descriptive caption for this image"
                caption_output = get_gemini_pro_vision_response_cached(default_prompt, image)
                st.subheader("Generated Caption:")
                st.info(caption_output)

    if caption_output:
        st.download_button(
            label="Download Caption",
            data=caption_output,
            file_name="image_caption.txt",
            mime="text/plain"
        )

# text embedding page
if selected == "Embed Text":
    st.markdown("<h1 class='main-header'>🔡 Text Embedder</h1>", unsafe_allow_html=True)
    st.write("Enter any text below to get its numerical vector representation (embedding).")

    # input text box
    input_text = st.text_area(label="Your Text:", placeholder="Type or paste the text you want to embed here...",
                              height=150)

    if st.button("Get Embeddings ✨"):
        if input_text:
            with st.spinner("Generating embeddings..."):
                response = get_embedding_model_response_cached(input_text)
                st.subheader("Generated Embedding (first 100 characters):")
                st.code(str(response)[:100] + "...")
                st.download_button(
                    label="Download Full Embedding",
                    data=str(response),
                    file_name="text_embedding.txt",
                    mime="text/plain"
                )
        else:
            st.warning("Please enter some text to get embeddings.")

# question answering page
if selected == "Ask Me Anything":
    st.markdown("<h1 class='main-header'>❓ Ask Gemini: Direct Q&A</h1>", unsafe_allow_html=True)
    st.write("Ask Gemini Pro any question and get a direct answer.")

    # text box to enter prompt
    user_prompt = st.text_area(label="Your Question:", placeholder="e.g., Explain quantum physics in simple terms...",
                               height=100)

    ai_response = ""
    if st.button("Get an Answer 💡"):
        if user_prompt:
            with st.spinner("Fetching answer..."):
                ai_response = get_gemini_pro_response_cached(user_prompt)
                st.subheader("Gemini's Answer:")
                st.info(ai_response)
        else:
            st.warning("Please type a question to get an answer.")

    if ai_response:
        st.download_button(
            label="Download Answer",
            data=ai_response,
            file_name="gemini_answer.txt",
            mime="text/plain"
        )