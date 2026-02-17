import streamlit as st

# Dummy credentials (replace with database or secure storage)
USER_CREDENTIALS = {
    "admin": "1234",
    "sai": "password"
}

def login():
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.success(f"Welcome, {username}!")
            st.session_state["authenticated"] = True
        else:
            st.error("Invalid username or password")

def main_app():
    st.title("Main Application")
    st.write("You are logged in!")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    main_app()
