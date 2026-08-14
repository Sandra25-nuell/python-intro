from quiz_data import get_questions
import random, datetime

question_bank = get_questions()

#print(question_bank)

random.shuffle(question_bank)
print("=" * 60)
print (" ")
print(question_bank)


question_only = []
answers_only = []
user_response = []

for question in question_bank:
    #print(question[0])
    question_only.append(question[0])
    answers_only.append(question[1])

    print(question_only)
    print(answers_only)

def ask(question):
    response = input(f"{question} :")
    return response

while True:
    for que in question_bank:
     ans = ask(que)
    user_response.append(ans)


    break
#correct = 0 

#incorrect = 0

for i, corr_ans in enumerate(answers_only):
    for resp in user_response:
        if resp == corr_ans:
            print("correct")
            correct += 1
        else:
           print("incorrect")
           incorrect += 1

        #if i > 5:
            #break
# calculate score and percentage
score = correct 
percentage = round((correct / len(question_only)) * 100, 2)
#Get timestamp
timestamp = datetime.datetime.now()

#Display results
print("====== QUIZ RESULT ======")
print("Score:", score, "/", len(question_only))
print("Correct answers:,", correct)
print("Incorrect answers:", incorrect)
print("Percentage:", percentage, "%")
print("Session timestamp:", timestamp.strft("%d/%m/%y"))