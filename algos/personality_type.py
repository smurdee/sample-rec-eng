from pandas import read_csv
from random import choice
import logging
import json

with open('config.json') as f:
    config = json.load(f)

def get_recommendation(personality_type: str) -> str:
    """
    Returns a recommendation based on the personality type.
    """
    
    try:        
        personality_type = personality_type.upper()
        df = read_csv("datasets/personality_activity_matrix.csv")

        # Check if personality type exists in dataset
        if personality_type in df['personality_type'].values:
            
            # Apply some variance in activity preference
            if config['variance'] > 0:
                from algos.apply_variance import vary_personality_type
                personality_type = vary_personality_type(personality_type, config['variance'])
            
            # Find all suitable activities
            df = df[df['personality_type'] == personality_type]
            values = df.values.tolist()[0]
            activity_indexes = [i for i in range(len(values)) if values[i] == 1]
            
            # Pick one of the activities at random
            random_index = choice(activity_indexes)
            activity = df.columns[random_index]
            
            return "Try " + activity + " for " + personality_type + "."
        else:
            return "Personality type not found."
    except Exception as e:
        # log the error
        logging.error("Error in get_recommendation: " + str(e), stack_info=True)
        return "Error in get_recommendation: " + str(e) + ". Please try again."