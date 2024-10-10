ZERO_SHOT_PROMPT = """
Given the following topic {input}, generate a quiz with a randon number of questions between 1 to 5.  Return the result as
JSON.  The JSON object should have a "questions" property that is an array of ojects.  Each object has a "question", "choices",
and "answer" propery.  The value of "question" is "question" is a string representing the question being asked.
The value of "choices" is an array of objects with key - "key" and value is a multiple choice answer as string.  The value of
"answer" is a string representing the "key" of the correct multiple choice answer
"""
