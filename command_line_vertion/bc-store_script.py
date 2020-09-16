import sys
import os
import subprocess
import re
import pandas as pd
import matplotlib.pyplot as plt

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
        result = 'good set'
    else:
        result = 'bed set, try another one'
    return result, table_raiting

def check_set_function(custom_set,custom_rate,custom_criteria):
    custom_set_numbers_index=''
    for i in range(0, len(custom_set)):
        custom_set_numbers_index = custom_set_numbers_index + '\n' + \
                                    str(MGI_barcode_number[MGI_barcode_number.index(str(custom_set[i]))]) + \
                                    ' ' + str(MGI_barcode_sequence[MGI_barcode_number.index(str(custom_set[i]))])
    print('\n\nbarcodes:\n' + (','.join(custom_set)) + '\nrate:\n' + (','.join([str(i) for i in custom_rate])) + '\ncriteria:\n' + str(custom_criteria))

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

    pr1_custom = "min values A T G C " + str(min(yA)) + ' ' + str(min(yT)) + ' ' + str(min(yG)) + ' ' + str(min(yC))
    pr2_custom = "\nmin values A T G C " + str(max(yA)) + ' ' + str(max(yT)) + ' ' + str(max(yG)) + ' ' + str(max(yC))
    pr3_custom = "\nmin " + str(min(min(yA), min(yT), min(yG), min(yC)))
    pr4_custom = "\nmax " + str(max(max(yA), max(yT), max(yG), max(yC)))
    print('\n\nwith custom rate min and max values:\n' + pr1_custom + pr2_custom + pr3_custom + pr4_custom+'\n'+ressetreit_frac+'\n'+err_custom)

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

#MAIN PART
option =  str(sys.argv[1])
if option == "check_set":
    error_flag = 0
    set_line = str(sys.argv[2])
    rate_line = str(sys.argv[3])
    criteria_line = str(sys.argv[4])
    # ADD variants of mistakes
    #
    #
    set = set_line.split("=")[1].split(",")
    rate = [float(i) for i in rate_line.split("=")[1].split(",")]
    criteria = criteria_line.split("=")[1]
    if (set_line.split("=")[0] != "set") or \
       (rate_line.split("=")[0] != "rate") or \
       (criteria_line.split("=")[0] != "criteria"):
        print("\n\nProblem with parameters. Please, use \"help\"")
        error_flag = 1
    else:
        while("" in set):
            set.remove("")
        while("" in rate):
            rate.remove("")
        if len(set) != len(rate):
            print("\n\nDifferent lenght of set and rate. It must be equal")
            error_flag = 1
    # ADD other variants of mistakes
    #
    #
    if error_flag == 0:
        check_set_function(set,rate,criteria)

elif option == "add_to_set":
    current_set = str(sys.argv[2])
    current_rate = str(sys.argv[3])
    how_many_add = str(sys.argv[4])
    rate_add = str(sys.argv[6])
    criteria = str(sys.argv[7])
    from_barcodes = str(sys.argv[8])
elif option == "help":
    print(\
        "Welcome to BC-store.\n\nHere you can check your set by command like:\n"+\
        "python3 bc-store_script.py check_set set=1,2,3,4 rate=1,2,1,2 criteria=strong\n\n"+\
        "or add some barcodes to current set by command like:\n"+\
        "python3 bc-store_script.py add_to_set current_set=1,2,3,4 current_rate=1,2,1,2 how_many_add=2 rate_add=3,4 criteria=lite from_barcodes=13,14,15,16\n\n"+\
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
        "\nincorrect option\n"+\
        "Please, run script with \"help\" like:\n"\
        "python3 bc-store_script.py help\n"\
        "to see the variants\n"\
   )
