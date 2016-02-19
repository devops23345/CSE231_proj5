# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:40:34 2016

@author: ncolella
"""
total = 0

#file_name_input = input("Enter file name with extension:")
file_name_input = "national_M2014_dl.txt" 
outfile = open("output.txt","w")

while True:
    
    try: 
        fp = open(file_name_input)
        break
    except FileNotFoundError:
        print ("Error:  No file found with name:", file_name_input)    
        print ("Try Again")
        file_name_input = input("Enter file name with extension:")

header = fp.readline()## reads the first line which is the header.  you can then start
# reading the date in the for loop.
header = header.strip('\n')#strip the \n character of the end of line from the header
print("0123456789112345678921234567893123456789412345678951234567896123456789712345678981234567899123456789012345678911234567892123456789", file = outfile)
print('{:<110} {:<13} {:<13}'.format("Occ Descr", "Occ Group", "Average Salary"), file = outfile)

for line in fp:
    total += + 1
#    A_mean =  line[167:180]
#    asterix_index = A_mean.find("*")
#    if asterix_index == -1:
#        A_mean = int(A_mean)
#        print ("A_mean=", A_mean)

#
## parse data - coluomn 2
    occupation_descr = line[10:110]
    occupational_group = line[120:133]
    average_salary = line[172:185]
    print("Occ Descr:", occupation_descr, "Occ Group:", occupational_group)
    print("Avg salary:", average_salary)
    print('{:<110} {:<13} {:<13}'.format(occupation_descr, occupational_group, average_salary), file = outfile)
#
#
#
print("0123456789112345678921234567893123456789412345678951234567896123456789712345678981234567899123456789012345678911234567892123456789", file = outfile)
print ("Number of lines in file:", total) 
#






outfile.close()  
fp.close()
