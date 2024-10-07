ZERO_SHOT_PROMPT = """
Given the following topic {input}, generate a quiz with a randon number of questions between 1 to 5.

Here is the output schema:
```
{{"$defs": {{"Choice": {{"properties": {{"key": {{"description": "The key for the choice which exists as a single character as a key", "title": "Key", "type": "string"}}, "value": {{"description": "The value for the choice", "title": "Value", "type": "string"}}}}, "required": ["key", "value"], "title": "Choice", "type": "object"}}, "Question": {{"properties": {{"question": {{"description": "The question to be asked", "title": "Question", "type": "string"}}, "choices": {{"description": "The choices for the question", "items": {{"$ref": "#/$defs/Choice"}}, "title": "Choices", "type": "array"}}, "answer": {{"description": "The answer to the question. Validated against choices to ensure answer exists in the choices list based on the key. Exists as a single character as a key.", "title": "Answer", "type": "string"}}}}, "required": ["question", "choices", "answer"], "title": "Question", "type": "object"}}}}, "properties": {{"questions": {{"description": "The questions for the quiz", "items": {{"$ref": "#/$defs/Question"}}, "title": "Questions", "type": "array"}}}}, "required": ["questions"]}}
```
"""
