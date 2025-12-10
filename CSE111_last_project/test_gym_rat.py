import pytest
from gym_rat import training_plan_logger, choice_validator, language_validator

def test_training_plans_logic():
    assert training_plan_logger(0, "ABCD") == "Chest and Triceps"
    assert training_plan_logger(1, "ABCD") == "Back and Biceps"
    assert training_plan_logger(5, "ABCD") == "Legs"
    assert training_plan_logger(6, "ABCD") == "Rest Day"

    assert training_plan_logger(0, "PPL") == "Push (Chest, Shoulders, Triceps)"
    assert training_plan_logger(1, "PPL") == "Pull (Back, Biceps)"
    assert training_plan_logger(2, "PPL") == "Legs"
    assert training_plan_logger(6, "PPL") == "Rest Day"

    assert training_plan_logger(0, "UL") == "Upper Body"
    assert training_plan_logger(1, "UL") == "Lower Body"
    assert training_plan_logger(6, "UL") == "Rest Day"

def test_validators_valid_input():
    assert language_validator("E") is True
    assert language_validator("P") is True
    
    assert choice_validator("1", "eng") is True
    assert choice_validator("2", "pt") is True
    assert choice_validator("3", "eng") is True

    custom_list = ["1", "2", "3", "4"]
    assert choice_validator("4", "eng", valid_choices=custom_list) is True