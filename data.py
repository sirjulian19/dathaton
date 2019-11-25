# Import the Pandas package
import pandas as pd

strPath = 'Dataset/'

def setPath(strCurrentPath):
    strPath = strCurrentPath
    print(strPath)

# @staticmethod
def dataLoader(strFileName,bLowMem = False,strSeparator=','):
    # if bLowMem is _undefined: bLowMem=False
    # if strSeparator is _undefined: strSeparator=","
    # df = pd.read_csv(strPath + strFileName, sep=strSeparator, low_memory=bLowMem)
    df = pd.read_csv(strPath + strFileName, sep=strSeparator)
    return df

def askOK(prompt, retries=3, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes','Y'):
            return True
        if ok in ('n', 'no','N'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
    
def getDate(df,strFieldFrom='pickup_datetime',strFieldTo='DATE'):
    df[strFieldTo] = pd.DatetimeIndex(df[strFieldFrom]).date

def getTime(df,strFieldFrom='pickup_datetime',strFieldTo='TIME'):
    df[strFieldTo] = pd.DatetimeIndex(df[strFieldFrom]).time

def viewRange(strName, strFieldName,objX):
    print(strName)
    x_objX = objX[strFieldName]
    print("Min:" + x_objX.min())
    print("Max:" + x_objX.max())

def viewDFStructure(df):
    #print('Info:' + df.info())
    print('Describe:' + df.describe())
    print('DTypes:' + df.dtypes)
    print('NaN:' + df.isna().sum())
    

""" def MonsterConcat(lstItems,dfItems,strItemName="Item"):
     lstMonster = []
    for cV in lstItems:
        lstMonster.append(dfItems[cV])

    dfV = pd.DataFrame(pd.concat(lstMonster,axis=0,ignore_index=True,sort=True))
    dfV = dfV.rename(columns={0:strItemName})
    dfV = dfV.reset_index()

    dfV = pd.DataFrame(dfV).dropna()
    dfV.groupby(strItemName)
    #print(dfV)

    lstMonster = []
    for x in dfV[strItemName].unique():
        y = dfItems[((dfItems[strItemName]==x).sum()

        lstMonster.append([x,y])
        
    _ =pd.DataFrame(lstMonster)
    return _
    # askOK('Do you really want to quit?')
    # askOK('OK to overwrite the file?', 2)
    # askOK('OK to overwrite the file?', 2, 'Come on, only yes or no!')"""