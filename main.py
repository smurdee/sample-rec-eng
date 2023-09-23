import logging
import algos.personality_type as pt

def setup_logging():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s -  %(levelname)s - %(message)s')

def get_user_input():
    try:
        user_input = int(input("Enter your mode: "))
        return user_input
    except ValueError:
        logging.error("Invalid input", stack_info=True)
        print("Invalid input. Please try again.\n")

def admin_config():
    print("Admin configuration\n")
    # Add admin configuration logic here

def pt_recommendation():
    personality_type = input("Enter your personality type: ")
    print(pt.get_recommendation(personality_type) + '\n')

def main():
    while True:
        print("0. Admin configuration")
        print("1. Recommendation based on personality type")
        user_input = get_user_input()

        if user_input == 0:
            admin_config()
        elif user_input == 1:
            pt_recommendation()
        else:
            logging.error("Invalid input", stack_info=True)
            print("Invalid input. Please try again.\n")

if __name__ == "__main__":
    setup_logging()    
    main()