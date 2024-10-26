from enum import Enum
from dataclasses import dataclass

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
    points: int = 0
    section: int = 0

questions = {
    QuestionType.SHAPER: [
        Question("I react strongly when meetings look like losing track of the main objective.", QuestionType.SHAPER, section=0),
        Question("I like to have a strong influence on decisions.", QuestionType.SHAPER, section=1),
        Question("I am ready to make my personal views known in a forceful way if necessary.", QuestionType.SHAPER, section=2),
        Question("I am not reluctant to emphasise my own point of view in meetings.", QuestionType.SHAPER, section=3),
        Question("I feel it is sometimes worth incurring some temporary unpopularity if one is to succeed in getting one's views across in a group.", QuestionType.SHAPER, section=4),
        Question("I am happy to take the lead when action is required.", QuestionType.SHAPER, section=5),
        Question("I try to make my mark in group meetings.", QuestionType.SHAPER, section=6),
    ],
    QuestionType.COORDINATOR: [
        Question("I have an aptitude for organising people.", QuestionType.COORDINATOR, section=0),
        Question("I enjoy reconciling different points of view.", QuestionType.COORDINATOR, section=1),
        Question("I can co-ordinate and use productively other people's abilities and talents.", QuestionType.COORDINATOR, section=2),
        Question("I can work with all sorts of people provided that they have got something worthwhile to contribute.", QuestionType.COORDINATOR, section=3),
        Question("I can work with people who vary widely in their personal qualities and outlook.", QuestionType.COORDINATOR, section=4),
        Question("I am able to assert myself to get other people involved if necessary.", QuestionType.COORDINATOR, section=5),
        Question("I see both sides of a problem and take a decision acceptable to all.", QuestionType.COORDINATOR, section=6),
    ],
    QuestionType.PLANT: [
        Question("I produce original suggestions.", QuestionType.PLANT, section=0),
        Question("I tend to have a creative approach to problem solving.", QuestionType.PLANT, section=1),
        Question("I often produce a new approach to a long continuing problem.", QuestionType.PLANT, section=2),
        Question("I tend to see patterns where others would see items as unconnected.", QuestionType.PLANT, section=3),
        Question("I often find my imagination frustrated by working in a group.", QuestionType.PLANT, section=4),
        Question("I am able to take an independent and innovative look at most situations.", QuestionType.PLANT, section=5),
        Question("I can see how ideas and techniques can be used in new relationships.", QuestionType.PLANT, section=6),
    ],
    QuestionType.RESOURCE_INVESTIGATOR: [
        Question("I am keen to find out the latest ideas and developments.", QuestionType.RESOURCE_INVESTIGATOR, section=0),
        Question("I particularly enjoy exploring different views and techniques.", QuestionType.RESOURCE_INVESTIGATOR, section=1),
        Question("I explore ideas that may have a wider application than in the immediate task.", QuestionType.RESOURCE_INVESTIGATOR, section=2),
        Question("I make a point of following up interesting ideas and/or people.", QuestionType.RESOURCE_INVESTIGATOR, section=3),
        Question("I usually know someone whose specialist knowledge is particularly apt.", QuestionType.RESOURCE_INVESTIGATOR, section=4),
        Question("I start to look around for possible ideas and openings.", QuestionType.RESOURCE_INVESTIGATOR, section=5),
        Question("A broad range of personal contacts is important to my style of working.", QuestionType.RESOURCE_INVESTIGATOR, section=6),
    ],
    QuestionType.MONITOR_EVALUATOR: [
        Question("I analyse other people's ideas objectively, for both merits and failings.", QuestionType.MONITOR_EVALUATOR, section=0),
        Question("I like to make critical discrimination between alternatives.", QuestionType.MONITOR_EVALUATOR, section=1),
        Question("I like to weigh up and evaluate a range of suggestions thoroughly before choosing.", QuestionType.MONITOR_EVALUATOR, section=2),
        Question("I can usually find the argument to refute unsound propositions.", QuestionType.MONITOR_EVALUATOR, section=3),
        Question("My feelings seldom interfere with my judgment.", QuestionType.MONITOR_EVALUATOR, section=4),
        Question("I approach the problem in a carefully analytical way.", QuestionType.MONITOR_EVALUATOR, section=5),
        Question("My considered judgment may take time but is usually near the mark.", QuestionType.MONITOR_EVALUATOR, section=6),
    ],
    QuestionType.IMPLEMENTER: [
        Question("I can be relied upon to see that work that needs to be done is organised.", QuestionType.IMPLEMENTER, section=0),
        Question("I am more interested in practicalities than new ideas.", QuestionType.IMPLEMENTER, section=1),
        Question("I maintain a steady systematic approach, whatever the pressures.", QuestionType.IMPLEMENTER, section=2),
        Question("I am keen to see there is nothing vague about my task and objectives.", QuestionType.IMPLEMENTER, section=3),
        Question("I strive to build up an effective structure.", QuestionType.IMPLEMENTER, section=4),
        Question("I find it hard to give in a job where the goals are not clearly defined.", QuestionType.IMPLEMENTER, section=5),
        Question("I think I have a talent for sorting out the concrete steps that need to be taken given a broad brief.", QuestionType.IMPLEMENTER, section=6),
    ],
    QuestionType.TEAM_WORKER: [
        Question("I am always ready to support good suggestions that help to resolve a problem.", QuestionType.TEAM_WORKER, section=0),
        Question("I am concerned to help colleagues with their problems.", QuestionType.TEAM_WORKER, section=1),
        Question("I am ready to help whenever I can.", QuestionType.TEAM_WORKER, section=2),
        Question("I have a quiet interest in getting to know people better.", QuestionType.TEAM_WORKER, section=3),
        Question("I find my personal skill particularly appropriate in achieving agreement.", QuestionType.TEAM_WORKER, section=4),
        Question("I can respond positively to my colleagues and their initiatives.", QuestionType.TEAM_WORKER, section=5),
        Question("I get on well with others and work hard for the team.", QuestionType.TEAM_WORKER, section=6),
    ],
    QuestionType.COMPLETER_FINISHER: [
        Question("I pick up slips and omissions that others fail to notice.", QuestionType.COMPLETER_FINISHER, section=0),
        Question("I feel in my element where work requires a high degree of attention and concentration.", QuestionType.COMPLETER_FINISHER, section=1),
        Question("I keep a watching eye on areas where difficulty may arise.", QuestionType.COMPLETER_FINISHER, section=2),
        Question("Being busy gives me real satisfaction.", QuestionType.COMPLETER_FINISHER, section=3),
        Question("I seem to develop a natural sense of urgency.", QuestionType.COMPLETER_FINISHER, section=4),
        Question("I am concerned to finish and perfect current work before I start.", QuestionType.COMPLETER_FINISHER, section=5),
        Question("I have an eye for getting the details right.", QuestionType.COMPLETER_FINISHER, section=6),
    ],
}

