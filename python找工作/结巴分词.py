import jieba

with open('./nlp_test0.txt') as f:
    document = f.read()

    document_decode = document.decode('GBK')
    document_cut = jieba.cut(document_decode)
    # print  ' '.join(jieba_cut)  //如果打印结果，则分词效果消失，后面的result无法显示
    result = ' '.join(document_cut)
    result = result.encode('utf-8')
    with open('./nlp_test1.txt', 'w') as f2:
        f2.write(result)
f.close()
f2.close()

# 添加用户词典
jieba.load_userdict("files/FenCi.txt")
# 添加新词
jieba.suggest_freq('沙瑞金', True)
jieba.suggest_freq('易学习', True)
jieba.suggest_freq('王大路', True)

# 添加停用词
stpwrdpath = "stop_words.txt"
stpwrd_dic = open(stpwrdpath, 'rb')
stpwrd_content = stpwrd_dic.read()
#将停用词表转换为list
stpwrdlst = stpwrd_content.splitlines()
stpwrd_dic.close()

