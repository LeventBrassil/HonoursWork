import os
import csv
from pickle import TRUE
#Create List of Covid Variants
"""
with open('/Users/leventbrassil/Desktop/Honours/SARS-CoV-2_LongTermPassaging_Database_master_2022.csv','r') as reader:
    csvreader = csv.DictReader(reader)
    with open('/Users/leventbrassil/Desktop/Honours/nameList.csv','w') as writer:
        fieldNames = ['Original_ID','Seq_ID']

        csvwriter = csv.DictWriter(writer,fieldnames=fieldNames,delimiter=',')
        csvwriter.writeheader()
        for line in csvreader:
            del line['\ufeffnCoV_ID']
            del line['Passage_Number']
            del line['Cells']
            del line['Replicate']
            del line['Lineage']
            del line['Isolate_Name']
            del line['Episode_Number']
            del line['Culture_Date']
            del line['Sequencing_Date']
            del line['Notes']
            del line['']
            csvwriter.writerow(line)
"""
with open('/Users/leventbrassil/Desktop/Honours/nameList.csv','r') as reader:
    csvreader = csv.DictReader(reader)
    lgcounter = 0
    fkcuonter = 0
    for line in csvreader:
        
        if os.path.exists('/Volumes/LeventHons/Passaging_Data copy/reads/{}_L001_R1_001.fastq.gz'.format(line['Original_ID'])) == True:
            print('LETS GOOO')
            os.rename('/Volumes/LeventHons/Passaging_Data copy/reads/{}_L001_R1_001.fastq.gz'.format(line['Original_ID']),'/Volumes/LeventHons/Passaging_Data copy/reads/{}_R1.fastq.gz'.format(line['Seq_ID']))
            os.rename('/Volumes/LeventHons/Passaging_Data copy/reads/{}_L001_R2_001.fastq.gz'.format(line['Original_ID']),'/Volumes/LeventHons/Passaging_Data copy/reads/{}_R2.fastq.gz'.format(line['Seq_ID']))
            lgcounter += 1
        else:
            print("FUCK")
            fkcuonter += 1
        
    print( lgcounter, fkcuonter, (lgcounter + fkcuonter))

        #else:
            #print('Old name is {}, new name is {}'.format(line['Original_ID'],line['Seq_ID']))
            #os.rename('/Volumes/LeventHons/Passaging_Data copy/reads/{}.fastq.gz'.format(line['Original_ID']),'/Volumes/LeventHons/Passaging_Data copy/reads/{}.fastq.gz'.format(line['Seq_ID']))
            
