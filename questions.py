class Questions:
    # Creating the list that will hold all the questions under different types such as history, geography and many more
    list_of_questions = [
        {"Indian History": [
            {"question": "The Battle of Plassey was fought in",
             "options":["1757", "1782", "1748", "1764"],
             "answer": "1757"},
            {"question": "The territory of Porus who offered strong resistance to Alexander was situated between the rivers of",
             "options":["Sutlej and Beas", "Jhelum and Chenab", "Ravi and Chenab", "Ganga and Yamuna"],
             "answer": "Jhelum and Chenab"}
            ]
        },
        {"Indian Geography": [
            {"question": "The Paithan (Jayakwadi) Hydro-electric project, completed with the help of Japan, is on the river",
             "options": ["Ganga", "Cauvery", "narmada", "godavari"],
             "answer": "godavari"},
            {"question": "The percentage of irrigated land in India is about",
             "options": ["45", "65", "35"," 25"],
             "answer": "35"}
        ]
        }
    ]
    # print(list_of_questions[0])
    # Creating the list that will hold the categories of the quiz that is "Indian History", "Indian Geography  and many more
    list_of_category = ["Indian History", "Indian Geography"]

    # This code has been pasted from chatgpt and the question was "First paste this list and then asked in the same question that 'how to iterate this list'"

    # for topic_dict in list_of_questions:
    #     for topic, questions_list in topic_dict.items():
    #         print(f"Topic: {topic}")
    #         for question_dict in questions_list:
    #             question = question_dict['question']
    #             options = question_dict['options']
    #             answer = question_dict['answer']
    #             print(f"Question: {question}")
    #             print("Options:", ", ".join(options))
    #             print(f"Answer: {answer}")
    #             print("------")
