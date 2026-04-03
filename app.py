import streamlit as st
import google.generativeai as genai

# הגדרת המפתח
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    # כפיית עבודה עם REST וגרסה v1 כדי למנוע שגיאות 404
    genai.configure(api_key=api_key, transport='rest')
except:
    st.error("חסר מפתח API ב-Secrets!")

# הגדרת המודל - בלי 'models/' ובלי שטויות
model = genai.GenerativeModel('gemini-1.5-flash')

# ה-SI של ארנסטו
system_prompt = "אתה ארנסטו, אנליסט מחוספס לחשיפת מניפולציות. תענה תכלס, בעברית, בלי חרטות."

st.title("ארנסטו: טר'ול אנליסט")

user_input = st.text_input("מה המניפולציה הפעם?")

if st.button("נתח תכלס"):
    if user_input:
        try:
            # שליחה נקייה
            response = model.generate_content(f"{system_prompt}\n\nסיפור: {user_input}")
            st.subheader("ארנסטו אומר:")
            st.write(response.text)
        except Exception as e:
            # אם גם זה נכשל, נציג את השגיאה המדויקת
            st.error(f"שגיאה טכנית: {e}")
    else:
        st.write("תכתוב משהו, אל תהיה צבוע.")
