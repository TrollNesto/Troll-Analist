import streamlit as st
import google.generativeai as genai

# חיבור ישיר - בלי סיבוכים
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("בדיקת מערכת ארנסטו")
user_input = st.text_input("תגיד משהו לבדיקה:")

if st.button("שלח"):
    try:
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(f"תקלה: {e}")
