import streamlit as st
from tempfile import NamedTemporaryFile

st.title("Audio Transcription App")

# File uploader allows user to add M4A file
uploaded_file = st.file_uploader("Upload an M4A audio file", type=["m4a"])
if uploaded_file is not None:
    # Save the uploaded audio file to a temporary file
    with NamedTemporaryFile(delete=False, suffix=".m4a") as tmp:
        tmp.write(uploaded_file.getvalue())
        audio_file_path = tmp.name

    # Display the audio file player
    st.audio(uploaded_file)

# Selection between "Large" and "Small"
model_size = st.selectbox("Select Model Size", ["Large", "Small"])

# Text input for output file name
output_file_name = st.text_input("Specify the name of the output file")

# Button to start transcription
if st.button("Transcribe Audio"):
    if uploaded_file is not None and model_size and output_file_name:
        # Depending on the model size selection, load the appropriate model
        # if model_size == "Large":
        #     model = whisper.load_model("large")
        # else:
        #     model = whisper.load_model("tiny")

        # # Transcribe the audio
        # result = model.transcribe(audio_file_path)

        # Display the transcription
        st.text_area("Transcription", value="text", height=300)
    else:
        st.error("Please upload a file and specify all options.")
