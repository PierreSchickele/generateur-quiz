import os
import logging
import subprocess

import duckdb
import streamlit as st
from random import shuffle

if "data" not in os.listdir():
    print("creating folder data")
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

if "questions.duckdb" not in os.listdir("data"):
    subprocess.run(["python", "init_db.py"])

conn = duckdb.connect(database="data/questions.duckdb", read_only=False)

question_id = "sql2"
question = (
    conn
    .execute(f"SELECT question_title "
             f"FROM questions_answers "
             f"WHERE question_name = '{question_id}' "
             f"LIMIT 1")
    .df()["question_title"]
    .iloc[0]
)
answers = (
    conn
    .execute(f"SELECT answer1,answer2,answer3,answer4 "
             f"FROM questions_answers "
             f"WHERE question_name = '{question_id}' "
             f"LIMIT 1")
    .df()[['answer1', 'answer2', 'answer3', 'answer4']]
    .iloc[0]
    .to_numpy()
)
good_answer = answers[0]

conn.close()

st.write("# Générateur de quiz")
st.write(f"## Question {question_id}")
st.write(question)

buttons = st.columns([1, 1, 1, 1])

est_correct = False
est_incorrect = False
num_arr = list(range(4))
shuffle(num_arr)

for col, col2 in zip(num_arr, range(4)):
    with buttons[col2]:
        if st.button(answers[col]):
            est_correct = answers[col] == good_answer
            est_incorrect = not est_correct

if est_correct:
    st.write("C'est la bonne réponse !")
    st.write("La bonne réponse était :", good_answer)
if est_incorrect:
    st.write("Ce n'est pas la bonne réponse...")
    st.write("La bonne réponse était :", good_answer)
