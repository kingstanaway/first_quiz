class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = str(prompt)
        self.options = options
        self.answer = str(answer)

    def print_question(self):
        print(self.prompt)

        letters = ["a", "b", "c", "d", "e"]
        x = 0

        for option in self.options:
            print("(" + letters[x] + ") " + str(option))
            x += 1

        print("")

    def guess_answer(self):
        ans = str(input("Enter answer: "))
        if ans.lower() == self.answer.lower():
            return True
        else:
            return False

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_questions(self, questions):
        self.questions = questions

    def start_quiz(self):
        for question in self.questions:
            question.print_question()
            was_correct_answer = question.guess_answer()

            if was_correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print("Wrong!\n")

        print("You got " + str(self.score) + "/" + str(len(self.questions)) + "!")