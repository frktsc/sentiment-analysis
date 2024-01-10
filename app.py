import streamlit as st
from transformers import pipeline

emotion_labels = {
    'LABEL_0': 'Sadness',
    'LABEL_1': 'Joy',
    'LABEL_2': 'Love',
    'LABEL_3': 'Anger',
    'LABEL_4': 'Fear',
    'LABEL_5': 'Surprise'
}

emojis = {
    'Sadness': '😢',
    'Anger': '😠',
    'Fear':'😱',
    'Surprise':'😲',
}

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/frktsc/sentiment-analysis/blob/main/README.md',
        'About': "This app does sentiment analysis. For more information, please click on the 'get help' button in the triple dots in the upper right corner.."
    }
)



model_name = "frktsc/emotion" 
model = pipeline("sentiment-analysis", model=model_name)


st.title(" 🔥 Sentiment Analysis")

user_input = st.text_area("Enter text for sentiment analysis", "")


if st.button("Analyze"):
    
    results = model(user_input)
    
    
    for result in results:
        label = result['label']
        score = result['score']
        emotion = emotion_labels.get(label, "Unknown")  
        st.write(f"Emotion: {emotion}")
        st.write(f"Score: {score:.2f}")

        if emotion in ['Joy','Love']:
            st.success(f"It seems like the text expresses {emotion.lower()}.")
            st.balloons()
    

        if emotion in ['Sadness', 'Anger','Fear','Surprise']:
            emoji = emojis.get(emotion)
            st.markdown(f"<h1 style='text-align: center;'>{emoji}</h1>", unsafe_allow_html=True)
            st.error(f"It seems like the text expresses {emotion}.")
