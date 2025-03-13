import streamlit as st
import random
import string
import re

# Password Generator
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Blacklist of common passwords
blacklist = ["password", "123456", "qwerty", "password123", "abc123"]

# Check if password is blacklisted
def check_blacklist(password):
    return password.lower() in blacklist

# Password Strength Checker
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

# Streamlit UI
st.title("🔒 Password Strength Meter")

# Password Generator Button
st.sidebar.markdown("""
## Instructions:
1. Password should be at least 8 characters long.
2. Include both uppercase and lowercase letters.
3. Add at least one number (0-9).
4. Include at least one special character (!@#$%^&*).
""")

if st.sidebar.button("*Hint*"):
    st.sidebar.success(f"example: {generate_password()}")

# Password input from user
password = st.text_input("Enter a password to generate:", type="password")

# Add Enter button
if st.button("Enter"):
    if password:
        if check_blacklist(password):
            st.error("Weak password! This password is too common. Please choose a stronger one.")
        else:
            score, feedback = check_password_strength(password)
            st.subheader(f"Password Strength Score: {score}/4")
            st.progress(score / 4)

            for item in feedback:
                st.warning(item)

            if score == 4:
                st.success("✅ Strong Password!")
            elif score == 3:
                st.info("⚠️ Moderate Password - Consider adding more security features.")
            else:
                st.error("⚠️ Weak Password - Improve it using the suggestions above.")
