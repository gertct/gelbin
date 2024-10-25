from enum import Enum
from typing import List

import streamlit as st
from attr import dataclass

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
There are 8 categories in each section
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

class QuestionType(Enum):
    SHAPER = "Shaper"
    PLANT = "Plant"
    COORDINATOR = "Coordinator"
    MONITOR_EVALUATOR = "Monitor Evaluator"
    IMPLEMENTER = "Implementer"
    COMPLETER_FINISHER = "Completer Finisher"
    TEAM_WORKER = "Team Worker"
    RESOURCE_INVESTIGATOR = "Resource Investigator"

@dataclass
class Question:
    question: str
    type: QuestionType

@dataclass
class Section:
    questions: List[Question]
    max_points: int = 10








