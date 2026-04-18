import streamlit as  st
from api_calling import note_generator, audio_generarton, quiz_generation
from PIL import Image


st.title("Note Summary and Quiz Generator", anchor=None)
st.subheader("Upload upto 3 image and see magic!")
st.divider()

with st.sidebar:
    st.header("Upload you images: ")
    picture = st.file_uploader("Select photos:",
                     type=["jpg", "jpeg", "png"],
                     accept_multiple_files=True)
    size = len(picture)
    if picture:
        if (size > 3):
            st.warning("you should not upload more than 3 image")
        else:
            st.success("Your image uploaded successfully")
            cols = st.columns(size)
            for i, p in enumerate(picture):
                with cols[i]:
                    st.image(p)
    
    selected = st.selectbox(
        "Select dificulty:",
        ["Easy", "Medium", "Hard"],
        index=None
    )

    pressed = st.button("Submit", type="primary")

    pil_images =[]
    for i in range(len(picture)):
        image = Image.open(picture[i])
        pil_images.append(image)


if pressed:
    if not picture:
        st.error("You must upload image!")
    if not selected:
        st.error("You must have to select a dificulty options!")

    if picture and selected:

        with st.container(border=True):
            st.subheader("Your note: ")
            with st.spinner("AI is writing note for you.."):
                generated_note = note_generator(pil_images)
                st.markdown(generated_note)

        with st.container(border=True):
            with st.spinner("AI is making you audio.."):
                generated_note = generated_note.replace("#","")
                generated_note = generated_note.replace("*","")
                generated_note = generated_note.replace("-","")
                generated_note = generated_note.replace("","")


                generated_audio = audio_generarton(generated_note)
                st.subheader("Audio explanaion: ")
                st.audio(generated_audio)
        
        with st.container(border=True):
            st.subheader(f"Quiz {selected} level: ")
            with st.spinner("Preparing Quiz.."):
                generated_quiz = quiz_generation(generated_note, selected)
                st.markdown(generated_quiz)
    

