import numpy as np
import pandas as pd


dizi=np.array([3,2,1])
dizi2=np.ones((2,2),dtype="int")
dizi3=np.zeros(3,dtype="int")
dizi4=np.full((2,3),"x")
dizi5=np.linspace(10,20,3)
dizi6=np.random.randint(50,60,(3,2))
dizi7=np.arange(70,80,5)
"""
print(dizi)
print()
print(dizi2)
print()
print(dizi3)
print()
print(dizi4)
print()

print()
print(dizi6)
print()
print(dizi7)
------------------------------------------------------------------------------
print(dizi4[-1][-1])
dizi4[0][1]="y"
dizi4=np.append(dizi4,"z")
print(dizi4)
print(dizi4.size)
------------------------------------------------------------------------------
print(dizi4)
print(dizi4.shape)
dizi4=dizi4.reshape((3,2))


dizi4=np.concatenate((dizi4,dizi4),axis=1)
print(dizi4)
x = dizi4.view()  adresiyle verir değişince x de değişir
x = dizi4.copy()
a,b,c=np.split(dizi,3)

dizi=np.sort(dizi)
print(dizi)
------------------------------------------------------------------------------

PANDAS
"""
#print(dizi6)
df1=pd.DataFrame(dizi6,columns=["Sutun1","sutun2"],index=["a","b","c"])
dizi=np.array([3,5,11,1])
dizi2=np.array([7,9,15,19])
datam={"sutun1":dizi,"sutun2":dizi2}
datam2={"sutun1":dizi,"sutun2":[1,2,3,4]}
df7=pd.DataFrame(datam2)
df2=pd.DataFrame(datam)
#print(df1)
print(df2)
#print(df7)

#print(df1.head(1))
#print(df1.tail(1))
#print(df1.size)
#print(len(df1))
#print(df1.values)
#print(df1.info())
#print(df1.describe())
#print(df1.nunique())
"""
print(df2[0:2])
print(df2["sutun2"][0:1])
print(df2["sutun2"][1])

print(df2[df2["sutun2"]>10]["sutun2"])
print(df1.loc["b"])
print(df2.loc[2,"sutun2"])
print(df1.loc["a":"b"])

print(df1.iloc[0:2])

df2["toplam"]=df2["sutun1"]+df2["sutun2"]
"print(df2)
df2=df2.drop("toplam",axis=1)
df2=df2.drop([0,1])
print(df2)


DATAFRAME BİRLEŞTİRME
------------------------------------
df3=pd.concat([df1,df2],ignore_index=True,join="inner")             #alt alta
df4=pd.concat([df1,df2],ignore_index=True,join="outer") 

df3=pd.merge(df2,df7,on="sutun1")                                   #eksik sutun ekleme birleştirirken
df1=pd.DataFrame({"sutun1":[1,2,3],"sutun2":[3,4,5]})
df2=pd.DataFrame({"sutun1":[1,2,3],"sutun2":[3,4,5]})

df3=df1.join(df2,lsuffix='_df1', rsuffix='_df2')                    #yanyana
print(df3)


print(df2.groupby("sutun1").mean())
print(df2.groupby("sutun1").aggregate([min,max]))

def hepsineUygula(a):
    return a+3
df2["sutun2"]=df2["sutun2"].apply(hepsineUygula)
print(df2)

dfNullu=pd.DataFrame({"sutun1":[1,2,None,3],"sutun2":[5,None,7,8]})
print(dfNullu.isnull().sum().sum())
#dfNullu=dfNullu.fillna(value=-1)
dfNullu=dfNullu.dropna(axis=0)
print(dfNullu)"""