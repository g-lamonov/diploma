import re
import xlsxwriter

file1 = open("example.txt", "r")
lines = []
counter = 0
i = 0
j = 0
while True:
    line = file1.readline()
    if (not line):
        break
    if (line.startswith('Func') or line.startswith('\n')):
        continue
    else:
       
        value = re.findall('[0-9]*[.,]?[0-9]+', line)
        value[0] = float(value[0])

        lines.append(value[0])
file1.close

print(lines)
workbook = xlsxwriter.Workbook('test7.xlsx')
worksheet = workbook.add_worksheet()

row = 0
for i, valueNum in enumerate(lines):
    if (i)%8 ==  0.0:
        j = j + 1
        row = 0
    worksheet.write(j, row, valueNum)
    row += 1
workbook.close()
