quiz = {
    "question1": {
        "question" : "who is the father of statistics",
        "answer" : "RA Fisher"
    },
    "question2" : {
        "question" : "who is father of statistics in India",
        "answer" : "PC Mahalanobis"
    }
}


def quiz_time():
    score = 0
    for key, value in quiz.items():
        print(value["question"])
        answer = input("Your answer: ")
        if answer.lower() == value["answer"].lower():
            score = score + 1
            print("your answer is correct and your score is " + str(score))
            print("")
        else:
            print("your answer is incorrect and your score is " + str(score))
        print("your scored " + str(int(score / 2 * 100)) + "%")

if __name__ == "__main__":
    quiz_time()


redo = input("entry t to try again: ")
if redo == "t":
    quiz_time()
else:
    quit()
