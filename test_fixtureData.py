import pytest


@pytest.mark.usefixtures("dataLoad")
class Test_example():

    def test_editProfile(self, dataLoad):
        print(dataLoad)


