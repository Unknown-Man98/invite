import streamlit as st

# Page setup
st.set_page_config(page_title="Dla Martynki ❤️", page_icon="💌", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    }
    .main-card {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
        margin-top: 50px;
    }
    h1 {
        color: #d63384 !important;
        font-family: 'Georgia', serif;
    }
    p {
        font-size: 20px;
        color: #444;
    }
    .stButton>button {
        background-color: #ff4b6b;
        color: white;
        border-radius: 20px;
        padding: 10px 30px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    # Title in Polish
    st.title("Dla mojej Pani, Martynki... ✨")
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/L4lvBpHFmEofNvCc9B/giphy.gif", width=200)
    
    st.write("I have a very important question for you today...")

    # Logic for buttons
    if 'answered' not in st.session_state:
        st.session_state.answered = False

    if not st.session_state.answered:
        if st.button("Click to see what it is 💌"):
            st.session_state.answered = True
            st.rerun()
    else:
        st.balloons()
        st.markdown("## Will you be my Valentine? 🌹")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("TAK! 😍"):
                st.snow()
                st.success("Yay! You just made me the happiest person! I'll see you on the 14th! ❤️")
        
        with col2:
            if st.button("Nie... ❌"):
                st.error("Error! This button is currently out of service. Please click 'TAK' instead! 😉")

    st.markdown('</div>', unsafe_allow_html=True)
