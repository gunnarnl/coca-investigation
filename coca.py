import os
import pandas as pd

def mergePOS(tsv):
    text = ''
    for index, row in tsv.iterrows():
        if row['c1']=='<p>':
            text += '\n'
        else:
            text += str(row['c1'])+'_'+str(row['c2'])+' '
        print(text)
    return text


def main():
    file = 'wlp_acad_1990.txt'
    tsv = pd.read_csv(file, sep="\t", quoting=3, encoding='latin_1', header=0, names=['c1', 'c2'], usecols=[1,3])
    newtext = mergePOS(tsv)
    print(newtext)

main()
