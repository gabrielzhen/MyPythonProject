def find_diff(befors,afters):
    not_in=[]
    for befor in befors:
        if not befor in afters:
            not_in.append(befor)
    if len(not_in):
        return ','.join(not_in)
    else:
        return ''

def find_change_info(a_info, b_info):
    # 字符串转字典
    before_info_list = b_info.split(',')
    after_info_list = a_info.split(',')
    not_befor=find_diff(before_info_list,after_info_list)
    not_after=find_diff(after_info_list,before_info_list)
    return (not_befor,not_after)
output={'not_befor':find_change_info(input['befor_info'],input['after_info'])(0)}




#     # 如果新信息的选项小于或者等于旧信息则直接返回新信息
#     if len(after_info_list) <= len(before_info_list):
#         return a_info
#     # 通过迭代寻找差异
#     more_info_list = []
#     for after_item in after_info_list:
#         # 如果新信息选择不在旧信息中，则加入more_info_list
#         if after_item not in before_info_list:
#             more_info_list.append(after_item)
#     # 如果more_info_list中有数据,则返回
#     if len(more_info_list):
#         return ','.join(more_info_list)
#     # 如果more_info_list中无数据,则返回新消息
#     else:
#         return a_info

# output= {'diff_info': find_change_info(input['after_info'], input['before_info'])}


find_change_info('第一批,第二批','第一批,第三批')