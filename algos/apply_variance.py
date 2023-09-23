from random import randint, choice
import logging

def vary_personality_type(personality_type: str, variance: int) -> str:
    """
    Returns a personality type with some variance applied.
    The higher the variance, the personality type will change to a higher extent.
    """
    try:
        personality_dict = {0:['E', 'I'], 1:['S', 'N'], 2:['T', 'F'], 3:['J', 'P']}
        for _ in range(variance):
            random_index = randint(0, 3)
            personality_type = personality_type.replace(personality_type[random_index], choice(personality_dict[random_index]))
    except Exception as e:
        logging.error(e, stack_info=True)
        print(e + '\n')
    finally:
        return personality_type