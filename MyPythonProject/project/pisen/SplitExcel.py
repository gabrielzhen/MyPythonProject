#按照一定的规则分割excel,比如按照单体的名称来进行区分
import pandas,os
#todo1 打开文件夹下的所有文件并加载到内存
allfiles=[]
dfs=[]

for path,dirs,files in os.walk('test'):
    for file in files:
        print( os.path.join(path,file))
        allfiles.append(os.path.join(path,file))
print('一共读取到了'+str(len(allfiles))+'个文件，开始加载...')

for file in allfiles:
    df=pandas.read_excel(file)
    dfs.append(df)
concat_df=pandas.concat(dfs)
#todo 2 对内存的数据进行排序处理，并且按照单体进行切分
df_distinct=concat_df['单体名称'].drop_duplicates().to_list()
# todo3 导出excel
for singl_df in df_distinct:
    row=concat_df[concat_df['单体名称']==singl_df]
    row.to_excel(f'{singl_df}.xlsx',index=False)