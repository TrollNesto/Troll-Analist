import streamlit as st
import google.generativeai as genai

# הגדרות דף ועיצוב לימין
st.set_page_config(page_title="ארנסטו: טר'ול אנליסט", layout="centered")
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    body { direction: rtl; text-align: right; }
    div.stButton > button { width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# חיבור ל-API מה-Secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# כאן תדביק את ה-SI המלא שלך (בין הגרשיים)
SYSTEM_PROMPT = """
אתה ארנסטו... [הדבק כאן את ה-SI שלך]
"""

# הגדרת המודל
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

st.title("🕶️ ארנסטו: טר'ול אנליסט")

user_input = st.text_area("מה קרה?", height=150, placeholder="תאר את הסיטואציה כאן...")

if st.button("נתח סיטואציה"):
    if user_input:
        try:
            with st.spinner("ארנסטו מנתח..."):
                response = model.generate_content(user_input)
                st.markdown("---")
                st.write(response.text)
        except Exception as e:
            st.error(f"שגיאה: {e}")
    else:
        st.warning("תכתוב משהו, אל תהיה יען.")
