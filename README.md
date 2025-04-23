# 🔐 Password Strength Meter

This is a simple yet powerful app that evaluates the strength of a user's password. It is built using Python and Streamlit.

## 🧠 Problem:
Many people tend to use weak and easily guessable passwords like "123456", "password", or "abc123". Such passwords pose a serious risk to user security.

## 💡 Solution:
This app provides real-time feedback to users by checking:
- Password length
- A mix of uppercase and lowercase letters
- Presence of numbers (0-9)
- Inclusion of special characters (!@#$%^&*)

Additionally, it checks if the password is on a **common blacklist** and provides a warning if it is.

## 🔧 Features:
- 🔒 Real-time password strength scoring (0 to 4)
- ❌ Detection of weak passwords using a blacklist
- 🎲 Random password generator (Hint button)
- 📊 Visual progress bar for strength level
- ⚠️ Helpful suggestions for password improvement

## 📦 Tech Stack:
- Python
- Streamlit
- Regex
- Random
- String

## 🚀 How to Run:
```bash
pip install streamlit
streamlit run password.py
