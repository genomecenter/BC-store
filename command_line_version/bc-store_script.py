import sys
import os
import subprocess
import re
import pandas as pd
import matplotlib.pyplot as plt
import itertools

#CONST
#MGI barcode numbers
MGI_barcode_number=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                    '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34',
                    '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                    '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66',
                    '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82',
                    '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98',
                    '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112',
                    '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126',
                    '127', '128', '999']
#MGI barcode sequence
MGI_barcode_sequence=['TAGGTCCGAT', 'GGACGGAATC', 'CTTACTGCCG', 'ACCTAATTGA', 'TTCGTATCCG', 'GGTAACGAGC', 'CAACGTATAA', 'ACGTCGCGTT', 'TTCTGCTAGC', 'AGGAAGATAG', 'GCTCTTGCTT', 'CAAGCACGCA', 'CGGCAATCCG', 'ATCAGGATTC', 'TCATTCCAGA', 'GATGCTGGAT', 'GTGAGTGATG', 'GAGTCAGCTG', 'TGTCTGCGAA', 'ATTGGTACAA', 'CGATTGTGGT', 'ACAGACTTCC', 'TCCACACTCT', 'CACCACAAGC', 'TAGAGGACAA', 'CCTAGCGAAT', 'GTAGTCATCG', 'GCTGAGCTGT', 'AACCTAGATA', 'TTGCCATCTC', 'AGATCTTGCG', 'CGCTATCGGC', 'GCAACGATGG', 'TAATCGTTCA', 'GTTCGCTCTA', 'TCTCACACAT', 'CTGTTAGGAT', 'CGCAGACGCG', 'AAGGATCATC', 'AGCGTTGAGC', 'TTAGATGCAT', 'GTCCAGAGCT', 'CACGTGATAG', 'CCACTAGTCC', 'TGGACTTGGC', 'GCTTGACAGG', 'AAGACCTCTA', 'AGTTGCCATA', 'ATGTACGCAG', 'TTAATGAGAT', 'TGCGCCACTT', 'CATTAAGGCC', 'CCGCCTCAGA', 'AATCGGCTCG', 'GCCGGTTATC', 'GGAATATTGA', 'ATTCAACGGA', 'AACTGTACTG', 'GTACCTCAAT', 'GACTTCTAAT', 'TGAAGCGTTG', 'CGTGCGATCC', 'TCGGAAGGCA', 'CCGATGTCGC', 'ACTTAGAATG', 'TCCAAGCCTG', 'AGACGATGAT', 'CTCACAAGAC', 'CGTTCCTACT', 'GTGGTTGTGA', 'GAAGGCCTGC', 'TAGCTTGCCA', 'GACAATGCTC', 'GCTAATCACA', 'AGTCCATAGG', 'CTATCGCCTA', 'ATCGTGGTCT', 'TGGCTAATAC', 'CAGTGCAGAG', 'TCAGGCTGGT', 'ATACTCACGC', 'ATGCTCCGCG', 'TGTGAACTTG', 'GAGAGGTGCT', 'TGCACTGTAA', 'GCCTAGGCAA', 'CCATCATAGC', 'CATGGTAATT', 'CACCATGTCT', 'ATATGTCTGG', 'AAGGAAGCGT', 'TCAAGACGTC', 'CCGCTCAGTA', 'GGTGTGTACA', 'TTCACGTAAG', 'GGTTCCACAC', 'AGGTATTCTT', 'CGAATGCAAC', 'TTCAACGGCG', 'CTCGGCGGAA', 'ACGGTAATGG', 'GATCCGACGT', 'TCACGATACA', 'GATTCTCTTC', 'ACAATTAATA', 'ACCAGCATTA', 'CATCAGGCCC', 'CCTTCTCAAG', 'TAGCTCAACG', 'TAGTGCCCGT', 'GTTGAGAGAA', 'GCCTCATGGA', 'GGTCAACCTA', 'CCAGAGTCAG', 'AACAGGCAGT', 'GCTCCATGAC', 'ATGTCTATCC', 'CTTGACAAGG', 'TGTTTCGTTA', 'TGGAGTACCC', 'CCTTGATCAA', 'GGAAGTGGCA', 'AACATTCTAC', 'GACGCGAGTC', 'CTATAACACT', 'AGTCTCGTGT', 'TCGGCCTATG', 'TTGCAGACGG', 'GCGTATGCGG']
linenum=list(range(0,129))
#criteria
min_rate_strong = 0.15
max_rate_strong = 0.35
min_rate_lite = 0.07
max_rate_lite = 0.6
#lenght of barcodes
NUCLEN=10

#FUNCTIONS for running different options

def one_set_analisys(function_set, function_rate, MGI_barcode_sequence, \
                            MGI_barcode_number, min_rate_value, max_rate_value):
    names_index = []
    table_raiting = [[0 for i in range(4)] for j in range(NUCLEN)]
    ratesum = sum(function_rate)
    set_lenght = len(function_set)
    for i in range(0, set_lenght):
        names_index.append(MGI_barcode_number.index(str(function_set[i])))
    flag = 1
    for j in range(0, NUCLEN):
        reiting = [0, 0, 0, 0]  # A T G C
        for i in range(0, set_lenght):
            if MGI_barcode_sequence[names_index[i]][j] == 'A': reiting[0] += function_rate[i]
            if MGI_barcode_sequence[names_index[i]][j] == 'T': reiting[1] += function_rate[i]
            if MGI_barcode_sequence[names_index[i]][j] == 'G': reiting[2] += function_rate[i]
            if MGI_barcode_sequence[names_index[i]][j] == 'C': reiting[3] += function_rate[i]
        table_raiting[j][0] = round(reiting[0] / ratesum, 3)
        table_raiting[j][1] = round(reiting[1] / ratesum, 3)
        table_raiting[j][2] = round(reiting[2] / ratesum, 3)
        table_raiting[j][3] = round(reiting[3] / ratesum, 3)
        if not ((reiting[0] >= (min_rate_value * ratesum)) and
                (reiting[0] <= (max_rate_value * ratesum)) and
                (reiting[1] >= (min_rate_value * ratesum)) and
                (reiting[1] <= (max_rate_value * ratesum)) and
                (reiting[2] >= (min_rate_value * ratesum)) and
                (reiting[2] <= (max_rate_value * ratesum)) and
                (reiting[3] >= (min_rate_value * ratesum)) and
                (reiting[3] <= (max_rate_value * ratesum))):
            flag = 0
    if (flag == 1):
        result = '\nGood set'
    else:
        result = '\nBad set, try another one'
    return result, table_raiting

def check_set_function(custom_set,custom_rate,custom_criteria):
    custom_set_numbers_index=''
    for i in range(0, len(custom_set)):
        custom_set_numbers_index = custom_set_numbers_index + '\n' + \
                                    str(MGI_barcode_number[MGI_barcode_number.index(str(custom_set[i]))]) + \
                                    ' ' + str(MGI_barcode_sequence[MGI_barcode_number.index(str(custom_set[i]))])
    print('\n\nbarcodes:\n' + (','.join(custom_set)) + '\nrate:\n' + (','.join([str(i) for i in custom_rate])) + '\ncriteria: ' + str(custom_criteria))

    # CUSTOM RATE
    err_custom=''
    if custom_criteria=='strong':
        ressetreit_frac, table_rate_nucl_posfrac = one_set_analisys(custom_set, custom_rate, \
                                                        MGI_barcode_sequence, MGI_barcode_number, \
                                                        min_rate_strong, max_rate_strong)
    elif custom_criteria=='lite':
        ressetreit_frac, table_rate_nucl_posfrac = one_set_analisys(custom_set, custom_rate, \
                                                        MGI_barcode_sequence, MGI_barcode_number, \
                                                        min_rate_lite, max_rate_lite)
    #make table for plotting
    yA = []
    yT = []
    yG = []
    yC = []
    for i in range(0, NUCLEN):
        yA.append(table_rate_nucl_posfrac[i][0])
        yT.append(table_rate_nucl_posfrac[i][1])
        yG.append(table_rate_nucl_posfrac[i][2])
        yC.append(table_rate_nucl_posfrac[i][3])

    pr1_custom = "\nmin values \nA\tT\tG\tC\n" + str(min(yA)) + '\t' + str(min(yT)) + '\t' + str(min(yG)) + '\t' + str(min(yC))
    pr2_custom = "\nmax values \nA\tT\tG\tC\n" + str(max(yA)) + '\t' + str(max(yT)) + '\t' + str(max(yG)) + '\t' + str(max(yC))
    pr3_custom = "\ntotal min " + str(min(min(yA), min(yT), min(yG), min(yC)))
    pr4_custom = "\ntotal max " + str(max(max(yA), max(yT), max(yG), max(yC)))
    print('\nwith custom rate min and max values:\n' + pr1_custom + pr2_custom + pr3_custom + pr4_custom+'\n'+ressetreit_frac+'\n'+err_custom)

    #plotting
    x = list(range(1,11))
    x.reverse()

    plt.figure()

    plt.plot(x, yA, label="fraction A") # A
    plt.plot(x, yT, label="fraction T") # T
    plt.plot(x, yG, label="fraction G") # G
    plt.plot(x, yC, label="fraction C") # C

    plt.plot([1, NUCLEN], [min_rate_lite, min_rate_lite], color='k', linestyle='-', linewidth=3)
    plt.plot([1, NUCLEN], [max_rate_lite, max_rate_lite], color='k', linestyle='-', linewidth=3)
    plt.plot([1, NUCLEN], [min_rate_strong, min_rate_strong], color='k', linestyle='-', linewidth=2)
    plt.plot([1, NUCLEN], [max_rate_strong, max_rate_strong], color='k', linestyle='-', linewidth=2)

    plt.xlabel('nucleotide position in barcode') # naming the x axis
    plt.ylabel(' nucleotides fraction ') # naming the y axis
    plt.title('NUCLEOTIDES FRACTION FOR BARCODE SET CUSTOM RATE: set: ' + (','.join(custom_set)) + ' rate: ' + (','.join([str(i) for i in custom_rate]))) # giving a title to my graph
    plt.legend() # show a legend on the plot
    plt.show() # function to show the plot
    print('done')

def findsubsets(s, n):
    return list(itertools.combinations(s, n))

def add_to_set_function(custom_current_set,custom_how_many_add,custom_rate_with_add,custom_criteria,custom_from_barcodes):
    custom_set_numbers_index=''
    for i in range(0, len(custom_current_set)):
        custom_set_numbers_index = custom_set_numbers_index + '\n' + \
                                    str(MGI_barcode_number[MGI_barcode_number.index(str(custom_current_set[i]))]) + \
                                    ' ' + str(MGI_barcode_sequence[MGI_barcode_number.index(str(custom_current_set[i]))])
    print('\n\nbarcodes:\n' + (','.join(custom_current_set)) + '\nhow many add: '+ str(custom_how_many_add) + '\nrate with add:\n' + (','.join([str(i) for i in custom_rate_with_add])) + '\ncriteria: ' + str(custom_criteria) + '\nadd from:\n' + (','.join([str(i) for i in custom_from_barcodes])))

    # CUSTOM RATE
    err_custom=''
    if custom_criteria=='strong':
        min_rate=min_rate_strong
        max_rate=max_rate_strong

    elif custom_criteria=='lite':
        min_rate=min_rate_lite
        max_rate=max_rate_lite

    flag_good_set=0

    subsets=findsubsets(custom_from_barcodes,custom_how_many_add)
    number_of_subset=0
    while (flag_good_set==0 and number_of_subset<len(subsets)):
        ressetreit_frac, table_rate_nucl_posfrac = one_set_analisys(custom_current_set+list(subsets[number_of_subset]), custom_rate_with_add, \
                                                        MGI_barcode_sequence, MGI_barcode_number, \
                                                        min_rate, max_rate)
        if ressetreit_frac == '\nGood set':
            flag_good_set=1
        number_of_subset+=1

    if flag_good_set==0:
        print('\n\nNo good set exist')
    elif flag_good_set==1:
        print('\n\nGood set exist')
        print('\nBarcodes to add:\n'+str(subsets[number_of_subset]))
        #make table for plotting
        yA = []
        yT = []
        yG = []
        yC = []
        for i in range(0, NUCLEN):
            yA.append(table_rate_nucl_posfrac[i][0])
            yT.append(table_rate_nucl_posfrac[i][1])
            yG.append(table_rate_nucl_posfrac[i][2])
            yC.append(table_rate_nucl_posfrac[i][3])

        pr1_custom = "\nmin values \nA\tT\tG\tC\n" + str(min(yA)) + '\t' + str(min(yT)) + '\t' + str(min(yG)) + '\t' + str(min(yC))
        pr2_custom = "\nmax values \nA\tT\tG\tC\n" + str(max(yA)) + '\t' + str(max(yT)) + '\t' + str(max(yG)) + '\t' + str(max(yC))
        pr3_custom = "\ntotal min " + str(min(min(yA), min(yT), min(yG), min(yC)))
        pr4_custom = "\ntotal max " + str(max(max(yA), max(yT), max(yG), max(yC)))
        print('\nwith custom rate min and max values:\n' + pr1_custom + pr2_custom + pr3_custom + pr4_custom+'\n'+ressetreit_frac+'\n'+err_custom)

        #plotting
        x = list(range(1,11))
        x.reverse()

        plt.figure()

        plt.plot(x, yA, label="fraction A") # A
        plt.plot(x, yT, label="fraction T") # T
        plt.plot(x, yG, label="fraction G") # G
        plt.plot(x, yC, label="fraction C") # C

        plt.plot([1, NUCLEN], [min_rate_lite, min_rate_lite], color='k', linestyle='-', linewidth=3)
        plt.plot([1, NUCLEN], [max_rate_lite, max_rate_lite], color='k', linestyle='-', linewidth=3)
        plt.plot([1, NUCLEN], [min_rate_strong, min_rate_strong], color='k', linestyle='-', linewidth=2)
        plt.plot([1, NUCLEN], [max_rate_strong, max_rate_strong], color='k', linestyle='-', linewidth=2)

        plt.xlabel('nucleotide position in barcode') # naming the x axis
        plt.ylabel(' nucleotides fraction ') # naming the y axis
        plt.title('NUCLEOTIDES FRACTION FOR BARCODE SET CUSTOM RATE: set: ' + (','.join(custom_current_set+list(subsets[number_of_subset]))) + ' rate: ' + (','.join([str(i) for i in custom_rate_with_add]))) # giving a title to my graph
        plt.legend() # show a legend on the plot
        plt.show() # function to show the plot
        print('done')



#MAIN PART
option =  str(sys.argv[1])
if option == "check_set":
    error_flag = 0
    flag_argv=[0]*3
    for i in range(2,len(sys.argv)):
        if 'set' in sys.argv[i]:
            flag_argv[0]+=1
            set_line = str(sys.argv[i])
        elif 'rate' in sys.argv[i]:
            flag_argv[1]+=1
            rate_line = str(sys.argv[i])
        elif 'criteria' in sys.argv[i]:
            flag_argv[2]+=1
            criteria_line = str(sys.argv[i])
        else:
            print('\n', sys.argv[i],' is wrong argument\n')
            error_flag = 1
    if 0 in flag_argv:
        print('not all arguments provided')
        error_flag = 1
    if error_flag == 0:
        set = set_line.split("=")[1].split(",")
        if rate_line=='rate=equal':
            rate=[1.0]*len(set)
        else:
            rate = [float(i) for i in rate_line.split("=")[1].split(",")]
        criteria = criteria_line.split("=")[1]
        #while("" in set):
        #    set.remove("")
        #while("" in rate):
        #    rate.remove("")
        if (rate_line!='rate=equal') and (len(set) != len(rate)):
            print("\n\nDifferent lenght of set and rate. They must be equal")
            error_flag = 1
        if not (criteria=='strong' or criteria=='lite'):
            error_flag = 1
            print("\nWrong criteria name")
        # ADD other variants of mistakes
        #
        #
        if error_flag == 0:
            check_set_function(set,rate,criteria)

elif option == "add_to_set":
    error_flag = 0
    flag_argv=[0]*5
    for i in range(2,len(sys.argv)):
        if 'current_set' in sys.argv[i]:
            flag_argv[0]+=1
            current_set_line = str(sys.argv[i])
        elif 'how_many_add' in sys.argv[i]:
            flag_argv[1]+=1
            how_many_add_line = str(sys.argv[i])
        elif 'rate_with_add' in sys.argv[i]:
            flag_argv[2]+=1
            rate_with_add_line = str(sys.argv[i])
        elif 'criteria' in sys.argv[i]:
            flag_argv[3]+=1
            criteria_line = str(sys.argv[i])
        elif 'from_barcodes' in sys.argv[i]:
            flag_argv[4]+=1
            from_barcodes_line = str(sys.argv[i])
        else:
            print('\n', sys.argv[i],' is wrong argument\n')
            error_flag = 1
    if 0 in flag_argv:
        print('not all arguments provided')
        error_flag = 1
    if error_flag == 0:
        how_many_add=int(how_many_add_line.split("=")[1])
        current_set = current_set_line.split("=")[1].split(",")
        if rate_with_add_line=='rate_with_add=equal':
            rate_with_add=[1.0]*(len(current_set)+how_many_add)
        else:
            rate_with_add = [float(i) for i in rate_with_add_line.split("=")[1].split(",")]
        criteria = criteria_line.split("=")[1]
        from_barcodes = from_barcodes_line.split("=")[1].split(",")
        #while("" in set):
        #    set.remove("")
        #while("" in rate):
        #    rate.remove("")
        if (rate_with_add_line!='rate_with_add=equal') and (len(rate_with_add) != len(current_set)+how_many_add):
            print("\n\nDifferent lenght of current_set with how_many_add and rate_with_add. They must be equal")
            error_flag = 1
        if not (criteria=='strong' or criteria=='lite'):
            error_flag = 1
            print("\nWrong criteria name")
        # ADD other variants of mistakes
        #
        #
        if error_flag == 0:
            add_to_set_function(current_set,how_many_add,rate_with_add,criteria,from_barcodes)


elif option == "help":
    print(\
        "Welcome to BC-store.\n\nHere you can check your set by command like:\n"+\
        "python3 bc-store_script.py check_set set=1,2,3,4 rate=1,2,1,2 criteria=strong\n\n"+\
        "or add some barcodes to current set by command like:\n"+\
        "python3 bc-store_script.py add_to_set current_set=1,2,3,4 how_many_add=2 rate_with_add=1,2,1,2,3,4 criteria=lite from_barcodes=13,14,15,16\n\n"+\
        "avoid using spaces inside parameters\n\n"+\
        "also you can see MGI sets by command:\n"+\
        "python3 bc-store_script.py MGI_sets\n\n"+\
        "ask for help by command:\n"+\
        "python3 bc-store_script.py help\n\n"+\
        "MORE information about parameters:\n"+\
        "set - this parameter...\n"\
    )
elif option == "MGI_sets":
    print(\
        '\nset1: 1,2,3,4'+\
        '\nset2: 13,14,15,16'+\
        '\nset3: 41,42,43,44,45,46,47,48'+\
        '\nset4: 57,58,59,60,61,62,63,64'+\
        '\nset5: 65,66,67,68,69,70,71,72'+\
        '\nset6: 73,74,75,76,77,78,79,80'+\
        '\nset7: 81,82,83,84,85,86,87,88'+\
        '\nset8: 89,90,91,92,93,94,95,96'+\
        '\nset9: 97,98,99,100,101,102,103,104'+\
        '\nset10: 121,122,123,124,125,126,127,128'+\
        '\nsetbig: 25,26,117,28,29,30,114,32,33,34,35,36,'+\
                  '37,38,39,115,49,50,51,52,53,116,55,56\n'\
    )
else:
    print(\
        "\nincorrect command "+str(sys.argv[1])+"\n"+\
        "Please, run script with \"help\" like:\n"\
        "python3 bc-store_script.py help\n"\
        "to see the variants\n"\
   )
