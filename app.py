import streamlit as st

# Page setup
st.set_page_config(page_title="For My Favorite Person", page_icon="💌", layout="centered")

# Custom CSS for the "Valentine Card" look
st.markdown("""
    <style>
    /* Change background color */
    .stApp {
        background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    }
    
    /* Style the main card container */
    .main-card {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Custom fonts and colors */
    h1 {
        color: #d63384 !important;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }
    
    p {
        color: #555;
        font-size: 18px;
    }

    /* Style buttons */
    .stButton>button {
        background-color: #ff4b6b;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 25px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #d63384;
        border: none;
        color: white;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

# App Content
with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    
    st.title("To My Favorite Human... ✨")
    
    # You can replace this URL with a link to a cute photo of you two
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/L4lvBpHFmEofNvCc9B/giphy.gif", width=200)
    
    st.write("I've been thinking about how to ask you this all week...")
    
    if st.button("Click to open the letter"):
        st.balloons()
        st.markdown("## Will you be my Valentine? 🌹")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("YES! 😍"):
                st.snow()
                st.write("### It's a date! ❤️")
                st.write("I'll pick you up at 7:00 PM. Wear something you feel beautiful in (which is anything)!")
        
        with col2:
            if st.button("No (Try again)"):
                st.write("Oops! That button seems to be broken. Try the one on the left! 😉")
                
    st.markdown('</div>', unsafe_allow_html=True)
