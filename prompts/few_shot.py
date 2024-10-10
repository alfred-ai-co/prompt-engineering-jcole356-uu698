FEW_SHOT_PROMPT = """
Given the following topic {input}, generate a quiz with a randon number of questions between 1 to 5.

The output should be formatted as a JSON instance as follows:

An example of the schema:
{{ "questions": [ {{ "question": "The question to ask the user", "choices": [{{ "key": "a", value: "The correct answer to the question" }}], "answer": "a" }} ] }}

Choices may have multiple examples as follows:
[ {{ "key": "a", "value": "Answer One" }}, {{ "key": "b", "value": "Answer Two" }} ]
"""
