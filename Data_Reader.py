#made by @l@murit
#name of csv file should be Data.csv
#name of text file should be out.txt
import csv
a=[]
with open('Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    l=0
    for r in csv_reader:
        if l<3:
            l+=1
        else:
            print(f'.......{r[0]}..{r[1]}')
            a.append(f'       {r[0]}  {r[1]}')
            l+=1
with open('out.txt', 'w') as t:
    t.write(f'   {len(a)}\n')
    for x in a:
        t.write(f'{x}\n')
