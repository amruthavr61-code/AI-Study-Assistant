import streamlit as st
from streamlit_option_menu import option_menu
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Sidebar ----------------
with st.sidebar:
    selected = option_menu(
        menu_title="AI Study Assistant",
        options=["Home", "Study", "About"],
        icons=["house", "book", "info-circle"],
        menu_icon="robot",
        default_index=0,
    )

# ---------------- Home ----------------
if selected == "Home":

    st.title("🤖 AI Study Assistant")

    st.markdown("""
    Welcome to your **Personal AI Study Assistant**.

    This website helps students:
    - 📚 Learn different subjects
    - 📝 Understand concepts easily
    - 💡 Get quick explanations
    - 🎓 Improve exam preparation

    ---
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🐍 Python")

    with col2:
        st.info("💻 Data Structures")

    with col3:
        st.info("🤖 Artificial Intelligence")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.info("🐧 Linux")

    with col5:
        st.info("📐 Mathematics")

    with col6:
        st.info("⚡ Electronics")

    st.success("Select **Study** from the sidebar to start learning.")

# ---------------- Study ----------------
elif selected == "Study":

    st.title("📚 AI Study Assistant")

    subject = st.selectbox(
        "Choose Subject",
        [
            "Python",
            "Data Structures",
            "Artificial Intelligence",
            "Linux",
            "Mathematics",
            "Electronics"
        ]
    )

    question = st.text_area("Ask your question")

    if st.button("Get Answer 🚀"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            st.chat_message("user").write(question)

            with st.spinner("🤖 Thinking..."):

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role":"system",
                            "content":f"You are an expert {subject} teacher. Explain answers simply for first-year BTech students."
                        },
                        {
                            "role":"user",
                            "content":question
                        }
                    ]
                )

                answer = response.choices[0].message.content

            st.chat_message("assistant").write(answer)
elif selected == "About":

    st.title("ℹ About Project")

    st.markdown("""
### AI Study Assistant

This project is developed using **Python** and **Streamlit**.

### Frontend
- Streamlit

### Backend
- Python

### Features
- Subject Selection
- Study Assistance
- User Friendly Interface
- Chat Interface
- Easy Navigation

### Future Enhancements
- AI Integration
- Voice Input
- PDF Notes
- Quiz Generator
- Chat History
""")