# any pytest file should start with test_
# pytest method name should start with test
# any code should be wrapped in a method

import pytest

def test_firstProgram(setup):
    print("You have invoked first program")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)

