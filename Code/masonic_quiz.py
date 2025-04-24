import streamlit as st
import time
import pandas as pd
import random
from datetime import datetime

# ---- ACCESS CODES ---- #
access_codes = {
    "Entered Apprentice": "255877",
    "Fellow Craft": "779311",
    "Master Mason": "85996170"
}

# ---- QUESTIONS ---- #
question_bank = {
    "Entered Apprentice": [
        ("What are the three great lights?", ["The Holy Bible, Square, Compass", "The trestle board, burning tapers", "The square, plumb, level", "The sun, moon, Worshipful Master"], "a"),
        ("As an Entered Apprentice, from whence you came?", ["Egypt", "Lodge of H.B. Turner", "Lodge of Due Guard", "Lodge of the Holy Saints John"], "d"),
        ("What came you here to do?", ["To seek light", "To improve my passions", "To subdue my passions and improve myself in Masonry", "To learn secrets"], "c"),
        ("Then I presume you are a Mason?", ["I am so taken and acknowledged", "I am", "I received the light", "I'm cautious"], "a"),
        ("What makes you a Mason?", ["The Bible", "My Obligation", "My Word", "God's Word"], "b"),
        # Additional EA Questions (sampled)
        ("What is the jewel of an Entered Apprentice?", ["Twenty-four inch gauge", "Plumb", "Level", "Trowel"], "a"),
        ("What is the covering of a Lodge?", ["A clouded canopy or star-decked heaven", "A blue ceiling", "A black curtain", "The altar"], "a"),
        ("Where does the Worshipful Master sit?", ["In the East", "In the West", "In the South", "In the North"], "a"),
        ("What do the three lesser lights represent?", ["Sun, Moon, and Worshipful Master", "Wisdom, Strength, and Beauty", "East, West, and South", "Faith, Hope, and Charity"], "a"),
        ("Why are you hoodwinked?", ["To represent darkness before receiving light", "To protect your identity", "To humble yourself", "To keep secrets"], "a"),
        ("How should a Mason act?", ["With upright conduct", "With boldness", "With secrecy", "With joy"], "a"),
        ("What is a Cable-tow?", ["A rope used in the ceremony", "A Masonic badge", "A tracing board", "A building tool"], "a"),
        ("What is the first duty of an Entered Apprentice?", ["To seek light", "To pay dues", "To vote", "To memorize ritual"], "a"),
        ("What is the flooring of a Lodge called?", ["Mosaic pavement", "Tracing board", "Working floor", "Sacred space"], "a"),
        ("Why do you wear a lambskin apron?", ["Badge of a Mason", "Symbol of labor", "Tool of work", "Representation of purity"], "a")
    ],
    "Fellow Craft": [
        ("What is the wage of a Fellow Craft?", ["Corn, wine, oil", "Knowledge and wisdom", "Five orders of architecture", "Brotherly love, relief, truth"], "a"),
        ("Where is the winding staircase?", ["Second degree lodge", "East side of the temple", "Between pillars", "Behind the altar"], "a"),
        # Additional FC Questions (sampled)
        ("What do the five senses represent in Masonry?", ["Ways of learning", "Degrees", "Working tools", "Temple pillars"], "a"),
        ("What is the importance of architecture in the 2nd degree?", ["Symbol of strength", "Foundation of Masonry", "Represents beauty", "Sign of completion"], "b"),
        ("What do the Seven Liberal Arts and Sciences represent?", ["Basis of Masonic education", "Masonic virtues", "Jewels of the Lodge", "Levels of initiation"], "a"),
        ("What is rhetoric?", ["The art of persuasive speech", "Study of geometry", "Style of clothing", "A tool of the Lodge"], "a"),
        ("What pillar is strength?", ["Boaz", "Jachin", "Solomon", "Moses"], "a"),
        ("What does the Level symbolize?", ["Equality", "Justice", "Wisdom", "Charity"], "a"),
        ("What does Grammar teach a Mason?", ["Proper speech and writing", "Geometric design", "Symbolism", "Order"], "a"),
        ("What does Arithmetic teach?", ["Number and measurement", "Prayer and patience", "Tools of a Mason", "Light"], "a"),
        ("How many steps to Middle Chamber?", ["15", "12", "7", "3"], "a"),
        ("What does Astronomy teach a Mason?", ["Order and harmony", "Zodiac symbols", "Faith and truth", "Travel"], "a"),
        ("What adorns the Porch of Solomon's Temple?", ["Two pillars", "A lion", "A globe", "Curtains"], "a"),
        ("What does the Plumb symbolize?", ["Uprightness", "Measurement", "Time", "Respect"], "a")
    ],
    "Master Mason": [
        ("Who was Hiram Abiff?", ["Architect of King Solomon’s Temple", "First Grand Master", "Builder of the Ark", "Keeper of the Temple Scrolls"], "a"),
        ("What are the three Ruffians’ names?", ["Jubela, Jubelo, Jubelum", "Abiram, Aholiab, Jehoash", "Tyrus, Sidon, Judah", "Jubal, Tubal, Lamech"], "a"),
        # Additional MM Questions (sampled)
        ("What does the trowel symbolize?", ["Spreading brotherly love", "Mortar of unity", "Tool of a Mason", "Secrecy"], "a"),
        ("What are Masonic landmarks?", ["Unchanging principles", "Temple stones", "Initiation rites", "Meeting places"], "a"),
        ("What does the broken column represent?", ["Untimely death of Hiram", "Wisdom destroyed", "End of journey", "Beginning of rebirth"], "a"),
        ("What is the significance of the grave?", ["Mortality and resurrection", "Secrets of life", "Path of light", "Time eternal"], "a"),
        ("What do the lion's paw and strong grip represent?", ["Raising from darkness", "Obligation", "Unity", "Reward"], "a"),
        ("What is the role of the Worshipful Master?", ["Preside over the Lodge", "Lead prayers", "Manage finances", "Teach songs"], "a"),
        ("What is the highest honor in Masonry?", ["Master Mason", "Worshipful Master", "Past Master", "Grand Master"], "a"),
        ("What is Mah-Ha-Bone?", ["Substitute word", "Ritual item", "Temple stone", "Code"], "a"),
        ("What is the setting of the 3rd degree?", ["Temple building site", "Outer court", "Lodge room", "East gate"], "a"),
        ("Who protects the secrets?", ["Master Masons", "Entered Apprentices", "Fellow Crafts", "All Brothers"], "a"),
        ("What is the Mason’s reward?", ["Light", "Obedience", "Wisdom", "Travel"], "a"),
        ("What is the apron a symbol of?", ["Service and labor", "Pride and ego", "Wisdom and strength", "Unity"], "a")
    ]
}

# ---- INITIAL STATE ---- #
for key, default in {
    'name': "",
    'degree': "Entered Apprentice",
    'quiz_started': False,
    'current_q': 0,
    'score': 0,
    'completed': False,
    'user_answers': [],
    'start_time': None,
    'shuffled_questions': None
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ---- CONFIG ---- #
st.set_page_config(page_title="Phoenix Nine Proficiency Exam", layout="centered")
st.title("🔥 Phoenix Nine Proficiency Exam")

# ---- START FORM ---- #
if not st.session_state.quiz_started:
    with st.form("start_form"):
        st.image("https://raw.githubusercontent.com/dreamchaserami/try-3/main/Images/phoenix9.png", width=350)
        st.session_state.name = st.text_input("Enter your name:")
        st.session_state.degree = st.selectbox("Select Degree Level:", list(question_bank.keys()))
        access_code = st.text_input("Enter access code for selected degree:")
        start_clicked = st.form_submit_button("Start Quiz")

        if start_clicked and st.session_state.name:
            correct_code = access_codes.get(st.session_state.degree)
            if access_code == correct_code:
                st.session_state.quiz_started = True
                st.session_state.start_time = time.time()
                st.session_state.shuffled_questions = {
                    deg: random.sample(questions, len(questions)) for deg, questions in question_bank.items()
                }
                st.success(f"Welcome Brother {st.session_state.name}, let's begin the {st.session_state.degree} quiz.")
                st.rerun()
            else:
                st.error("Invalid access code. Please try again.")

# ---- QUIZ LOOP ---- #
elif not st.session_state.completed:
    q_list = st.session_state.shuffled_questions[st.session_state.degree]
    q_idx = st.session_state.current_q
    q_text, opts, correct_letter = q_list[q_idx]

    st.image("https://raw.githubusercontent.com/dreamchaserami/try-3/main/Images/phoenix9.png", width=200)

    st.progress(q_idx / len(q_list))
    st.subheader(f"Question {q_idx + 1} of {len(q_list)}")
    st.write(q_text)

    selected = st.radio("Choose one:", opts, index=None, key=f"q_{q_idx}")

    time_limit = 30
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(0, time_limit - elapsed)
    st.info(f"⏱️ Time remaining: {remaining} seconds")

    if remaining == 0:
        st.warning("Time's up! Moving to the next question...")
        selected = None

    if st.button("Submit Answer"):
        correct_text = opts[ord(correct_letter) - ord('a')]
        is_correct = selected == correct_text

        st.session_state.user_answers.append({
            "question": q_text,
            "selected": selected or "(No answer)",
            "correct": correct_text,
            "result": "✅ Correct" if is_correct else "❌ Incorrect"
        })

        if is_correct:
            st.session_state.score += 1

        st.session_state.current_q += 1
        st.session_state.start_time = time.time()

        if st.session_state.current_q >= len(q_list):
            st.session_state.completed = True

        st.rerun()

# ---- QUIZ COMPLETE ---- #
if st.session_state.completed:
    total = len(st.session_state.shuffled_questions[st.session_state.degree])
    st.success(f"{st.session_state.name}, you scored {st.session_state.score} out of {total}.")

    if st.session_state.score == total:
        st.balloons()
        st.info("Perfect knowledge!")
    elif st.session_state.score >= total // 2:
        st.info("Well done, keep studying!")
    else:
        st.warning("Keep learning, Brother. You’ll get there!")

    score_data = {
        "Name": st.session_state.name,
        "Degree": st.session_state.degree,
        "Score": st.session_state.score,
        "Total": total,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    df = pd.DataFrame([score_data])
    df.to_csv("masonic_scores.csv", mode='a', index=False, header=not pd.io.common.file_exists("masonic_scores.csv"))
    st.success("Your score has been saved.")

    st.markdown("### 🔍 Review Your Answers")
    for idx, ans in enumerate(st.session_state.user_answers):
        st.write(f"**Q{idx+1}:** {ans['question']}")
        st.write(f"- Your answer: {ans['selected']}")
        st.write(f"- Correct answer: {ans['correct']}")
        st.write(f"- Result: {ans['result']}")
        st.markdown("---")

    if st.button("Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
