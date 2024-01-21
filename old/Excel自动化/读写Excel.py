import xlrd

book = xlrd.open_workbook(R"D:\Download\income.xlsx")
print(book.nsheets)
print(book.sheet_names())

