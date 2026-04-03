import streamlit as st
import google.generativeai as genai
from google.generativeai.types import RequestOptions

# הגדרת המפתח
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("חסר מפתח API ב-Secrets!")

# יצירת המודל עם הגדרת גרסת ה-API באופן מפורש ל-v1
model = genai.GenerativeModel('gemini-1.5-flash')

# הגדרת ה-SI
system_prompt = "אתה ארנסטו, אנליסט מחוספס לחשיפת מניפולציות. תענה תכלס, בעברית, בלי חרטות."

st.title("ארנסטו: טר'ול אנליסט")

user_input = st.text_input("מה המניפולציה הפעם?")

if st.button("נתח תכלס"):
    if user_input:
        try:
            # כאן אנחנו מכריחים את הבקשה להשתמש ב-v1 ולא ב-v1beta
            response = model.generate_content(
                f"{system_prompt}\n\nסיפור: {user_input}",
                request_options=RequestOptions(api_version='v1')
            )
            st.subheader("ארנסטו אומר:")
            st.write(response.text)
        except Exception as e:
            st.error(f"שגיאה טכנית: {e}")
    else:
        st.write("תכתוב משהו, אל תהיה צבוע.")
