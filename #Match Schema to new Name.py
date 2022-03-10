#Match Schema to new Name
import csv

with open('/Users/leventbrassil/Desktop/passaging_schemes.csv','r') as scReader:
    scCSV = csv.DictReader(scReader)
    with open('/Users/leventbrassil/Desktop/Honours/Name_Schema_List.csv','w') as writer:
        fieldNames = ['Original_ID','Seq_ID','Scheme','location_charles_pc']
        CSVwriter = csv.DictWriter(writer,fieldnames=fieldNames,delimiter=",")
        CSVwriter.writeheader()

        for scline in scCSV:
            writeline = ({'Original_ID' : scline['file'],'Seq_ID' : 'None','Scheme' : scline['scheme'],'location_charles_pc' : scline['location_charles_pc']})
            
            with open('/Users/leventbrassil/Desktop/Honours/nameList.csv','r') as nameReader:
                nameCSV = csv.DictReader(nameReader)

                for nmline in nameCSV:
                    
                    if str(scline['file']) == str(nmline['Original_ID']):
                        writeline = ({'Original_ID' : scline['file'],'Seq_ID' : nmline['Seq_ID'],'Scheme' : scline['scheme'],'location_charles_pc' : scline['location_charles_pc']})
                
            CSVwriter.writerow(writeline)

