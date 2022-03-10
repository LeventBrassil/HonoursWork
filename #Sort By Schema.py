#Sort By Schema
import csv
import os

from pickle import TRUE
import shutil
import csv

with open('/Users/leventbrassil/Desktop/Honours/Name_Schema_List.csv','r') as reader:
    cread = csv.DictReader(reader)
    #os.makedirs('/Volumes/LeventHons/Passaging_Data_copy/reads/Midnight', '/Volumes/LeventHons/Passaging_Data_copy/reads/Eden')
    for line in cread:
        print("Searching for Seq_ID")
        if os.path.exists('/Volumes/LeventHons/Passaging_Data_copy/reads/{}_R1.fastq.gz'.format(line['Seq_ID'])) == True:
            shutil.copy('/Volumes/LeventHons/Passaging_Data_copy/reads/{}_R1.fastq.gz'.format(line['Seq_ID']),'/Volumes/LeventHons/Passaging_Data_copy/reads/{}/{}_R1.fastq.gz'.format(line['Scheme'],line['Seq_ID']))
            shutil.copy('/Volumes/LeventHons/Passaging_Data_copy/reads/{}_R2.fastq.gz'.format(line['Seq_ID']),'/Volumes/LeventHons/Passaging_Data_copy/reads/{}/{}_R2.fastq.gz'.format(line['Scheme'],line['Seq_ID']))
        elif os.path.exists('/Volumes/LeventHons/Passaging_Data_copy/reads/{}_L001_R1_001.fastq.gz'.format(line['Original_ID'])) == True:
            print("Searching Seq_ID failed, Checking Original_ID")
            shutil.copy('/Volumes/LeventHons/Passaging_Data_copy/reads/{}_l001_R1_001.fastq.gz'.format(line['Original_ID']),'/Volumes/LeventHons/Passaging_Data_copy/reads/{}/{}_R1.fastq.gz'.format(line['Scheme'],line['Original_ID']))
            shutil.copy('/Volumes/LeventHons/Passaging_Data_copy/reads/{}_L001_R2_001.fastq.gz'.format(line['Original_ID']),'/Volumes/LeventHons/Passaging_Data_copy/reads/{}/{}_R2.fastq.gz'.format(line['Scheme'],line['Original_ID']))
        else:
            print("Error, No File Found")