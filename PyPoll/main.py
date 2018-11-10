# Modules
import os
import csv
   

#Declare variables
total_votes=0
poll_data_cand = []
cand_name =""
total_votes_cand = 0
total_perc_cand = 0.000
d ={}

print('\n Election Results\n' + '-' *30)

with open("election_data.csv") as f:
    reader = csv.reader(f)
    next(reader)

    #Candidates Name
    for row in reader:
        poll_data_cand.append(row[2])
        
        
 #Total Votes     
    total_votes = len(poll_data_cand) 
    print(f'Total Votes: {total_votes}\n' + '-'*30)

sort_can = sorted(poll_data_cand)
cand_name = poll_data_cand[1]
list_cand = []
list_perc = []
list_tot  = []

for x in range(len(sort_can)):
   
    if sort_can[x] == cand_name:
        total_votes_cand+=1
        cand_name=sort_can[x]
        if total_votes == x+1:
            total_perc_cand=total_votes_cand/total_votes*100
            print(f'{cand_name}: {round(total_perc_cand,0)}% ({total_votes_cand})\n') 
            list_cand.append(cand_name)
            list_perc.append(round(total_perc_cand,0))
            list_tot.append(total_votes_cand)
            
    else:
        total_perc_cand=total_votes_cand/total_votes*100
        print(f'{cand_name}: {round(total_perc_cand,0)}% ({total_votes_cand})\n')
        list_cand.append(cand_name)
        list_perc.append(round(total_perc_cand,0))
        list_tot.append(total_votes_cand)
        
        total_votes_cand = 1
        cand_name=sort_can[x]

d = dict(zip(list_cand,zip(list_perc,list_tot)))
print('-'*30)
key_max = max(d.keys(),key=(lambda k: d[k]))
print(f'Winner:{key_max}')
print('-'*30)

#Output to text file
with open('election_results.txt',"w") as txt_file:
    txt_file.write(f'\n Election Results\n' + '-' *30)
    txt_file.write(f'\nTotal Votes: {total_votes}\n' + '-'*30)
    for key,v in d.items():
        txt_file.write(f'\n{key,v}\n')
    txt_file.write(f'-'*30)
    txt_file.write(f'\nWinner:{key_max}\n')
    txt_file.write(f'-'*30)