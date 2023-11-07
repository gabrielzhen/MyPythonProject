import openpyxl
wb=openpyxl.Workbook()
sheet=wb.get_active_sheet()
for i in range(1,11):
    sheet['A'+str(i)]=i
refobj=openpyxl.charts.Reference(sheet,(1,1),(10,1))
seriesobj=openpyxl.charts.Series(refobj,title='fuck you ')
chartobj=openpyxl.charts.Barchart()
chartobj.append(seriesobj)