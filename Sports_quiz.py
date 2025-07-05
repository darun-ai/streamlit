import streamlit as st

# Title
st.title("🏆 Sports Quiz App")
st.subheader("Test your sports knowledge!")

# Questions
quiz = [
    {
        "question": "1️⃣ Who won the 2023 Cricket World Cup?",
        "options": ["India", "Australia", "England", "New Zealand"],
        "answer": "Australia"
    },
    {
        "question": "2️⃣ How many players are on a football (soccer) team on the field?",
        "options": ["9", "10", "11", "12"],
        "answer": "11"
    },
    {
        "question": "3️⃣ Who has won the most Olympic gold medals?",
        "options": ["Usain Bolt", "Michael Phelps", "Mark Spitz", "Carl Lewis"],
        "answer": "Michael Phelps"
    },
    {
        "question": "4️⃣ What country hosted the FIFA World Cup in 2022?",
        "options": ["Qatar", "Russia", "Brazil", "Germany"],
        "answer": "Qatar"
    },
    {
        "question": "5️⃣ Which Indian player is known as the 'God of Cricket'?",
        "options": ["Virat Kohli", "MS Dhoni", "Kapil Dev", "Sachin Tendulkar"],
        "answer": "Sachin Tendulkar"
    }
]

# Store user answers
score = 0
user_answers = []

# Loop through questions
for q in quiz:
    st.markdown(f"### {q['question']}")
    user_answer = st.radio("Choose your answer:", q["options"], key=q["question"])
    user_answers.append((q["question"], user_answer, q["answer"]))

# Submit button
if st.button("Submit Quiz"):
    st.write("## 📝 Results")
    for question, user_ans, correct_ans in user_answers:
        if user_ans == correct_ans:
            st.success(f"✅ {question} — Your answer: {user_ans}")
            score += 1
        else:
            st.error(f"❌ {question} — Your answer: {user_ans}, Correct: {correct_ans}")

    st.info(f"🎯 Your total score: **{score} / {len(quiz)}**")
