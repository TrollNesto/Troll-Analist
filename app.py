import streamlit as st
import google.generativeai as genai

# הגדרת המפתח מה-Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("חסר מפתח API ב-Secrets!")

# שימוש במודל הכי יציב שיש לגוגל בחינם
model = genai.GenerativeModel('gemini-1.5-flash')

# ה-SI המקוצר של ארנסטו
system_prompt = "אתה ארנסטו, אנליסט מחוספס לחשיפת מניפולציות. תענה תכלס, בעברית, בלי חרטות."

st.title("ארנסטו: טר'ול אנליסט (גרסת טקסט)")

user_input = st.text_input("מה המניפולציה הפעם?")

if st.button("נתח תכלס"):
    if user_input:
        try:
            # בקשת טקסט פשוטה - בלי תמונות ובלי סיבוכים
            response = model.generate_content(f"{system_prompt}\n\nהנה הסיפור: {user_input}")
            st.subheader("ארנסטו אומר:")
            st.write(response.text)
        except Exception as e:
            st.error(f"שגיאה: {e}")
    else:
        st.write("תכתוב משהו, אל תהיה צבוע.")
