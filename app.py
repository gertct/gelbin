from enum import Enum
import random
from typing import List

import streamlit as st
from attr import dataclass
from questions import questions, Question

st.write("Hello world")

"""
You have 7 sections to choose from:
each with 8 choices

You get 10 points to distribute in each section
You can distribute the points however you like, but you must use all 10 points in each section

you must complete all sections to get your results
"""


"""
Each section will have one question from each category
There are 7 categories in each section
The categories are:
1. Shaper
2. Plant
3. Coordinator
4. Monitor Evaluator
5. Implementer
6. Completer Finisher
7. Team Worker
8. Resource Investigator
"""

class Section:
    def __init__(self, number: int):
        self.number = number
        self.questions = []
        self.points = 10

    def get_one_question_from_each_type(index: int = 0) -> List[Question]:
        question_list = [question_list[index] for question_list in questions.values()]
        random.shuffle(question_list)
        return question_list


