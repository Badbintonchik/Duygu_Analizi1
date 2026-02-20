import streamlit as st
st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="🧠")
# --- Duygu Kelime Listeleri ---
POSITIVE_WORDS = [
    "good", "great", "excellent", "amazing", "wonderful", "happy", "love",
    "fantastic", "awesome", "best", "beautiful", "nice", "perfect", "brilliant",
    "superb", "outstanding", "positive", "glad", "joyful", "pleased",
    "iyi", "güzel", "harika", "mükemmel", "süper", "mutlu", "seviyorum",
    "muhteşem", "başarılı", "memnun", "sevindim", "güzel", "olumlu"
]
NEGATIVE_WORDS = [
    "bad", "terrible", "awful", "horrible", "hate", "worst", "ugly",
    "disgusting", "poor", "negative", "sad", "disappointed", "boring",
    "fail", "failure", "wrong", "stupid", "annoying", "frustrating",
    "kötü", "berbat", "korkunç", "nefret", "üzgün", "başarısız",
    "hayal kırıklığı", "olumsuz", "sıkıcı", "sinir", "yanlış"
]
def analyze_sentiment(text):
    words = text.lower().split()
    pos_count = sum(1 for w in words if w in POSITIVE_WORDS)
    neg_count = sum(1 for w in words if w in NEGATIVE_WORDS)
    total = pos_count + neg_count
    if total == 0:
        return 0.5, 0.5, "neutral"
    positive = pos_count / total
    negative = neg_count / total
    if positive > 0.6:
        sentiment = "positive"
    elif negative > 0.6:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return positive, negative, sentiment
# --- Arayüz ---
st.title("🧠 Yapay Zeka Duygu Analizi")
st.write("Metnin duygu durumunu analiz edin. Türkçe ve İngilizce desteklenir.")
text_input = st.text_area(
    "Analiz edilecek metni girin:",
    height=150,
    placeholder="Örnek: Bu ürün gerçekten harika ve çok işe yarıyor!"
)
if st.button("🔍 Analiz Et", use_container_width=True):
    if text_input.strip() == "":
        st.warning("⚠️ Lütfen bir metin girin.")
    else:
        positive, negative, sentiment = analyze_sentiment(text_input)
        st.subheader("📊 Sonuçlar")
        if sentiment == "positive":
            st.success("😊 Pozitif bir metin!")
        elif sentiment == "negative":
            st.error("😞 Negatif bir metin!")
        else:
            st.info("😐 Nötr bir metin.")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("✅ Pozitif Skor", f"{positive:.0%}")
        with col2:
            st.metric("❌ Negatif Skor", f"{negative:.0%}")
        st.write("**Pozitif Oranı:**")
        st.progress(positive)
        st.write("**Negatif Oranı:**")
        st.progress(negative)