from aiogram.dispatcher.filters.state import StatesGroup, State

class Registration(StatesGroup):
    group_index = State()
    grade_book = State()

class ChangeGradeBook(StatesGroup):
    new_grade_book = State()

class ChangeGroupIndex(StatesGroup):
    new_group_index = State()

class SelectTerm(StatesGroup):
    select_term = State()