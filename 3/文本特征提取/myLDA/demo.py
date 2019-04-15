# import jieba
#
# strs="\n\u3000\u3000窃蛋龙类是生活在亚洲和北美白垩纪时期的长羽毛的恐龙。它们成年个体小至火鸡大小，生态系统的重要组成分子。', '\n', '\n\u3000\u3000“华南龙的发现，"
#
# fenci = jieba.cut(strs)  # 切分  句子
# for each in fenci:
#     if each =='　':
#         pass
#     else:
#         print('%%%%'+each+'%%%%')
#         print('---------------------------------------')
import numpy as np

list=[[1,2,2,4],[2,3,2,5],[3,4,2,6]]
a=np.array(list)
print(a[:,2])


