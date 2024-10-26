from enum import Enum
import random
from typing import Dict, List

import streamlit as st
from attr import dataclass
from questions import QuestionType, questions, Question

class Section:
    def __init__(self, number: int):
        self.number = number
        self.questions = self.get_one_question_from_each_type()
        self.allowed_points = 10
        self.shaper_points = 0
        self.plant_points = 0
        self.coordinator_points = 0
        self.monitor_evaluator_points = 0
        self.implementer_points = 0
        self.completer_finisher_points = 0
        self.team_worker_points = 0
        self.resource_investigator_points = 0
    
    def __str__(self):
        return f"Section {self.number}"

    def get_one_question_from_each_type(self, index: int = 0) -> List[Question]:
        question_list = [question_list[index] for question_list in questions.values()]
        return question_list
    
    def return_question_category(self, question: Question) -> QuestionType:
        return question.category
    
    def add_points_to_category(self, category: QuestionType, points: int):
        if category == QuestionType.SHAPER:
            self.shaper_points += points
        elif category == QuestionType.PLANT:
            self.plant_points += points
        elif category == QuestionType.COORDINATOR:
            self.coordinator_points += points
        elif category == QuestionType.MONITOR_EVALUATOR:
            self.monitor_evaluator_points += points
        elif category == QuestionType.IMPLEMENTER:
            self.implementer_points += points
        elif category == QuestionType.COMPLETER_FINISHER:
            self.completer_finisher_points += points
        elif category == QuestionType.TEAM_WORKER:
            self.team_worker_points += points
        elif category == QuestionType.RESOURCE_INVESTIGATOR:
            self.resource_investigator_points += points

    def return_all_categories_points(self) -> Dict[str, int]:
        return {
            QuestionType.SHAPER.name: self.shaper_points,
            QuestionType.PLANT.name: self.plant_points,
            QuestionType.COORDINATOR.name: self.coordinator_points,
            QuestionType.MONITOR_EVALUATOR.name: self.monitor_evaluator_points,
            QuestionType.IMPLEMENTER.name: self.implementer_points,
            QuestionType.COMPLETER_FINISHER.name: self.completer_finisher_points,
            QuestionType.TEAM_WORKER.name: self.team_worker_points,
            QuestionType.RESOURCE_INVESTIGATOR.name: self.resource_investigator_points,
        }
        

    
section_1 = Section(1)
st.write(section_1)
total_points = section_1.allowed_points

for question in section_1.questions:
    number = st.number_input(question.text, min_value=0, max_value=10, value=0, step=1)
    category = section_1.return_question_category(question)
    section_1.add_points_to_category(category, number)
    total_points -= number

st.write(f"Total points left to distribute: {total_points}")
if total_points > 0:
    st.info("You have not used all your points")
elif total_points < 0:
    st.error("You have used too many points")
else:
    st.success("You have used all your points")
    if st.button("Next section"):
        categories_points = section_1.return_all_categories_points()

        st.write(categories_points)



