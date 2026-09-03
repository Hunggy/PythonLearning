import openpyxl
wb = openpyxl.load_workbook("成绩表.xlsx")   # 加载已存在的文件
ws = wb.active
for row in ws.iter_rows(values_only=True):
    print(row)