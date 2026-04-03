import streamlit as st
import google.generativeai as genai

# הגדרת ה-API Key מה-Secrets של Streamlit
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# הגדרת המודל המדויק שראית בסטודיו (Nano Banana)
model = genai.GenerativeModel('gemini-2.5-flash-image')

# כאן תדביק את ה-SI המלא של ארנסטו מהסטודיו
system_instructions = """
זהות: אתה ארנסטו, אנליסט לחשיפת מניפולציות.
הנחיות: נתח את הטקסט לפי מילון החיות והוצא תמונה קולנועית מחוספסת.
(מומלץ להדביק כאן את כל ה-SI שיש לך בסטודיו)
"""

st.title("ארנסטו: טר'ול אנליסט")

user_input = st.text_area("מה הסיפור? (תכתוב כאן מה קרה):", placeholder="למשל: אחותי שוב עושה לי גזלייטינג...")

if st.button("נתח והוצא תמונה"):
    if user_input:
        with st.spinner("ארנסטו בודק את הקומבינה..."):
            try:
                # שליחת הבקשה למודל עם ה-SI
                response = model.generate_content([system_instructions, user_input])
                
                # הצגת הטקסט (הניתוח)
                st.subheader("הניתוח של ארנסטו:")
                st.write(response.text)
                
                # הצגת התמונה (אם המודל ג'ינרט אחת)
                if response.candidates[0].content.parts:
                    for part in response.candidates[0].content.parts:
                        if part.inline_data: # בדיקה אם יש נתוני תמונה
                            st.image(part.inline_data.data, caption="האמת של ארנסטו")
            
            except Exception as e:
                st.error(f"שגיאה טכנית: {e}")
    else:
        st.warning("תכתוב משהו, אל תהיה חפרפרת.")
