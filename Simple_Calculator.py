import streamlit as st

# Initialize theme in session state
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# Toggle theme function
def toggle_theme():
    if st.session_state.theme == 'light':
        st.session_state.theme = 'dark'
    else:
        st.session_state.theme = 'light'

# Theme colors
if st.session_state.theme == 'dark':
    bg_color = "#1E1E1E"
    text_color = "#FFFFFF"
    input_bg = "#2D2D2D"
    button_color = "#4CAF50"
    result_bg = "#2D2D2D"
else:
    bg_color = "#F0F2F6"
    text_color = "#262730"
    input_bg = "#FFFFFF"
    button_color = "#4CAF50"
    result_bg = "#FFFFFF"

# CSS for styling
st.markdown(f"""
<style>
    .stApp {{
        background-color: {bg_color};
    }}
    
    .main-title {{
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: {text_color};
        margin-bottom: 30px;
        transition: transform 0.3s ease;
    }}
    
    .main-title:hover {{
        transform: scale(1.05);
    }}
    
    label {{
        font-size: 20px !important;
        color: {text_color} !important;
        font-weight: 500 !important;
    }}
    
    .stButton > button {{
        font-size: 22px;
        padding: 15px 40px;
        background-color: {button_color};
        color: white;
        border: none;
        border-radius: 10px;
        transition: all 0.3s ease;
        width: 100%;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(76, 175, 80, 0.4);
    }}
    
    input {{
        background-color: {input_bg} !important;
        color: {text_color} !important;
        font-size: 18px !important;
        border-radius: 8px !important;
        transition: transform 0.2s ease;
    }}
    
    input:hover {{
        transform: scale(1.02);
    }}
    
    .stSelectbox > div > div {{
        background-color: {input_bg} !important;
        color: {text_color} !important;
    }}
    
    .result-box {{
        font-size: 28px;
        padding: 20px;
        background-color: {result_bg};
        border-radius: 10px;
        text-align: center;
        color: {text_color};
        margin-top: 20px;
        border: 2px solid {button_color};
        transition: all 0.3s ease;
    }}
    
    .result-box:hover {{
        box-shadow: 0 0 20px rgba(76, 175, 80, 0.3);
    }}
    
    .stCaption {{
        color: {text_color} !important;
    }}
</style>
""", unsafe_allow_html=True)

# Theme toggle button in corner
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("🌓"):
        toggle_theme()
        st.rerun()

# Title of calculator
st.markdown(f'<div class="main-title">🧮 My Calculator App</div>', unsafe_allow_html=True)

st.write("")

# Taking input from user
number1 = st.number_input("Enter first number:", value=0.0)
number2 = st.number_input("Enter second number:", value=0.0)

# Dropdown for operation
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Button to calculate
if st.button("Calculate ✨", use_container_width=True):
    
    # Addition
    if operation == "Add":
        result = number1 + number2
        st.markdown(f'<div class="result-box">✅ Answer is: {result}</div>', unsafe_allow_html=True)
    
    # Subtraction
    if operation == "Subtract":
        result = number1 - number2
        st.markdown(f'<div class="result-box">✅ Answer is: {result}</div>', unsafe_allow_html=True)
    
    # Multiplication
    if operation == "Multiply":
        result = number1 * number2
        st.markdown(f'<div class="result-box">✅ Answer is: {result}</div>', unsafe_allow_html=True)
    
    # Division
    if operation == "Divide":
        if number2 == 0:
            st.markdown(f'<div class="result-box">❌ Error! Cannot divide by zero</div>', unsafe_allow_html=True)
        else:
            result = number1 / number2
            st.markdown(f'<div class="result-box">✅ Answer is: {result}</div>', unsafe_allow_html=True)