import openpyxl
cen=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=cen['Population by Census Tract']
countDate={}
for rows in range(2,sheet.max_row+1):
    state=sheet['B'+str(rows)].value
    country=sheet['C'+str(rows)].value
    pop=sheet['D'+str(rows)].value

    countDate.setdefault(state,{})
    countDate[state].setdefault(country,{'tracts':0,'pop':0})
    
    countDate[state][country]['tracts']+=1
    countDate[state][country]['pop']+=int(pop)

resultfile=open('censuspopdata.txt','w')
resultfile.write(str(countDate))
resultfile.close()

