from learning_tool import Question

import pytest
from learning_tool import Question

def test_display_statistics(capsys):
    question = Question("Question", "Answer", "quiz")
    question.id = "123"
    question.show_count = 10
    question.correct_count = 7

    question.display_statistics()

    captured = capsys.readouterr()
    output = captured.out

    assert "ID: 123" in output
    assert "Question: Question" in output
    assert "Answer: Answer" in output
    assert "Active: Yes" in output
    assert "Times Shown: 10" in output
    assert "Percentage Correct: 70.00%" in output



def test_disable_question():
    question = Question("Question text", "Answer", "quiz")
    question.disable()
    assert not question.active

def test_enable_question():
    question = Question("Question text", "Answer", "quiz")
    question.enable()
    assert question.active

