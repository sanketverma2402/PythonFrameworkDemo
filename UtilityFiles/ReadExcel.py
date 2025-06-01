import openpyxl

class ReadTD:

    @staticmethod
    def getTestData(rowIndex,colIndex):
        workbook = openpyxl.load_workbook("C:\\Users\\Sanky Verma\\PycharmProjects\\PythonProject\\PythonProject\\Framework_Demo\\TestData\\DataHomePage1.xlsx")
        sheet = workbook['Sheet1']

        s2 = sheet.cell(row=rowIndex, column=colIndex).value
        return s2

