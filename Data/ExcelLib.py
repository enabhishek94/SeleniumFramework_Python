import openpyxl



def read_locators(sheetname):
    filelocation = "C:\\Users\\abc\\Desktop\\Python P\\objects.xlsx"
    workbook = openpyxl.load_workbook(filelocation)
    worksheet = workbook[sheetname]
    r = worksheet.iter_rows()
    next(r)
    return {item[0].value:(item[1].value,item[2].value) for item in r}
print("ReadLocators working")