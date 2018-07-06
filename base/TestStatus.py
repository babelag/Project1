"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
from base.HandyWrappers import SeleniumDriver

class TestStatus(SeleniumDriver):

    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    print("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    print("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                print("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            print("### Exception Occurred !!!")
            self.screenShot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            print(testName +  " ### TEST FAILED")
            self.resultList.clear()
            assert True == False
        else:
            print(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True