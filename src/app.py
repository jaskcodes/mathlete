import sys
from ai_tutor import interactive_session, evaluate_math_tutor, analyze_results
import json
import pandas as pd
import os
from questions import math_questions

os.environ["OPENAI_API_KEY"] = "OPEN_AI_KEY"

def evaluate():
    """
    To evaluate the accuracy of the model for the given set of questions
    """
    questions_df = math_questions()
    results = evaluate_math_tutor(questions_df)
    return analyze_results(results)
    
def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "interactive":
            interactive_session()
        elif command == "evaluate":
            print(evaluate())
        else:
            print("Command not recognized")
    else:
        print("Please provide a command. Options are: interactive, evaluate")

if __name__ == "__main__":
    main()