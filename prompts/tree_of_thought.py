TREE_OF_THOUGHT_PROMPT = """
  Given the following topic {input}, generate a quiz with 5 questions.

  Create questions that are not common knowledge, but true

  If the question is birds, provide a hint in the question text

  For each question return 6 multiple choice answers

  Make the wrong answers seem very likely to be true

  Return the questions and answers as a JSON object in the following format:

  The top level property should be "questions" and the value should be an array

  Each question in the array should be an object with the following properties: "question", "choices" and "answer"

  "question" is a string representing the question being asked

  "choices" is an array of objects with key - "key" and value is a multiple choice answer as string

  "answer" is a string representing the "key" of the correct multiple choice answer
"""
