import streamlit as st

def sach_detector(text):
    text_lower = text.lower()
    # English + Hindi + Chinese Fake Words
    ai_words = ["as an ai", "in conclusion", "delve", "moreover", 
                "fake news", "viral sach", "100% sach",
                "人工智能", "假的新闻", "震惊", "必看"] # Chinese me "Fake, Shocking, Must Watch" ye sab fake news me hota hai
    
    score = 0
    found = []
    for w in ai_words:
        if w in text_lower:
            score += 1
            found.append(w)
    
    # Agar bahut lambe text me Full Stop kam hai to AI wala
    if len(text_lower.split()) > 80 and text_lower.count("。") < 2 and text_lower.count(".") < 3:
        score += 1

    if score >= 2:
        return f"⚠️ FAKE NEWS / 假新闻", found
    else:
        return f"✅ REAL NEWS / 真新闻", found

st.title("🛡️ Vansh - Global News Truth Detector")
st.write("Made by Vansh, Agra | For India + China | 印度 + 中国")

user_text = st.text_area("Koi bhi News yahan dalo (Hindi/English/中文):", height=150)

if st.button("Check Karo / 检查"):
    if user_text.strip() == "":
        st.warning("Pehle News likho!")
    else:
        result, words = sach_detector(user_text)
        if "FAKE" in result:
            st.error(result + " - Ye khabar jhoothi lag rahi hai!")
            st.write("Be careful! 小心假新闻")
        else:
            st.success(result + " - Ye khabar sacchi lag rahi hai!")
        if words:
            st.write(f"Pakde gaye shabd: {', '.join(words)}")

st.caption("Made with ❤️ by Vansh - Future China Trending App")
