#汇总excel文件
import pandas,openpyxl
from pathlib import Path

outxls='F:\\编程文件\\拆分与合并\\结果文件.xlsx'
files_path=Path('F:\\编程文件\\拆分与合并\\子文件夹')

#获取将合并的列表
files=[x for x in files_path.rglob('*.xlsx')]
print(files)

content=[]
for file in files:
    data=pandas.read_excel(file,'调查文件模版')
    content.append([file.stem,data.iloc[3,4],data.iloc[9,4]])
print(content)
pd=pandas.DataFrame(content)
pd.to_excel(outxls,sheet_name='sheet1')
