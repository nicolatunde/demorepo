# Hardcode Questions and Keywords:
# Create at least 5 theory questions.
# For each question, determine the essential keywords or phrases that should be included in the ideal answer.
# Assign weights to each keyword based on its importance.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Evaluate the user's answers based on the presence of the specified keywords..
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score out of the max score e.g. 10/12.
score = 0
i = 1
full_mark = 0
question_bank = [{"question": "whats photosynthesis", "keywords": ["process", "plants", "green", "organisms", "energy"], "heavykeywords": ["photosynthesis", "transform", "chemical"]},
                 {"question": "whats matter", "keywords": ["matter", "anything", "space"], "heavykeywords": ["weight"],},
                 {"question": "whats Heisenberg principle", "keywords": ["limit", "known"], "heavykeywords": ["momentum", "simulteneosly"]},
                 {"question": "State newton third law of motion", "keywords": ["action", "equall", "opposite"], "heavykeywords":["reaction"]},
                 {"question": "whats culture", "keywords": ["way",  "life", "culture"], "heavykeywords": ["people"]}
                 ]
for question in question_bank:
    print(question["question"])
    answer = input().split(" ") # photosynthesis is process of getting blabla bla and also the process
    for word in answer:
        if word in question["keywords"]:
            score += 1
        elif word in question["heavykeywords"]:
            score += 2
    full_mark += ((len(question["keywords"])) + (len(question["heavykeywords"])*2))

print(f"Total score is {score} out of {full_mark}")
if score > full_mark /2:
    remark = "Credict"

elif score < (full_mark /2) and score > (full_mark/2.22):
    remark = "pass"

else:
    remark = "opps you failed the exam"
print(remark)
