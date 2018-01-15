from sas7bdat import SAS7BDAT
import time

starttime=time.clock()

#고추, 고춧잎, 상추, 배추, 쌈추,쑥갓, 갓,무청
list = [[6029],[6038],[6217],[6063,6186],[6262], [6265],[6008, 6057],[6139]]
list_intake=[0]*len(list)
list_num=[0]*len(list)

codeIndex=0
intakeIndex=0
codeIncrease=1
intakeIncrease=1

f=SAS7BDAT('HN16_24RC.sas7bdat')

for row in f :
    for i in range(len(row)) :
        if row[i]=='N_FCODE3' : codeIncrease=0
        if row[i]=='NF_INTK3' : intakeIncrease=0
        codeIndex=codeIndex+codeIncrease
        intakeIndex=intakeIndex+intakeIncrease
    break
print(codeIndex, intakeIndex)

for row in f:
    for i in range(len(list)):
        if row[codeIndex] in list[i]:
            list_intake[i] += row[intakeIndex]
            list_num[i] = list_num[i] = 1
        print(i, row[1], row[intakeIndex], list_intake[i], list_num[i])

endtime=time.clock()

print(endtime-starttime)