import streamlit as st
import google.generativeai as genai

# הגדרת המפתח
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("חסר מפתח API ב-Secrets!")

# יצירת המודל - הכי פשוט שיש
# אם 1.5-flash נותן 404, ננסה את השם המלא שלו
model = genai.GenerativeModel('gemini-2.0-flash')

# ה-SI של ארנסטו
system_prompt = "אתה ארנסטו, אנליסט מחוספס לחשיפת מניפולציות. תענה תכלס, בעברית, בלי חרטות."

st.title("ארנסטו: טר'ול אנליסט")

user_input = st.text_input("מה המניפולציה הפעם?")

if st.button("נתח תכלס"):
    if user_input:
        try:
            # שימוש בשיטה הכי בסיסית של הספרייה
            response = model.generate_content(f"{system_prompt}\n\nסיפור: {user_input}")
            
            if response.text:
                st.subheader("ארנסטו אומר:")
                st.write(response.text)
            else:
                st.error("המודל לא החזיר טקסט. ייתכן שיש חסימת תוכן.")
        except Exception as e:
            # אם גם זה נכשל ב-404, ננסה מודל חלופי באותה ריצה
            try:
                model_alt = genai.GenerativeModel('gemini-pro')
                response = model_alt.generate_content(f"{system_prompt}\n\nסיפור: {user_input}")
                st.subheader("ארנסטו אומר (via Pro):")
                st.write(response.text)
            except:
                st.error(f"שגיאה סופית: {e}")
    else:
        st.write("תכתוב משהו, אל תהיה צבוע.")
