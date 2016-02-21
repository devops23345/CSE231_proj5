# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:40:34 2016

@author: ncolella
"""
count = 0
occ_descr_keyword = ""
A_mean_max = 0
A_mean_min = 1000000
occ_descr_min = ""
occ_descr_max = ""
total_salary = 0

#file_name_input = input("Enter file name with extension:")
file_name_input = "national_M2014_dl.txt" 
#outfile = open("output.txt","w")

while True:
    
    try: 
        fp = open(file_name_input, "r")
        break
    except FileNotFoundError:
        print ("Error:  No file found with name:", file_name_input)    
        print ("Try Again")
        file_name_input = input("Enter file name with extension:")

header = fp.readline()## reads the first line which is the header.  you can then start
# reading the date in the for loop.
#print("0123456789112345678921234567893123456789412345678951234567896123456789712345678981234567899123456789012345678911234567892123456789", file = outfile)
#print('{:<110} {:<13} {:<13}'.format("Occ Descr", "Occ Group", "Average Salary"), file = outfile)


occ_descr_keyword = input("Enter keyword:")

check_for_keyword = occ_descr_keyword.isalpha()   #check to see if anything entered

if check_for_keyword == True: #parse occ descr for keyword if no keyword then print all occ
    #convert keyword to lowercase
    occ_descr_keyword = occ_descr_keyword.lower()

    print("Salary    Occupation")    
    
    for line in fp:


    # parse data - occupation description column
        occupation_descr = line[10:110]
        occupational_group = line[120:133]

    # convert to lower case to search for keyword
        occupation_descr_lower = occupation_descr.lower()
        
    # only search rows that have group coded as "detailed"
        if "detailed" in occupational_group:

        # search the description for the keyword
            if occ_descr_keyword in occupation_descr_lower:
                A_mean = line[172:185]
                if "*" in A_mean:#skip positions with * in salary column
                    continue 

                else:# valid salary 
                    count += + 1
                    
                    #convert from string to int
                    A_mean = int(A_mean)
                    if A_mean < A_mean_min:
                        A_mean_min = A_mean
                        occ_descr_min = occupation_descr
                    if A_mean > A_mean_max:
                        A_mean_max = A_mean
                        occ_descr_max = occupation_descr
                        
                    total_salary = total_salary + A_mean

                    print('${:>7,} ' ' {}'.format(A_mean, occupation_descr))

                        
        else:
             continue

         
    print("")
    if count > 1:
        average_salary = total_salary/count
        print('Max: ${:>7,} ' ' {}'.format(A_mean_max, occ_descr_max))
        print('Min: ${:>7,} ' ' {}'.format(A_mean_min, occ_descr_min))
        print("")
        print('Across {} occupations the average salary was ${:,}'.format(count, average_salary))
    elif count == 1:
        print('Across {} occupation the average salary was ${:,}'.format(count, average_salary))
    else:  #nothing found count = 0
        print('No matches found')
        
        
    #
    ## parse data - coloumns
#        occupation_descr = line[10:110]
#        occupational_group = line[120:133]
#        average_salary = line[172:185]
#        print("Occ Descr:", occupation_descr, "Occ Group:", occupational_group)
#        print("Avg salary:", average_salary)
#        print('{:<110} {:<13} {:<13}'.format(occupation_descr, occupational_group, average_salary), file = outfile)
##
#
#
else: #nothing entered or numbers entered.  print out all occupatons and max/mins
    print("Salary    Occupation")    
    
    for line in fp:


    # parse data - occupation description column
        occupation_descr = line[10:110]
        occupational_group = line[120:133]
        
    # only search rows that have group coded as "detailed"
        if "detailed" in occupational_group:

            A_mean = line[172:185]
            if "*" in A_mean:#skip positions with * in salary column
                continue 

            else:# valid salary 
                count += + 1
                
                #convert from string to int
                A_mean = int(A_mean)
                if A_mean < A_mean_min:
                    A_mean_min = A_mean
                    occ_descr_min = occupation_descr
                if A_mean > A_mean_max:
                    A_mean_max = A_mean
                    occ_descr_max = occupation_descr
                    
                total_salary = total_salary + A_mean

                print('${:>7,} ' ' {}'.format(A_mean, occupation_descr))

                        
        else:
             continue

    average_salary = total_salary/count
         
    print("")
    print('Max: ${:>7,} ' ' {}'.format(A_mean_max, occ_descr_max))
    print('Min: ${:>7,} ' ' {}'.format(A_mean_min, occ_descr_min))
    print("")
    print('Across {} occupations the average salary was ${:,}'.format(count, average_salary))






#outfile.close()  
fp.close()
