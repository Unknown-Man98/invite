import streamlit as st

# Page setup
st.set_page_config(page_title="Dla Martynki ❤️", page_icon="💌", layout="centered")

# Custom CSS for the romantic vibe
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    }
    .main-card {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
    }
    h1 { color: #d63384 !important; font-family: 'Georgia', serif; }
    .stButton>button {
        background-color: #ff4b6b;
        color: white;
        border-radius: 20px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- IMAGE LINKS ---
# Replace these URLs with your actual uploaded image links!
img_intro = "https://your-link-to-first-photo.jpg" 
img_yes = "https://your-link-to-second-photo.jpg"
img_no = "https://your-link-to-third-photo.jpg"

with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    # 1. Start of the App
    if 'stage' not in st.session_state:
        st.session_state.stage = 'intro'

    if st.session_state.stage == 'intro':
        st.title("Dla mojej Pani, Martynki... ✨")
        st.image(img_intro, use_container_width=True) # First Picture
        st.write("I have a very important question for you...")
        if st.button("Click to see what it is 💌"):
            st.session_state.stage = 'question'
            st.rerun()

    # 2. The Big Question
    elif st.session_state.stage == 'question':
        st.markdown("## Martynka, will you be my Valentine? 🌹")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("TAK! 😍"):
                st.session_state.stage = 'yes'
                st.rerun()
        
        with col2:
            if st.button("Nie... ❌"):
                st.session_state.stage = 'no'
                st.rerun()

    # 3. The "Yes" Screen
    elif st.session_state.stage == 'yes':
        st.balloons()
        st.snow()
        st.title("Hooray! ❤️")
        st.image(img_yes, use_container_width=True) # Second Picture
        st.success("I'm the luckiest guy in the world. I'll see you on the 14th!")
        if st.button("Back"):
            st.session_state.stage = 'intro'
            st.rerun()

    # 4. The "No" Screen (The playful error)
    elif st.session_state.stage == 'no':
        st.title("Wait... what? 🤨")
        st.image(img_no, use_container_width=True) # Third Picture
        st.error("Error 404: 'No' is not a valid answer for Martynka. Try again!")
        if st.button("Try again 😉"):
            st.session_state.stage = 'question'
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
