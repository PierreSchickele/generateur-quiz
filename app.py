import streamlit as st

question = "En SQL, quel mot-clé permet d'obtenir de la donnée ?"
answers = ["SELECT", "GET", "RETRIEVE", "OBTAIN"]
good_answer = "SELECT"

st.write("# Générateur de quiz")
st.write("## Question 1")
st.write(question)

buttons = st.columns([1, 1, 1, 1])

est_correct = False
est_incorrect = False
for col in range(4):
    with buttons[col]:
        if st.button(answers[col]):
            est_correct = answers[col] == good_answer
            est_incorrect = not est_correct

if est_correct:
    st.write("C'est la bonne réponse !")

if est_incorrect:
    st.write("Ce n'est pas la bonne réponse...")