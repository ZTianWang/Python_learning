myStr = 'Hello World  '
# Slicing
print(myStr[0:5])  # 从index=0开始到index=5，但不包括5
print(myStr[:7])  # 从开始到index=7，但不包括7
print(myStr[6:])  # 从index=6开始到结束

# str(): str构造器。len(str): str长度
print('len: ' + str(len(myStr)))

# in: str逻辑运算符
print('wo' in myStr)

# str library
print('lower: ' + myStr.lower())  # lower(), upper(): 大小写转换，不改变原对象(copy)
# strip(): 删除两侧whitespace, lstrip()/rstrip(): 删除左/右侧空白（包含space/tab/newline)
print('stripping: ' + myStr.strip())
# startwith()/endwith(): 判断是否以xxx开头/结尾
print(myStr.startswith('h'))
print('replace: ' + myStr.replace('W', 'w'))  # 替换所有字符，copy。
# find(): 字符串存在则返回所在的第一个index, 否则返回-1。可与replace()、in配合使用
print(myStr.find(' '))

# format: 使用%隔开
print('format int: %d' % 4)
print('format float: %f' % 4.5)
print('format string: %s' % 'string')
print('mix string format: %d, %f' % (1, 1.5))  # 混合format用()包裹

# Practice :
# Use find and string slicing to extract the portion of the string after the colon character
# and then use the float function to convert the extracted string into a floating point number.
praStr = 'X-DSPAM-Confidence: 0.8475'
colon = praStr.find(': ')
num = praStr[colon + 1:]
floatNum = float(num)
print('Practice result: ' + str(floatNum))
