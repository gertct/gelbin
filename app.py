from enum import Enum

import streamlit as st
from attr import dataclass

from questions import QuestionSection

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


class Section():
    name: str
    questions: QuestionSection
    section_number: int

    def __init__(self, name: str, questions: QuestionSection):
        self.name = name
        self.questions = questions

    def get_questions(self, section_number: int):
        return self.questions.questions[section_number]
    

section1 = Section("Section 1", )


    


    
