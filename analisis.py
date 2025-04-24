import streamlit as st
from textblob import TextBlob
from googletrans import Translator

translator = Translator()

# Título Principal
st.markdown("<h1 style='color: red;'>Análisis de Sentimiento con tu amigo y vecino Spider-man</h1>", unsafe_allow_html=True)

# Subtítulo
st.markdown("<h3 style='color: blue;'>Escribe una frase para analizar su polaridad y subjetividad</h3>", unsafe_allow_html=True)

# Barra lateral con info
with st.sidebar:
    st.markdown("<h3 style='color: blue;'>¿Qué significa esto?</h3>", unsafe_allow_html=True)
    st.markdown("""
    **Polaridad:**  
    Indica si el sentimiento es positivo (1), negativo (-1) o neutral (0).

    **Subjetividad:**  
    Mide si el texto es más emocional (1) o más objetivo (0).
    """)

# Expansor análisis de sentimientos
with st.expander('🔍 Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('✍️ Escribe aquí tu texto en español:')
    
    if text1:
        # Traducir texto
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write(f'🔸 **Polaridad:** {polarity}')
        st.write(f'🔸 **Subjetividad:** {subjectivity}')

        # Mostrar emoción con emojis animados (GIFs)
        if polarity >= 0.5:
            st.success("😊 ¡Espectacular como Spider-man! Manteniendo la vibra positiva ¡Sigue así!")
            st.image("https://i.pinimg.com/originals/31/94/e6/3194e670373f841b65b266d38bcd902f.gif", width=150)  # feliz
            st.balloons()

        elif polarity <= -0.5:
            st.error("😔 Tienes como... negatividad saliéndote de los poros. ¡Ánimo! No queremos un segundo Duende Verde :/")
            st.image("https://i.pinimg.com/originals/54/3b/85/543b85eb58783aa60e05bac18961eb53.gif", width=150)  # triste

        else:
            st.warning("😐 Emmmm... Escuchamos y no juzgamos, pero me faltó como más sazón, algo neutral está, bro.")
            st.image("https://64.media.tumblr.com/5710a90d7b5e95d13132163b10db7644/74e02ff4a6def3c0-cc/s540x810/56381fc63c713efa309150a7cb69c8e47166da6b.gifv", width=150)  # neutral cute

# corrección de inglés
with st.expander('✏️ Corrección ortográfica en inglés'):
    text2 = st.text_area('Escribe tu texto en inglés:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        corrected = blob2.correct()
        st.markdown("✅ Texto corregido:")
        st.write(corrected)
