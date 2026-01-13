import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", initial_sidebar_state="collapsed")

if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

def toggle_theme():
    if st.session_state.theme == 'light':
        st.session_state.theme = 'dark'
    else:
        st.session_state.theme = 'light'

if st.session_state.theme == 'dark':
    bg_color = "#0E1117"
    text_color = "#FAFAFA"
    input_bg = "#262730"
    button_color = "#FF4B4B"
else:
    bg_color = "#FFFFFF"
    text_color = "#31333F"
    input_bg = "#F0F2F6"
    button_color = "#FF4B4B"

st.markdown(f"""
<style>
    .stApp {{
        background-color: {bg_color};
    }}
    h1 {{
        color: {text_color};
        text-align: center;
        font-size: 45px;
    }}
    label {{
        color: {text_color} !important;
        font-size: 18px !important;
    }}
    .stButton button {{
        background-color: {button_color};
        color: white;
        width: 100%;
        height: 50px;
        font-size: 20px;
        border-radius: 8px;
    }}
    .stButton button:hover {{
        background-color: #FF6B6B;
    }}
    input {{
        background-color: {input_bg} !important;
        color: {text_color} !important;
    }}
    div[data-baseweb="select"] {{
        background-color: {input_bg} !important;
    }}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([9, 1])
with col2:
    if st.button("🌓"):
        toggle_theme()
        st.rerun()

st.title("🧮 Calculator")
st.write("")

number1 = st.number_input("First Number", value=0.0)
number2 = st.number_input("Second Number", value=0.0)

operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    
    if operation == "Add":
        result = number1 + number2
        st.success(f"Answer: {result}")
    
    elif operation == "Subtract":
        result = number1 - number2
        st.success(f"Answer: {result}")
    
    elif operation == "Multiply":
        result = number1 * number2
        st.success(f"Answer: {result}")
    
    elif operation == "Divide":
        if number2 == 0:
            st.error("Cannot divide by zero!")
        else:
            result = number1 / number2
            st.success(f"Answer: {result}")
