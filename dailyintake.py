from sas7bdat import SAS7BDAT
import time

starttime=time.clock()

#고추, 고춧잎, 상추, 배추, 쌈추,쑥갓, 갓,무청
list = [['06029'],['06038'],['06217'],['06063','06186'],['06262'], ['06265'],['06008', '06057'],['06139']]
list_intake=[0]*len(list)
list_num=[0]*len(list)

codeIndex=0
intakeIndex=0
codeIncrease=1
intakeIncrease=1
preID='0'
samplesize=0

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
    if preID==row[1] : identicality=1
    else :
        identicality=0
        samplesize=samplesize+1
    for i in range(len(list)) :
        if row[codeIndex] in list[i] :
            list_intake[i] = list_intake[i] + row[intakeIndex]
            if identicality==0 : list_num[i] = list_num[i] + 1
    preID = row[1]
    print(samplesize)
        #print(i, row[1], row[intakeIndex], list_intake[i], list_num[i])

endtime=time.clock()

print(endtime-starttime)
print(list_intake, list_num)
for i in range(len(list)) :
    print(list_intake[i]/list_num[i], end=', ')
