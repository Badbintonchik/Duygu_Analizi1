import streamlit as st
import requests
from requests.exceptions import ConnectionError

st.set_page_config(page_title="AI Sentiment Analyzer")

st.title("🧠 Yapay Zeka Duygu Analizi")
st.write("Metnin duygu durumunu yapay zeka ile analiz edin.")

text_input = st.text_area(
    "Analiz edilecek metni girin:",
    height=150
)

API_URL = "http://127.0.0.1:8000/predict"

if st.button("Analiz Et"):
    if text_input.strip() == "":
        st.warning("Lütfen bir metin girin.")
    else:
        try:
            with st.spinner("Analiz ediliyor..."):
                response = requests.post(
                    API_URL,
                    json={"text": text_input},
                    timeout=10  # Add timeout to prevent hanging
                )

            if response.status_code == 200:
                result = response.json()
        
                st.subheader("📊 Sonuçlar")
                
                # Create two columns for better display
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Pozitif", f"{result['positive']:.2%}")
                with col2:
                    st.metric("Negatif", f"{result['negative']:.2%}")
                
                # Show progress bar
                st.subheader("Duygu Skoru")
                st.progress(result["positive"])
                
                # Add a gauge-like visualization
                if result["positive"] > 0.6:
                    st.success("✨ Pozitif duygu ağırlıklı")
                elif result["positive"] < 0.4:
                    st.error("🌧️ Negatif duygu ağırlıklı")
                else:
                    st.info("😐 Nötr duygu")
                    
            else:
                st.error(f"Sunucu hatası: {response.status_code}")
                
        except ConnectionError:
            st.error("🔴 Backend sunucusuna bağlanılamıyor! Lütfen FastAPI sunucusunun çalıştığından emin olun.")
            st.info("📌 Çözüm: Ayrı bir terminalde 'python api.py' komutunu çalıştırın.")
        except Exception as e:
            st.error(f"Beklenmeyen bir hata oluştu: {str(e)}")

# Add helpful information in the sidebar
with st.sidebar:
    st.header("ℹ️ Yardım")
    st.write("""
    **Nasıl kullanılır:**
    1. Metin girişi yapın
    2. 'Analiz Et' butonuna tıklayın
    3. Sonuçları görüntüleyin
    
    **Not:** Backend sunucusunun çalıştığından emin olun.
    """)
    
    # Check backend status
    try:
        health_check = requests.get("http://127.0.0.1:8000", timeout=2)
        st.success("✅ Backend bağlantısı başarılı")
    except:
        st.error("❌ Backend bağlantısı yok")