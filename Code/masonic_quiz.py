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
        ("What are the three great lights?", ["The Holy Bible, Square, Compass", "The trestle board, burning tapers", "The square, plumb, level", "The sun, moon, Worshipful Master"], "a", "These represent the spiritual and moral guidance of Masonry."),
        ("As an Entered Apprentice, from whence you came?", ["Egypt", "Lodge of H.B. Turner", "Lodge of Due Guard", "Lodge of the Holy Saints John"], "d", "This reflects the symbolic origin from the East, the source of Masonic light."),
        ("What came you here to do?", ["To seek light", "To improve my passions", "To subdue my passions and improve myself in Masonry", "To learn secrets"], "c", "This describes the aspirational goals of the candidate."),
        ("Then I presume you are a Mason?", ["I am so taken and acknowledged", "I am", "I received the light", "I'm cautious"], "a", "This is the accepted answer in the ritualistic dialogue."),
        ("What makes you a Mason?", ["The Bible", "My Obligation", "My Word", "God's Word"], "b", "The obligation is central to becoming a Mason."),
        ("How do you know yourself to be a mason?", ["I know my penalty and signs", "Tried and never denied", "I know my obligation", "I have grip, token, and sign"], "b", "This phrase confirms recognition among Masons."),
        ("How shall I know you to be a mason?", ["Tried and never denied", "Recognized by brothers", "Subduing passions", "Signs, token, word, and entrance"], "d", "This line summarizes means of Masonic verification."),
        ("What are signs?", ["Bible, Square, Compass", "Grip called due guard", "Right angles and perpendiculars", "Three burning tapers"], "c", "This describes the symbolic geometric meaning."),
        ("What is a token?", ["Password from St. John", "Square, level, plumb", "Grip to identify in dark/light", "Your apron"], "c", "Tokens are grips used for recognition in Masonry."),
        ("What do you conceal?", ["My signs and tokens", "My obligation", "All secrets except rightful", "Bible, square, compass"], "c", "Masons are obliged to conceal the secrets of the Craft."),
        ("What is the first degree called?", ["Entered Apprentice", "Fellow Craft", "Master Mason", "Initiate"], "a", "The first degree is foundational in Masonry."),
        ("What do the three lesser lights represent?", ["Sun, Moon, and Worshipful Master", "Faith, Hope, and Charity", "East, West, and South", "Wisdom, Strength, Beauty"], "a", "These represent guidance from above and leadership within the lodge."),
        ("Where were you prepared to be made a Mason?", ["In a room adjoining the Lodge", "In the West", "In the Outer Chamber", "At the Altar"], "a", "The candidate is prepared outside the lodge before initiation."),
        ("How were you prepared?", ["Divested of metals, hoodwinked, and cable-tow about the neck", "Dressed in a white robe", "Wearing gloves and apron", "With Masonic ring"], "a", "The preparation symbolizes humility and equality."),
        ("What is the covering of a Lodge?", ["A clouded canopy or star-decked heaven", "A blue ceiling", "A black curtain", "The altar"], "a", "This represents the celestial canopy under which the lodge meets."),
        ("What is the jewel of an Entered Apprentice?", ["Twenty-four inch gauge", "Plumb", "Level", "Trowel"], "a", "This tool teaches proper division of time."),
        ("Where does the Worshipful Master sit?", ["In the East", "In the West", "In the South", "In the North"], "a", "The East represents light and direction in the lodge."),
        ("Why are you hoodwinked?", ["To represent darkness before receiving light", "To protect your identity", "To humble yourself", "To keep secrets"], "a", "The hoodwink symbolizes moral darkness before enlightenment."),
        ("How should a Mason act?", ["With upright conduct", "With boldness", "With secrecy", "With joy"], "a", "Masons are taught to act uprightly in all aspects of life."),
        ("What is a Cable-tow?", ["A rope used in the ceremony", "A Masonic badge", "A tracing board", "A building tool"], "a", "The cable-tow symbolizes binding to the obligations of Masonry."),
        ("What is the first duty of an Entered Apprentice?", ["To seek light", "To pay dues", "To vote", "To memorize ritual"], "a", "The pursuit of light is the fundamental aim of Masonry."),
        ("What is the flooring of a Lodge called?", ["Mosaic pavement", "Tracing board", "Working floor", "Sacred space"], "a", "The mosaic pavement represents the ground floor of King Solomon’s Temple."),
        ("Why do you wear a lambskin apron?", ["Badge of a Mason", "Symbol of labor", "Tool of work", "Representation of purity"], "a", "It is the badge of a Mason and symbolizes innocence."),
        ("Where were you first prepared to be made a Mason?", ["In my heart", "In the anteroom", "In the lodge hall", "In the temple"], "a", "Spiritual readiness begins within one's own heart."),
        ("What moral lesson is taught by the 24-inch gauge?", ["To divide your time wisely", "To measure work precisely", "To construct the temple", "To teach geometry"], "a", "It teaches balance of duty, rest, and service."),
        ("What does the common gavel symbolize?", ["To remove the rough parts of character", "To command silence", "To signal the Master", "To raise a candidate"], "a", "It teaches moral refinement."),
        ("What are the principal tenets of Masonry?", ["Brotherly Love, Relief, and Truth", "Faith, Hope, and Charity", "Wisdom, Strength, Beauty", "Light, Duty, Honor"], "a", "These are the guiding principles of the Craft."),
        ("What is the Masonic word of the Entered Apprentice?", ["Boaz", "Jachin", "Mah-Hah-Bone", "Tubal-Cain"], "a", "Boaz represents strength."),
        ("What is the traditional penalty for violating your obligation?", ["Throat cut and tongue torn out", "Exile from lodge", "Loss of right hand", "Public shame"], "a", "It is a symbolic penalty emphasizing secrecy and integrity."),
        ("What are the working tools of an Entered Apprentice?", ["Twenty-four inch gauge and common gavel", "Plumb and level", "Trowel and setting maul", "Square and compasses"], "a", "These tools represent moral duties and personal improvement.")
    ],  # Full 30 EA questions will be inserted
    "Fellow Craft": [
        ("What is the wage of a Fellow Craft?", ["Corn, wine, oil", "Knowledge and wisdom", "Five orders of architecture", "Brotherly love, relief, truth"], "a", "These represent symbolic wages given for faithful service."),
        ("Where is the winding staircase?", ["Second degree lodge", "East side of the temple", "Between pillars", "Behind the altar"], "a", "The winding staircase symbolizes the spiritual journey of the Mason."),
        ("How many steps lead to the Middle Chamber?", ["3", "7", "15", "33"], "c", "Fifteen steps are symbolically ascended in the Fellow Craft degree."),
        ("What do the three steps represent?", ["Youth, manhood, age", "Faith, hope, charity", "Earth, wind, fire", "Heaven, earth, sea"], "a", "These represent the stages of life in a Mason's journey."),
        ("What are the five orders of architecture?", ["Doric, Ionic, Corinthian, Composite, Tuscan", "Greek, Roman, Gothic, Modern, Renaissance", "Arch, Pillar, Keystone, Truss, Beam", "Romanesque, Gothic, Doric, Ionic, Baroque"], "a", "These are classical orders that inspire Masonic structure and teaching."),
        ("What do the Seven Liberal Arts and Sciences represent?", ["Basis of Masonic education", "Masonic virtues", "Jewels of the Lodge", "Levels of initiation"], "a", "They form the educational foundation of Freemasonry."),
        ("Which art includes the study of speech?", ["Logic", "Rhetoric", "Grammar", "Astronomy"], "b", "Rhetoric is the art of persuasive and structured speech."),
        ("Which art involves mathematical principles?", ["Arithmetic", "Logic", "Grammar", "Astronomy"], "a", "Arithmetic is the science of numbers and their properties."),
        ("What does the Middle Chamber symbolize?", ["Temple of Solomon", "Masonic enlightenment", "Mystical gateway", "Spiritual reward"], "b", "It represents the internal chamber of knowledge and truth."),
        ("What tool represents upright conduct?", ["Plumb", "Level", "Square", "Compass"], "a", "The plumb teaches rectitude of conduct."),
        ("What is represented by the letter 'G'?", ["Geometry and God", "Generosity", "Greatness", "Grace"], "a", "It reminds Masons of the Great Architect of the Universe."),
        ("Why are stairs winding instead of straight?", ["To symbolize secrecy", "To confuse enemies", "To represent life’s journey", "To test endurance"], "c", "The winding form illustrates moral progression and life's twists."),
        ("Which pillar is associated with strength?", ["Boaz", "Jachin", "Solomon", "Moses"], "a", "Boaz stands for strength, one of the two pillars."),
        ("What is the purpose of the tracing board?", ["To instruct", "To sign in", "To record minutes", "To show dues"], "a", "It is a visual aid for learning Masonic lessons."),
        ("What adorns the porch of King Solomon’s Temple?", ["Two pillars", "A triangle", "A lion and eagle", "A veil"], "a", "The two pillars Boaz and Jachin adorn the porch."),
        ("What are the three principal supports of Masonry?", ["Wisdom, Strength, Beauty", "Faith, Hope, Charity", "Brotherly Love, Relief, Truth", "Square, Level, Plumb"], "a", "These support the structure and teachings of Masonry."),
        ("What does Grammar teach a Mason?", ["Proper speech and writing", "Geometry", "Symbolism", "Number theory"], "a", "Grammar enhances communication and expression."),
        ("What does Logic help a Mason discern?", ["Truth from error", "Faith", "Secret meanings", "Time and space"], "a", "It sharpens reasoning and judgment."),
        ("What does Music represent?", ["Harmony in life", "Ritual tones", "Sound science", "Worship melodies"], "a", "Music symbolizes harmony in thought and action."),
        ("What does Astronomy teach the Mason?", ["Order of the heavens", "Astrological secrets", "Constellations", "Sun worship"], "a", "It inspires awe at divine order and harmony."),
        ("What is a Fellow Craft's duty?", ["To seek knowledge and light", "To memorize secrets", "To travel to the Middle Chamber", "To assist the Master Mason"], "a", "A Fellow Craft seeks enlightenment."),
        ("What virtue is central to the second degree?", ["Study and industry", "Charity", "Silence", "Obedience"], "a", "Learning is emphasized as a moral duty."),
        ("What represents balance in a Mason's life?", ["Level", "Plumb", "Trowel", "Gavel"], "a", "The level teaches equality and balance."),
        ("What does the Fellow Craft seek?", ["Wages in the Middle Chamber", "Glory", "Master's secret", "Masonic title"], "a", "His symbolic journey ends in reward."),
        ("What is the password for the second degree?", ["Shibboleth", "Boaz", "Jachin", "Tubal Cain"], "a", "Shibboleth is the word of passage for FC."),
        ("What do the 15 steps represent collectively?", ["Progressive growth", "Test of endurance", "Secrets of geometry", "Star wisdom"], "a", "They embody steady advancement toward knowledge."),
        ("What do the arts and sciences develop?", ["Moral and mental faculties", "Temple tools", "Pillar placement", "Sacred geometry"], "a", "They nurture intellect and virtue."),
        ("What sense is most emphasized in FC?", ["Hearing", "Sight", "Smell", "Taste"], "a", "Hearing is vital for learning and ritual."),
        ("What does the staircase ascend to?", ["Middle Chamber", "Third Degree", "Heaven", "Temple altar"], "a", "It symbolizes the journey to wisdom and reward.")
    ],       # Full 30 FC questions will be inserted
    "Master Mason": [
        ("Who was Hiram Abiff?", ["Architect of King Solomon’s Temple", "First Grand Master", "Builder of the Ark", "Keeper of the Temple Scrolls"], "a", "He is the chief architect in Masonic legend representing fidelity."),
        ("What are the three Ruffians’ names?", ["Jubela, Jubelo, Jubelum", "Abiram, Aholiab, Jehoash", "Tyrus, Sidon, Judah", "Jubal, Tubal, Lamech"], "a", "These characters represent betrayal in Masonic teachings."),
        ("What does the sprig of acacia symbolize?", ["Immortality", "Brotherhood", "New beginnings", "Secrecy"], "a", "It symbolizes the soul's immortality."),
        ("What is the significance of the Lion’s Paw?", ["Grip used in raising a Master Mason", "Symbol of courage", "Mark of strength", "Jewelry emblem"], "a", "It is the strong grip that raises a fallen brother."),
        ("What does the Master’s Word represent?", ["Divine truth", "Lost knowledge", "Power", "Royalty"], "b", "It signifies knowledge once possessed but now concealed."),
        ("What is the emblem of the third degree?", ["Square and Compass", "Skull and Crossbones", "Trowel", "Sprig of Acacia"], "d", "It denotes immortality of the soul."),
        ("How was Hiram Abiff killed?", ["Struck by three blows", "Poisoned in the temple", "Drowned in the well", "Stabbed by guards"], "a", "The three Ruffians killed him with symbolic tools."),
        ("Where was Hiram Abiff buried?", ["Under the temple", "Near Mount Moriah", "In the rubbish of the temple", "In the forest"], "c", "He was buried hastily in the temple debris."),
        ("What do the three steps after raising symbolize?", ["Life, death, rebirth", "Wisdom, strength, beauty", "Mind, body, spirit", "Manhood, strength, age"], "a", "These represent the human journey."),
        ("What is the substitute word in the third degree?", ["Mah-Ha-Bone", "Hiramic Light", "Jah-Bul-On", "Tubal Cain"], "a", "It stands in place of the lost Master’s Word."),
        ("What lesson does the grave teach the Mason?", ["Mortality and resurrection", "Work hard in life", "Knowledge is power", "Justice is eternal"], "a", "The grave emphasizes the reality of death and hope of resurrection."),
        ("What is the duty of a Master Mason?", ["Preserve Masonic secrets", "Protect the Lodge", "Travel abroad", "Write Masonic texts"], "a", "He must keep the ancient landmarks of the order."),
        ("What jewel is worn by the Worshipful Master?", ["Square", "Trowel", "Level", "Plumb"], "a", "It represents moral rectitude and justice."),
        ("What does the broken column represent?", ["Untimely death of Hiram", "Wisdom destroyed", "End of journey", "Beginning of rebirth"], "a", "It marks Hiram's death before his work was finished."),
        ("What do the three ruffians demand of Hiram?", ["The secrets of a Master Mason", "The Ark of the Covenant", "The Holy Writings", "The plans of the temple"], "a", "They sought the Master’s secrets unlawfully."),
        ("Why is Hiram Abiff considered a martyr in Masonry?", ["He died keeping the secrets", "He built the temple", "He was betrayed", "He taught geometry"], "a", "His refusal to betray Masonic secrets cost him his life."),
        ("What do the three blows to Hiram signify?", ["Ignorance, fear, and tyranny", "Passion, fear, and death", "Mind, body, and soul", "The three degrees"], "a", "They symbolize attacks on truth and integrity."),
        ("How is a Master Mason raised?", ["By the Lion's Paw", "By the Worshipful Master", "By the Ruffians", "By ritual prayer"], "a", "He is symbolically raised by the grip of the Lion’s Paw."),
        ("Why is the Master's Word lost?", ["Due to Hiram's death", "Hidden in the temple", "Replaced by a substitute", "Only known by kings"], "a", "It was lost with the death of Hiram."),
        ("What replaces the lost word?", ["A substitute word", "The square", "A pillar", "A secret grip"], "a", "A substitute is used until the true word is recovered."),
        ("What does the trowel symbolize?", ["Spreading brotherly love", "Marking stones", "Justice", "Foundation"], "a", "It spreads the cement of brotherly love."),
        ("What is the significance of the temple’s unfinished state?", ["Man's imperfect life", "Time’s limitation", "Solomon’s design", "Death"], "a", "It represents the incompleteness of human endeavor."),
        ("Who discovered Hiram’s grave?", ["Twelve Fellow Crafts", "Three Ruffians", "King Solomon", "Jubela"], "a", "They found the body by following clues from the temple."),
        ("What was found at the grave site?", ["Sprig of acacia", "Sword", "Parchment", "Jewel"], "a", "The sprig symbolized the place of burial and immortality."),
        ("How is secrecy emphasized in this degree?", ["Through the penalty and burial legend", "By silence", "By signs", "By symbols"], "a", "The legend of Hiram reinforces secrecy."),
        ("What does the 'raising' represent spiritually?", ["Resurrection and moral awakening", "Learning a secret", "Gaining authority", "Promotion in rank"], "a", "It is a symbol of spiritual rebirth."),
        ("Why are there three ruffians?", ["To represent temptation", "To represent trials", "To represent flaws in man", "To tell the legend"], "a", "They symbolize moral failings."),
        ("What virtue is tested in the third degree?", ["Fidelity", "Humility", "Obedience", "Knowledge"], "a", "Fidelity is key, shown by Hiram’s death."),
        ("Why does a Mason reflect on mortality?", ["To lead a better life", "To earn rewards", "To recall the past", "To honor ancestors"], "a", "Contemplating death urges moral living."),
        ("What is the moral lesson of Hiram’s story?", ["Stand firm in principle", "Obey superiors", "Hide secrets", "Build grand works"], "a", "He chose death over betrayal."),
        ("How is the grave a symbol in this degree?", ["It reminds us of death and resurrection", "It marks the past", "It protects secrets", "It ends the journey"], "a", "It highlights Masonry's teachings on immortality."),
        ("Why is the number three important in this degree?", ["It reflects the three Ruffians and three blows", "It is a mystical number", "It marks rank", "It refers to three kings"], "a", "The number three is symbolic throughout the legend.")
    ]        # Full 30 MM questions will be inserted
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
    q_text, opts, correct_letter, *explanation = q_list[q_idx]

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

        explanation_text = explanation[0] if explanation else ""

        st.session_state.user_answers.append({
            "question": q_text,
            "selected": selected or "(No answer)",
            "correct": correct_text,
            "result": "✅ Correct" if is_correct else "❌ Incorrect",
            "explanation": explanation_text
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
        if ans['explanation']:
            st.info(f"📘 Explanation: {ans['explanation']}")
        st.markdown("---")

    if st.button("Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
