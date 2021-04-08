import pytest


@pytest.fixture(scope="class")
def setup():
    print("Fixture is executed first")
    yield
    print("This will be executed last")

@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Krishna", "krishna.ranjan.2021@gmail.com", "Software Engineer"]