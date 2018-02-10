import pandas as pd
import time

starttime=time.clock()

print("start")


#고추, 고춧잎, 상추, 배추, 쌈추,쑥갓, 갓, 무청
list = [['06029'],['06038'],['06217'],['06063','06186'],['06262'], ['06265'],['06008', '06057'],['06139']]
intake=[0]*len(list)

df=pd.read_sas('HN16_24RC.sas7bdat')

code='06029'
row = df['N_FCODE3'] == code
#print(row>0)
#intake[0]=intake[0] + df['NF_INTK3'].loc[row] * df['wt_ntr'].loc[row]

'''
for item in list :
    for code in item :
        row=df['N_FCODE3'] == code
        intake[list.index(item)]=intake[list.index(item)] + df['NF_INTK3'].loc[row] * df['wt_ntr'].loc[row]
'''
print("intake", intake)

weight=df.groupby('ID').mean()
samplesize=weight['wt_ntr'].sum()


endtime=time.clock()
print("It took %f seconds" %(endtime-starttime))
print("samplesize : " %samplesize)