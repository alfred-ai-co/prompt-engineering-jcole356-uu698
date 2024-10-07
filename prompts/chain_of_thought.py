CHAIN_OF_THOUGHT_PROMPT = """
  Given the following topic {input}, generate a quiz with 5 questions.

  For each question return 6 multiple choice answers

  Return the questions and answers as a JSON object in the following format:

  The top level property should be "questions" and the value should be an array

  Each question in the array should be an object with the following properties: "question", "choices" and "answer"

  "question" is a string representing the question being asked

  "choices" is an array of objects with key - "key" and value is a multiple choice answer as string

  "answer" is a string representing the "key" of the correct multiple choice answer
"""
