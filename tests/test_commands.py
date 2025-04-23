""" 
Test module for the arithmetic commands and REPL functionality of the class App. 
This module will have the unit tests that will validate the behavior of different mathematical operations 
(Add, Subtract, Multiply, Divide) in the command system of the App class, as well as the REPL interface. 
The tests will be simulating user input to ensure commands will work as expected and will verify that the
application will handle input/output correctly, including edge cases like division by zero.
"""
import pytest
from app import App
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.exit import ExitCommand


def test_add_command(capfd, monkeypatch):
    """
    Test the AddCommand's functionality.
    """
    monkeypatch.setattr('builtins.input', lambda _: '5 3')
    command = AddCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Additon result: 8" in out, "The AddCommand should print the correct addition result."

def test_subtract_command(capfd, monkeypatch):
    """
    Test the SubtractCommand's functionality.
    """
    monkeypatch.setattr('builtins.input', lambda _: '5 3')
    command = SubtractCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Subtraction result: 2" in out, "The SubtractCommand should print the correct subtraction result."

def test_multiply_command(capfd, monkeypatch):
    """
    Test the MultiplyCommand's functionality.
    """
    monkeypatch.setattr('builtins.input', lambda _: '5 3')
    command = MultiplyCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Multiplication result: 15" in out, "The MultiplyCommand should print the correct multiplication result."

def test_divide_command(capfd, monkeypatch):
    """
    Test the DivideCommand's functionality.
    """
    monkeypatch.setattr('builtins.input', lambda _: '9 3')
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Division result: 3" in out, "The DivideCommand should print the correct division result."

def test_dividebyzero_command(capfd, monkeypatch):
    """
    This test simulates user input ('9 0') and verifies that an appropriate error message
    """
    monkeypatch.setattr('builtins.input', lambda _: '9 0')
    command = DivideCommand()
    command.execute()
    out, err = capfd.readouterr()
    assert "Error Occured! DivisionByzero" in out, "Error should be Occured."

def test_app_menu_command(capfd, monkeypatch):
    """
    Test that the REPL correctly handles the 'menu' command and exits cleanly.
    """
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.value.code == 0, "The app did not exit cleanly with code 0"
    out, err = capfd.readouterr()
    assert "Select the operation to be performed" in out
    assert "Add" in out
    assert "Subtract" in out
    assert "Multiply" in out
    assert "Divide" in out

def test_exit_command():
    """
    Test that ExitCommand raises SystemExit with the correct message.
    """
    command = ExitCommand()
    with pytest.raises(SystemExit) as e:
        command.execute()

    assert str(e.value) == "Exiting...", "Expected SystemExit with message 'Exiting...'"
