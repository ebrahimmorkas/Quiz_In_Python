import questions as q
class play_game:
    category = ""
    # Will be used when we have to display questions of specific category
    quiz_questions = None
    # Creating the object of questions.py class
    ques = q.Questions()
    # Creating the counter that will be useful while iterating the list option_number that is created just below
    options_counter = 1
    # Creating the llist that will contain the option numbers
    options_number = ['A', 'B', 'C', 'D']
    # Function that will print all the categories from the questions.py file
    def print_categories(self):
        # ques = q.Questions()
        print(self.ques.list_of_category)

    # Function that will help user to select the category
    def select_category(self):
        self.category = input("Please select the anyone category displayed above")

    # Function that will help to select the questions from questions.py based on the category selected by the user
    def select_questions_based_on_category(self):
        counter = 1

        # Checking whether the category entered by the user exists or not
        if self.category in self.ques.list_of_category:
            # print("It is present")


            # This code is taken by chatgpt for selecting the questions based on some category the question entered in chatgpt was :"First we had pasted the list that was created in questions.py and then we had asked this in the same question 'From this list i only want the part that is associated with Indian History'" and ofcourse we had made some changes to make it dynamic because chatgpt has given code only for Indian History and if you want to see what has been changed than again paste the question in chatgpt and then compare it with this code
            for topic_dict in self.ques.list_of_questions:
                if self.category in topic_dict:
                    self.quiz_questions = topic_dict[self.category]
                    break
            for questions_and_options in self.quiz_questions:
                print(f"Question no {counter}")
                counter+=1
                # Fetching the list of opions
                list_of_options = questions_and_options['options']
                # print(list_of_options)
                print(questions_and_options['question'])
                # Printing the options
                for options in list_of_options:
                    print(f"{self.options_number[self.options_counter]}. {options}")
            # print(self.quiz_questions)
        else:
            # print("It is not present")
            self.select_category()


game = play_game()
game.print_categories()
game.select_category()
game.select_questions_based_on_category()
print(game.category)

