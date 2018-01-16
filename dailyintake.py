from sas7bdat import SAS7BDAT
import time

starttime = time.clock()

# 고추, 우유, 백미, 배추김치
#list = [['06029'], ['13010'], ['01173'], ['06063']]

#고추, 고춧잎, 상추, 배추, 쌈추,쑥갓, 갓,무청
list = [['06029'],['06038'],['06217'],['06063','06186'],['06262'], ['06265'],['06008', '06057'],['06139']]
list_intake = [0] * len(list)
list_num = [0] * len(list)
list_preID = ['0'] * len(list)

preID='0'
codeIndex = 0
intakeIndex = 0
weightIndex= 0
codeIncrease = 1
intakeIncrease = 1
weightIncrease = 1
n=-1

sampleSize=0


f = SAS7BDAT('HN16_24RC.sas7bdat')

for row in f:
    for i in range(len(row)):
        if row[i] == 'N_FCODE3': codeIncrease = 0
        if row[i] == 'NF_INTK3': intakeIncrease = 0
        if row[i] == 'wt_ntr': weightIncrease = 0
        codeIndex = codeIndex + codeIncrease
        intakeIndex = intakeIndex + intakeIncrease
        weightIndex = weightIndex + weightIncrease
    break
print(codeIndex, intakeIndex, weightIndex)


for row in f:
    n=n+1
    if preID != row[1] :
        if isinstance(row[weightIndex],str) : continue
        sampleSize= sampleSize + row[weightIndex]
    for i in range(len(list)) :
        if row[codeIndex] in list[i] :
            list_intake[i] = list_intake[i] + row[intakeIndex] * row[weightIndex]
            print(n)
            #print("list_num : ", list_num, "ID : ", row[1], "preID : ", list_preID[i], "identicality : ", list_preID[i]==row[1])
            '''
            if list_preID[i] != row[1] :
                list_num[i] = list_num[i] + 1
            list_preID[i]=row[1]
            '''
            # print(i, row[1], row[intakeIndex], list_intake[i], list_num[i])
    preID = row[1]
    

endtime=time.clock()

print("Time : ", endtime-starttime)
print("Sample size : ", sampleSize)
print(list_intake)
for i in range(len(list)) :
    print(list_intake[i]/sampleSize, end=', ')
