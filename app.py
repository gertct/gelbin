from enum import Enum
import random
from typing import Dict, List

import streamlit as st
from attr import dataclass
from questions import QuestionType, questions, Question

if st.button("Start Over"):
    st.session_state.total_points = {category: 0 for category in QuestionType.__members__}

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
        

def quiz_section(section_number):
    section = Section(section_number)
    st.write(section)
    total_points = section.allowed_points

    for question in section.questions:
        number = st.number_input(question.text, min_value=0, max_value=10, value=0, step=1, key=f"{section}{question.text}")
        category = section.return_question_category(question)
        section.add_points_to_category(category, number)
        total_points -= number

    st.write(f"Total points left to distribute: {total_points}")
    if total_points > 0:
        st.info("You have not used all your points")
    elif total_points < 0:
        st.error("You have used too many points")
    else:
        st.success("You have used all your points")
        if st.button("Next section", key=f"section_{section_number}"):
            categories_points = section.return_all_categories_points()
            st.write(categories_points)

            if 'total_points' not in st.session_state:
                st.session_state.total_points = {category: 0 for category in categories_points}

            for category, points in categories_points.items():
                st.session_state.total_points[category] += points

            st.write("Accumulated total points:")
            st.write(st.session_state.total_points)

quiz_section(1)
quiz_section(2)
quiz_section(3)
quiz_section(4)
quiz_section(5)
quiz_section(6)
quiz_section(7)