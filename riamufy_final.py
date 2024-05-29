import random 
in_str = input("Enter string: ")
in_list = [*in_str]
out_str = ''
cn_list = ['豆', '啊', '哦', '德', '骄', '三', '能', '芬', '术', '健', '格', '机', '用', '月', '动', '规', '车', '绿', '和', '拉', '傲', '肌', '奥', '克', '就', '发', '突', '二', '辉', '哈', '的', '酱', '国', '客', '起', '给', '卡', '光', '划', '腐', '非', '法', '阿', '力', '康', '更', '觉', '得', '斯', 'i', '肤', '风', '蒂', '开', '户']
riamu_cn = False
for i in in_list:
    event = random.randint(0,100)
    spaces = random.randint(0,3)
    choose_cn = random.randint(0,100)
    if(riamu_cn):
        i = random.choice(cn_list)
    if(event<85):
        out_str+=i+' '*spaces
    else:
        out_str+=' '*spaces
    if(not riamu_cn and choose_cn>80):
        riamu_cn = not riamu_cn
    elif(riamu_cn and choose_cn>50):
        riamu_cn = not riamu_cn
print(out_str)