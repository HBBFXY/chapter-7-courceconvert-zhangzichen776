import keyword

def convert_python_file(input_filename, output_filename):
    # 读取输入文件内容
    with open(input_filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取所有Python保留字
    reserved_words = set(keyword.kwlist)
    
    # 用于构建转换后的内容
    result = []
    i = 0
    n = len(content)
    
    while i < n:
        # 跳过非字母字符
        if not content[i].isalpha():
            result.append(content[i])
            i += 1
            continue
        
        # 提取完整的单词（由字母组成）
        j = i
        while j < n and content[j].isalpha():
            j += 1
        word = content[i:j]
        
        # 判断是否为保留字，决定是否转换大小写
        if word in reserved_words:
            result.append(word)  # 保留字不转换
        else:
            result.append(word.upper())  # 非保留字转为大写
        
        i = j  # 移动到下一个非字母位置
    
    # 将转换后的内容写入输出文件
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(''.join(result))

# 执行转换：读取random_int.py，输出到random_int_uppercase.py
convert_python_file('random_int.py', 'random_int_uppercase.py')
