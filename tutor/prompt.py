##########################
## prompt functions ##
##########################

from fewshot import create_few_shot_examples

def generate_prompt(few_shot_examples=few_shot_examples, system_message=system_message):
    """
    Given few shot examples, and a system message to set the tone of the conversation,
    generate a prompt for the AI tutor

      Args:
          few_shot_examples (list, optional): examples using few shot prompting
          system_message (str, optional): A system message providing guidance to
              the AI math tutor.
              Defaults to system_message defined elsewhere.

      Returns:
          list: A list of messages including the system message and user-generated examples
    """

    messages = [SystemMessage(content=system_message)]
    for example in few_shot_examples:
        user_message = example["question"]
        ai_message = example["answer"]
        messages.append(HumanMessage(content=user_message))
        messages.append(AIMessage(content=ai_message))
    return messages


def prompt_response(question, few_shot_examples=few_shot_examples, system_message=system_message):
    """
    Ask a question to the AI tutor

        Args:
            question (string): An elementary math question
            few_shot_examples (list, optional): examples used to train the tutor
            system_message (str, optional): System message used to train the tutor

        Returns:
            AI Tutor's response to the question

    """
    chat = ChatOpenAI(temperature=0)
    messages = generate_prompt(few_shot_examples, system_message)
    messages.append(HumanMessage(content=question))
    return chat(messages).content