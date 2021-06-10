import pandas as pd
import sys

NAME_OF_RELATION = 'spam'
NAME_OF_CLASS = 'ham'

path = './'
file_in = 'data.csv'

#a = "0.0,0.0,0.17,0.52,0.17,0.0,0.17,0.0,0.69,0.17,0.17,0.0,0.0,0.0,0.0,1.74,0.0,0.69,1.04,0.0,0.17,0.0,0.0,0.0,0.17,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.17,0.0,0.0,0.34,0.0,0.0,0.17,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.07200000000000001,0.0,0.754,0.6809999999999999,0.0,4.74,52,967,1351"

#print(len(a.split(',')))

#wordsTreino = ['word_freq_make', 'word_freq_address', 'word_freq_all', 'word_freq_3d', 'word_freq_our', 'word_freq_over', 'word_freq_remove', 'word_freq_internet', 'word_freq_order', 'word_freq_mail', 'word_freq_receive', 'word_freq_will', 'word_freq_people', 'word_freq_report', 'word_freq_addresses', 'word_freq_free', 'word_freq_business', 'word_freq_email', 'word_freq_you', 'word_freq_credit', 'word_freq_your', 'word_freq_font', 'word_freq_000', 'word_freq_money', 'word_freq_hp', 'word_freq_hpl', 'word_freq_george', 'word_freq_650', 'word_freq_lab', 'word_freq_labs', 'word_freq_telnet', 'word_freq_857', 'word_freq_data', 'word_freq_415', 'word_freq_85', 'word_freq_technology', 'word_freq_1999', 'word_freq_parts', 'word_freq_pm', 'word_freq_direct', 'word_freq_cs', 'word_freq_meeting', 'word_freq_original', 'word_freq_project', 'word_freq_re', 'word_freq_edu', 'word_freq_table', 'word_freq_conference', 'char_freq_;', 'char_freq_(', 'char_freq_[', 'char_freq_!', 'char_freq_$', 'char_freq_#', 'capital_run_length_average', 'capital_run_length_longest', 'capital_run_length_total', 'Id', 'ham']
#wordsTeste = ['word_freq_make', 'word_freq_address', 'word_freq_all', 'word_freq_3d', 'word_freq_our', 'word_freq_over', 'word_freq_remove', 'word_freq_internet', 'word_freq_order', 'word_freq_mail', 'word_freq_receive', 'word_freq_will', 'word_freq_people', 'word_freq_report', 'word_freq_addresses', 'word_freq_free', 'word_freq_business', 'word_freq_email', 'word_freq_you', 'word_freq_credit', 'word_freq_your', 'word_freq_font', 'word_freq_000', 'word_freq_money', 'word_freq_hp', 'word_freq_hpl', 'word_freq_george', 'word_freq_650', 'word_freq_lab', 'word_freq_labs', 'word_freq_telnet', 'word_freq_857', 'word_freq_data', 'word_freq_415', 'word_freq_85', 'word_freq_technology', 'word_freq_1999', 'word_freq_parts', 'word_freq_pm', 'word_freq_direct', 'word_freq_cs', 'word_freq_meeting', 'word_freq_original', 'word_freq_project', 'word_freq_re', 'word_freq_edu', 'word_freq_table', 'word_freq_conference', 'char_freq_;', 'char_freq_(', 'char_freq_[', 'char_freq_!', 'char_freq_$', 'char_freq_#', 'capital_run_length_average', 'capital_run_length_longest', 'capital_run_length_total', 'Id']
wordsData = ['word_freq_make', 'word_freq_address', 'word_freq_all', 'word_freq_3d', 'word_freq_our', 'word_freq_over', 'word_freq_remove', 'word_freq_internet', 'word_freq_order', 'word_freq_mail', 'word_freq_receive', 'word_freq_will', 'word_freq_people', 'word_freq_report', 'word_freq_addresses', 'word_freq_free', 'word_freq_business', 'word_freq_email', 'word_freq_you', 'word_freq_credit', 'word_freq_your', 'word_freq_font', 'word_freq_000', 'word_freq_money', 'word_freq_hp', 'word_freq_hpl', 'word_freq_george', 'word_freq_650', 'word_freq_lab', 'word_freq_labs', 'word_freq_telnet', 'word_freq_857', 'word_freq_data', 'word_freq_415', 'word_freq_85', 'word_freq_technology', 'word_freq_1999', 'word_freq_parts', 'word_freq_pm', 'word_freq_direct', 'word_freq_cs', 'word_freq_meeting', 'word_freq_original', 'word_freq_project', 'word_freq_re', 'word_freq_edu', 'word_freq_table', 'word_freq_conference', 'char_freq_;', 'char_freq_(', 'char_freq_[', 'char_freq_!', 'char_freq_$', 'char_freq_#', 'capital_run_length_average', 'capital_run_length_longest', 'capital_run_length_total', 'Id', 'ham']

#words = "word_freq_make,word_freq_address,word_freq_all,word_freq_3d,word_freq_our,word_freq_over,word_freq_remove,word_freq_internet,word_freq_order,word_freq_mail,word_freq_receive,word_freq_will,word_freq_people,word_freq_report,word_freq_addresses,word_freq_free,word_freq_business,word_freq_email,word_freq_you,word_freq_credit,word_freq_your,word_freq_font,word_freq_000,word_freq_money,word_freq_hp,word_freq_hpl,word_freq_george,word_freq_650,word_freq_lab,word_freq_labs,word_freq_telnet,word_freq_857,word_freq_data,word_freq_415,word_freq_85,word_freq_technology,word_freq_1999,word_freq_parts,word_freq_pm,word_freq_direct,word_freq_cs,word_freq_meeting,word_freq_original,word_freq_project,word_freq_re,word_freq_edu,word_freq_table,word_freq_conference,char_freq_;,char_freq_(,char_freq_[,char_freq_!,char_freq_$,char_freq_#,capital_run_length_average,capital_run_length_longest,capital_run_length_total,ham,Id"
#print((words.split(',')))

#treino = pd.read_csv("./train_data.csv" , engine='python')
#teste = pd.read_csv("./test_features.csv" , engine='python')

train = pd.read_csv(path + file_in, engine='python')

#dataTreino = [row.split() for row in open('train_data.csv').readlines()[1:]]
#dataTeste = [row.split() for row in open('test_features.csv').readlines()[1:]]
dataData = [row.split() for row in open(file_in).readlines()[1:]]

#listOfminTreino = []
#listOfmaxTreino = []

#listOfminTeste = []
#listOfmaxTeste = []

listOfminData = []
listOfmaxData = []

#for word in wordsTreino:
#    listOfminTreino.append(treino[word].min())
#    listOfmaxTreino.append(treino[word].max())

#for word in wordsTeste:
#    listOfminTeste.append(teste[word].min())
#    listOfmaxTeste.append(teste[word].max())

for word in wordsData:
    listOfminData.append(train[word].min())
    listOfmaxData.append(train[word].max())

#tstspambase = '0.0, 0.0, 0.0, 0.0, 1.85, 0.0, 0.0, 1.85, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.223, 0.0, 0.0, 0.0, 0.0, 3.0, 15.0, 54.0, 1'
#traspambase = '0.0, 0.64, 0.64, 0.0, 0.32, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.64, 0.0, 0.0, 0.0, 0.32, 0.0, 1.29, 1.93, 0.0, 0.96, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.778, 0.0, 0.0, 3.756, 61.0, 278.0, 1'

file = open('data.dat', 'w')
file.write('@relation {}\n'.format(NAME_OF_RELATION))

for idx, word in enumerate(wordsData):
    if word == NAME_OF_CLASS:
        file.write("@attribute ham {1, 0}\n")
        continue
    if word == 'capital_run_length_average' or word == 'capital_run_length_longest' or word == 'capital_run_length_total' or word == 'Id':
        file.write('@attribute {} integer [{}, {}]\n'.format(word, listOfminData[idx], listOfmaxData[idx]))
        continue
    file.write('@attribute {} real [{}, {}]\n'.format(word, listOfminData[idx], listOfmaxData[idx]))

file.write('@inputs {}\n'.format(", ".join(wordsData[:-1])))
file.write('@outputs {}\n'.format(NAME_OF_CLASS))
file.write('@data\n')

for idx, row in enumerate(dataData):
    listOfRowData = dataData[idx][0].split(',')
    if listOfRowData[-2] == 'True':
        listOfRowData[-2] = '1'
    elif listOfRowData[-2] == 'False':
        listOfRowData[-2] = '0'
    listOfRowData[-1], listOfRowData[-2] = listOfRowData[-2], listOfRowData[-1]
    rowData = ', '.join(listOfRowData)
    rowData += '\n'

    file.write(rowData)
    
file.close()
