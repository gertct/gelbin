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
        self.questions = self.get_one_question_from_each_type()
        self.points = 10
    
    def __str__(self):
        return f"Section {self.number}"

    def get_one_question_from_each_type(self, index: int = 0) -> List[Question]:
        question_list = [question_list[index] for question_list in questions.values()]
        return question_list
    
    def remove_points(self, points: int):
        self.points -= points

    def add_points(self, points: int):
        self.points += points

    
section_1 = Section(1)
st.write(section_1)
total_points = section_1.points
st.write(f"Total points: {total_points}")

for question in section_1.questions:
    number = st.number_input(question.text, min_value=0, max_value=10, value=0, step=1)
    total_points -= number

st.write(f"Total points: {total_points}")
if total_points <= 0:
    st.success("You have used all your points")
    st.button("Next section")
else:
    st.info("You have not used all your points")



