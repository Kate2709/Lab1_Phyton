#Вариант №3: Записать в выходной файл список доменов электронных почт из входного файла.
import re
data_file = open('test.txt', 'r')
find_el = '@(.*)'

line = data_file.readlines()
tmp = []
kontrol = 0
for i in range(len(line)):
    if line[i].strip():
        str = re.findall(find_el, line[i])
        if i == 0:
            tmp.append(str[0])
        else:
            for k in tmp:
                if k == str[0]:
                    kontrol = -1
                    break
            if kontrol == 0:
                tmp.append(str[0])
    kontrol = 0

result_file = open('result.txt', 'w')
for j in tmp:
    result_file.write(j + '\n')

result_file.close()
data_file.close()



