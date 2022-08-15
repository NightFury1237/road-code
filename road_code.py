"""
File: Road_code.py
Author: Cohen Fourie 
Date:
Description:
"""
import os



def get_questions():
    questions = {
        "When coming up to a pedestrian crossing without a raised traffic island, what must you do?":
        {
            "options":
            [
                "Stop and not over take other vehicles. ",
                "Ride on if pedestrian's are not on your side of the road.",
                "Stop and over take if vehicle is to slow, as well as if pedestrian is not on your side of the road. "
            ],
            "answer": 1,
        },
        "When driving at night on a road with lanes you must be able to stop in half the length of clear road you can see in front of you.":
        {   
            "options": 
            [
                "True",
                "False"
            ],
            "answer": 2,
        },
        "What should you do when you are coming up to traffic signals and the signals change from green to yellow?":
        {    
            "options":
            [
                "slow to a stop and wait for green ",
                "Speed up to cross before the red light"
            ],
            "answer": 1,
        
        },
        "You MUST dip the headlights on your vehicle when:":
        {
            "options":  
            [
                "When driving on a whinding road",
                "When following others"
            ],
            "answer": 1,
        },
        "What may you do at traffic signals if there is a green arrow pointing to the right and a red light showing at the same time?":
        {
            "options":
            [
                "You may turn to the right",
                "You must stop either way if there is a red light ",
                "You may turn to the left or go straight on"
            ],
            "answer": 1,
        },
        "If you have a learner licence can you carry passengers?":
        {
            "options":
            [
                "You may carry passengers but your supervisor has to agree as they will be responsible for them.",
                "You may if you take care and responsibility for how you drive."
            ],
            "answer": 1,
        },
        "What lights should you use if your vehicle has broken down and is being towed?":
        {
            "options": 
            [
                "hazard lights ",
                "any lights you have"
            ],
            "answer": 1,
        },
        "What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)":
        {
            "options": 
            [
                "80 km",
                "100 km",
                "60 km"
            ],
            "answer": 1,
        },
        "When turning right from a two-laned road into a one-way street that has two lanes, you must turn into the:":
        {
            "options": 
            [
                "right hand lane",
                "left hand lane, so big vechiles can pass on the right"
            ],
            "answer": 1,
        },
        "When coming up to a roundabout you must give way to all vehicles that will cross your path from your left?":
        {
            "options":
            [
                "True",
                "False"
            ],
            "answer": 2,
        },
    }

    return questions
def clear_screen():
    os.system("cys")

def show_main_menu():
    # First Menu which will ask whether user wants to continue or choose a different road code test

    print("""Hello, welcome to Cohen's Road Code test. Please choose an option below either 1, 2 or 3 (please input in numerical form)
    1) Run road code program, where you'll answer 10 questions and have a score 
    2) Run road code test, until you get 1 question wrong out of 10 questions
    3) EXIT """)


def ask_user_response():
    # Asking for users answer for first menu

    User_Menu_Choice = input("What is your choice?\n")
    return User_Menu_Choice


def validate_user_response(menu_response):
    # Validating users response for main menu and ch

    
    if menu_response == "1" or menu_response == "2" or menu_response == "3":
        return menu_response
    else:
        print("Invalid try again, please enter a valid number!")
        return "error"

    


def main():


    show_main_menu()
    
    
    menu_response = ask_user_response()
    validated_response = validate_user_response(menu_response)

    while (validated_response == "error"):
        menu_response = ask_user_response()
        validated_response = validate_user_response(menu_response)

    print("the user chose: " + validated_response)

    score = 0

    questions = get_questions()
    if validated_response == "1":
        for question in questions.keys():
            print(question)
            options = questions[question]["options"] 
            for index in range(len(options)):
                option = options[index]
                print(str(index + 1) + ")  " + option)
                
            answer = questions[question]["answer"]
            print(answer)
            users_answer = input("What is the answer?\n")

            if users_answer == answer: 
                score = score + 1
            
            valid_user_answers = index
            if users_answer != valid_user_answers: 
                print("Invalid response you can only enter, the numerical value of options")

            #clear_screen()

            
    print(score)

main()
