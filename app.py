from typing import Dict, List

import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard
from streamlit.components.v1 import components
from streamlit_float import float_parent, float_init

from questions import QuestionType, questions, Question
from role_details import role_details

st.set_page_config(page_title="Gelbin Test", layout="wide")

if "completed_sections" not in st.session_state:
    st.session_state.completed_sections = []

float_init()

role_display_names = {
    "SHAPER": "Shaper 🔨",
    "PLANT": "Plant 🌱",
    "COORDINATOR": "Coordinator 🎯",
    "MONITOR_EVALUATOR": "Monitor Evaluator 🔍",
    "IMPLEMENTER": "Implementer 🛠️",
    "COMPLETER_FINISHER": "Completer Finisher 🏁",
    "TEAM_WORKER": "Team Worker 🤝",
    "RESOURCE_INVESTIGATOR": "Resource Investigator 🕵️",
    "SPECIALIST": "Specialist 📚",
}


class Section:
    def __init__(self, number: int):
        self.number = number
        self.questions = self.get_one_question_from_each_type(self.number - 1)
        self.allowed_points = 10
        self.shaper_points = 0
        self.plant_points = 0
        self.coordinator_points = 0
        self.monitor_evaluator_points = 0
        self.implementer_points = 0
        self.completer_finisher_points = 0
        self.team_worker_points = 0
        self.resource_investigator_points = 0
        self.specialist_points = 0
        self.completed = False

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
        elif category == QuestionType.SPECIALIST:
            self.specialist_points += points

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
            QuestionType.SPECIALIST.name: self.specialist_points,
        }


@st.dialog("Instructions", width="large")
def show_instructions():
    st.image("belbin_roles.png", use_column_width=True)
    st.write(
        """
        Welcome to the Belbin Test! 
        

        ## Instructions
        1. Go through each section and select between 1-3 sentences that most apply to you.
        2. Distribute your 10 points among the selected sentences, based on preference.
        3. Mark the section as completed.
        4. Once all sections are completed, click on 'View Results' to see your top roles.
        
        This version of the Belbin test has been taken from "Teambuilding" by Alistair Fraser and Suzanne Neville.
        """
    )


start_col, _, instructions_col, _ = st.columns([1, 5, 1, 3])
with start_col:
    if st.button("Start Over"):
        st.session_state.total_points = {
            category: 0 for category in QuestionType.__members__
        }
        st.session_state.completed_sections = []
        st.rerun()
with instructions_col:
    if st.button("Instructions"):
        show_instructions()


def scroll_to(element_id):
    st.components.v1.html(
        f"""
        <script>
            var element = window.parent.document.getElementById("{element_id}");
            element.scrollIntoView({{behavior: 'smooth'}});
        </script>
    """.encode()
    )


def quiz_section(section_number, expanded=False):
    with st.expander(f"Section {section_number}", expanded=expanded):
        section = Section(section_number)
        st.header(f"Section {section_number}", anchor=f"{section_number}")
        total_points = section.allowed_points

        section_points = questions_section(section, total_points)

        points_and_mark_completed(section, section_number, section_points)


def points_and_mark_completed(section, section_number, total_points):
    disabled_setting = disabled_on_complete_setting(section)

    if total_points > 0:
        st.info("Distribute all your points to mark section as completed.")
    elif total_points < 0:
        st.error("You have used too many points")
    elif total_points is False:
        return st.error("You've checked too many boxes! 3 is the max.")
    else:
        if st.button(
            f"Mark Section {section_number} Completed",
            key=f"section_{section_number}",
            disabled=disabled_setting,
            use_container_width=True,
            type="primary",
        ):
            categories_points = section.return_all_categories_points()

            if "total_points" not in st.session_state:
                st.session_state.total_points = {
                    category: 0 for category in categories_points
                }

            for category, points in categories_points.items():
                st.session_state.total_points[category] += points

            st.session_state.completed_sections.append(section_number)
            section.completed = True
            st.rerun()


def questions_section(section, total_points):
    st.markdown(
        """
        <style>
        .vertically-centered {
            margin-top: 37px;  
        }
        .stCheckbox {
            margin-top: 29px;   
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    disabled_setting = disabled_on_complete_setting(section)

    checked_questions = []
    for question in section.questions:
        checkbox_col, question_col, points_col = st.columns([0.03, 0.7, 0.2])

        with checkbox_col:
            checked = st.checkbox(
                "checkbox",
                key=f"checkbox_{section}{question.text}",
                disabled=disabled_setting,
                label_visibility="collapsed",
            )
            if checked:
                checked_questions.append(question)

        with question_col:
            st.markdown(
                f'<p class="vertically-centered">{question.text}</p>',
                unsafe_allow_html=True,
            )

        with points_col:
            number = st.number_input(
                "number_input",
                min_value=0,
                max_value=10,
                value=0,
                step=1,
                key=f"{section}{question.text}",
                disabled=disabled_setting or not checked,
                label_visibility="collapsed",
            )

        category = section.return_question_category(question)
        section.add_points_to_category(category, number)
        total_points -= number

    if len(checked_questions) < 3:
        st.warning(
            "First, select between 1 to 3 sentences which most apply to you. Then distribute your points."
        )

    if len(checked_questions) > 3:
        return False

    if total_points != 0:
        st.success(f"Total points left to distribute: {total_points}")

    return total_points


def disabled_on_complete_setting(section):
    disable_list = st.session_state.get("completed_sections", [])
    disabled_setting = False
    if section.number in disable_list:
        disabled_setting = True
    return disabled_setting


quiz_section_col, data_col = st.columns([4, 2])
with quiz_section_col:
    uncompleted_sections = [
        section
        for section in range(1, 8)
        if section not in st.session_state.completed_sections
    ]
    min_uncompleted_section = min(uncompleted_sections, default=None)
    for section in range(1, 8):
        quiz_section(section, expanded=section == min_uncompleted_section)

    if min_uncompleted_section:
        scroll_to(min_uncompleted_section)

    if not uncompleted_sections:
        st.balloons()


@st.dialog("Your Top Roles", width="large")
def show_top_roles(top_roles, role_details):
    st.header("Your Top Roles and Their Points")
    for role, points in top_roles:
        pretty_role = role_display_names.get(role, role)
        st.subheader(f"{pretty_role}: {points} points")

        role_info = role_details[role]

        st.markdown(f"**Summary:** {role_info['summary']}")

        with st.expander("Detailed Information"):
            st.markdown(f"**Characteristics:** {role_info['characteristics']}")
            st.markdown(
                f"**Detailed Characteristics:** {role_info['detailed_characteristics']}"
            )
            st.markdown(f"**Function:** {role_info['function']}")
            st.markdown(f"**Strengths:** {role_info['strengths']}")
            st.markdown(f"**Weaknesses:** {role_info['weaknesses']}")

        role_text = f"""
Role: {pretty_role}
Points: {points}
Summary: {role_info['summary']}
Characteristics: {role_info['characteristics']}
Detailed Characteristics: {role_info['detailed_characteristics']}
Function: {role_info['function']}
Strengths: {role_info['strengths']}
Weaknesses: {role_info['weaknesses']}
        """

        st_copy_to_clipboard(role_text, "Copy Role Information")


with data_col:
    float_parent()
    completed_sections = st.session_state.completed_sections
    for section in completed_sections:
        st.write(f"✅ Section {section} completed")
    if len(completed_sections) == 7:
        st.divider()
        st.write("All sections completed 🎉")

        sorted_roles = sorted(
            st.session_state.total_points.items(), key=lambda x: x[1], reverse=True
        )

        top_two_points = sorted_roles[0][1], sorted_roles[1][1]

        top_roles = [
            (role, points) for role, points in sorted_roles if points in top_two_points
        ]

        if st.button("View Results", type="primary"):
            show_top_roles(top_roles, role_details)
