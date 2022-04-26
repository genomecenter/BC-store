# https://tproger.ru/translations/python-gui-pyqt/

import itertools
import sys  # sys нужен для передачи argv в QApplication

import designwhole  # Это наш конвертированный файл дизайна
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, designwhole.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.checkset)
        self.pushButton_2.clicked.connect(self.addtoset)
        self.pushButton_3.clicked.connect(self.viewset)

    def viewset(self):
        string = '\nset1: 1, 2, 3, 4' + '\nset2: 13, 14, 15, 16' + \
                 '\nset3: 41, 42, 43, 44, 45, 46, 47, 48' + \
                 '\nset4: 57, 58, 59, 60, 61, 62, 63, 64' + \
                 '\nset5: 65, 66, 67, 68, 69, 70, 71, 72' + \
                 '\nset6: 73, 74, 75, 76, 77, 78, 79, 80' + \
                 '\nset7: 81, 82, 83, 84, 85, 86, 87, 88' + \
                 '\nset8: 89, 90, 91, 92, 93, 94, 95, 96' + \
                 '\nset9: 97, 98, 99, 100, 101, 102, 103, 104' + \
                 '\nset10: 121, 122, 123, 124, 125, 126, 127, 128' + \
                 '\nsetbig: 25, 26, 117, 28, 29, 30, 114, 32, 33, 34, 35, 36, 37, 38, 39, 115, ' + \
                 '49, 50, 51, 52, 53, 116, 55, 56' + \
                 '\nsetGC_ABCD: 1A, 1B, 1C, 1D, 2A, 2B, 2C, 2D, 3A, 3B, 3C, 3D, 4A, 4B, 4C, 4D, ' \
                 '13A, 13B, 13C, 13D, 14A, 14B, 14C, 14D, 15A, 15B, 15C, 15D, 16A, 16B, 16C, 16D, ' \
                 '25A, 25B, 25C, 25D, 26A, 26B, 26C, 26D, 29A, 29B, 29C, 29D, 32A, 32B, 32C, 32D, ' \
                 '33A, 33B, 33C, 33D, 35A, 35B, 35C, 35D, 36A, 36B, 36C, 36D, 37A, 37B, 37C, 37D, ' \
                 '38A, 38B, 38C, 38D, 41A, 41B, 41C, 41D, 42A, 42B, 42C, 42D, 43A, 43B, 43C, 43D, ' \
                 '44A, 44B, 44C, 44D, 47A, 47B, 47C, 47D, 48A, 48B, 48C, 48D, 51A, 51B, 51C, 51D, ' \
                 '53A, 53B, 53C, 53D, 55A, 55B, 55C, 55D, 56A, 56B, 56C, 56D, 57A, 57B, 57C, 57D, ' \
                 '59A, 59B, 59C, 59D, 61A, 61B, 61C, 61D, 62A, 62B, 62C, 62D, 63A, 63B, 63C, 63D, ' \
                 '64A, 64B, 64C, 64D, 65A, 65B, 65C, 65D, 66A, 66B, 66C, 66D, 68A, 68B, 68C, 68D, ' \
                 '69A, 69B, 69C, 69D, 71A, 71B, 71C, 71D, 72A, 72B, 72C, 72D, 75A, 75B, 75C, 75D, ' \
                 '76A, 76B, 76C, 76D, 77A, 77B, 77C, 77D, 79A, 79B, 79C, 79D, 80A, 80B, 80C, 80D, ' \
                 '81A, 81B, 81C, 81D, 82A, 82B, 82C, 82D, 83A, 83B, 83C, 83D, 84A, 84B, 84C, 84D, ' \
                 '85A, 85B, 85C, 85D, 86A, 86B, 86C, 86D, 88A, 88B, 88C, 88D, 89A, 89B, 89C, 89D, ' \
                 '92A, 92B, 92C, 92D, 93A, 93B, 93C, 93D, 95A, 95B, 95C, 95D, 100A, 100B, 100C, 100D, ' \
                 '104A, 104B, 104C, 104D, 117A, 117B, 117C, 117D, 121A, 121B, 121C, 121D, ' \
                 '122A, 122B, 122C, 122D, 124A, 124B, 124C, 124D, 125A, 125B, 125C, 125D, 127A, 127B, 127C, 127D\n'

        self.textBrowser_3.append(string)

    def checkset(self):
        data_num = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34',
            '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
            '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66',
            '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82',
            '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98',
            '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112',
            '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126',
            '127', '128', '999',
            '1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D', '3A', '3B', '3C', '3D', '4A', '4B', '4C', '4D',
            '13A', '13B', '13C', '13D', '14A', '14B', '14C', '14D', '15A', '15B', '15C', '15D',
            '16A', '16B', '16C', '16D', '25A', '25B', '25C', '25D', '26A', '26B', '26C', '26D',
            '29A', '29B', '29C', '29D', '32A', '32B', '32C', '32D', '33A', '33B', '33C', '33D',
            '35A', '35B', '35C', '35D', '36A', '36B', '36C', '36D', '37A', '37B', '37C', '37D',
            '38A', '38B', '38C', '38D', '41A', '41B', '41C', '41D', '42A', '42B', '42C', '42D',
            '43A', '43B', '43C', '43D', '44A', '44B', '44C', '44D', '47A', '47B', '47C', '47D',
            '48A', '48B', '48C', '48D', '51A', '51B', '51C', '51D', '53A', '53B', '53C', '53D',
            '55A', '55B', '55C', '55D', '56A', '56B', '56C', '56D', '57A', '57B', '57C', '57D',
            '59A', '59B', '59C', '59D', '61A', '61B', '61C', '61D', '62A', '62B', '62C', '62D',
            '63A', '63B', '63C', '63D', '64A', '64B', '64C', '64D', '65A', '65B', '65C', '65D',
            '66A', '66B', '66C', '66D', '68A', '68B', '68C', '68D', '69A', '69B', '69C', '69D',
            '71A', '71B', '71C', '71D', '72A', '72B', '72C', '72D', '75A', '75B', '75C', '75D',
            '76A', '76B', '76C', '76D', '77A', '77B', '77C', '77D', '79A', '79B', '79C', '79D',
            '80A', '80B', '80C', '80D', '81A', '81B', '81C', '81D', '82A', '82B', '82C', '82D',
            '83A', '83B', '83C', '83D', '84A', '84B', '84C', '84D', '85A', '85B', '85C', '85D',
            '86A', '86B', '86C', '86D', '88A', '88B', '88C', '88D', '89A', '89B', '89C', '89D',
            '92A', '92B', '92C', '92D', '93A', '93B', '93C', '93D', '95A', '95B', '95C', '95D',
            '100A', '100B', '100C', '100D', '104A', '104B', '104C', '104D', '117A', '117B', '117C', '117D',
            '121A', '121B', '121C', '121D', '122A', '122B', '122C', '122D', '124A', '124B', '124C', '124D',
            '125A', '125B', '125C', '125D', '127A', '127B', '127C', '127D'
        ]
        # MGI barcode sequence
        data_seq = [
            'TAGGTCCGAT', 'GGACGGAATC', 'CTTACTGCCG', 'ACCTAATTGA', 'TTCGTATCCG', 'GGTAACGAGC', 'CAACGTATAA',
            'ACGTCGCGTT', 'TTCTGCTAGC', 'AGGAAGATAG', 'GCTCTTGCTT', 'CAAGCACGCA', 'CGGCAATCCG', 'ATCAGGATTC',
            'TCATTCCAGA', 'GATGCTGGAT', 'GTGAGTGATG', 'GAGTCAGCTG', 'TGTCTGCGAA', 'ATTGGTACAA', 'CGATTGTGGT',
            'ACAGACTTCC', 'TCCACACTCT', 'CACCACAAGC', 'TAGAGGACAA', 'CCTAGCGAAT', 'GTAGTCATCG', 'GCTGAGCTGT',
            'AACCTAGATA', 'TTGCCATCTC', 'AGATCTTGCG', 'CGCTATCGGC', 'GCAACGATGG', 'TAATCGTTCA', 'GTTCGCTCTA',
            'TCTCACACAT', 'CTGTTAGGAT', 'CGCAGACGCG', 'AAGGATCATC', 'AGCGTTGAGC', 'TTAGATGCAT', 'GTCCAGAGCT',
            'CACGTGATAG', 'CCACTAGTCC', 'TGGACTTGGC', 'GCTTGACAGG', 'AAGACCTCTA', 'AGTTGCCATA', 'ATGTACGCAG',
            'TTAATGAGAT', 'TGCGCCACTT', 'CATTAAGGCC', 'CCGCCTCAGA', 'AATCGGCTCG', 'GCCGGTTATC', 'GGAATATTGA',
            'ATTCAACGGA', 'AACTGTACTG', 'GTACCTCAAT', 'GACTTCTAAT', 'TGAAGCGTTG', 'CGTGCGATCC', 'TCGGAAGGCA',
            'CCGATGTCGC', 'ACTTAGAATG', 'TCCAAGCCTG', 'AGACGATGAT', 'CTCACAAGAC', 'CGTTCCTACT', 'GTGGTTGTGA',
            'GAAGGCCTGC', 'TAGCTTGCCA', 'GACAATGCTC', 'GCTAATCACA', 'AGTCCATAGG', 'CTATCGCCTA', 'ATCGTGGTCT',
            'TGGCTAATAC', 'CAGTGCAGAG', 'TCAGGCTGGT', 'ATACTCACGC', 'ATGCTCCGCG', 'TGTGAACTTG', 'GAGAGGTGCT',
            'TGCACTGTAA', 'GCCTAGGCAA', 'CCATCATAGC', 'CATGGTAATT', 'CACCATGTCT', 'ATATGTCTGG', 'AAGGAAGCGT',
            'TCAAGACGTC', 'CCGCTCAGTA', 'GGTGTGTACA', 'TTCACGTAAG', 'GGTTCCACAC', 'AGGTATTCTT', 'CGAATGCAAC',
            'TTCAACGGCG', 'CTCGGCGGAA', 'ACGGTAATGG', 'GATCCGACGT', 'TCACGATACA', 'GATTCTCTTC', 'ACAATTAATA',
            'ACCAGCATTA', 'CATCAGGCCC', 'CCTTCTCAAG', 'TAGCTCAACG', 'TAGTGCCCGT', 'GTTGAGAGAA', 'GCCTCATGGA',
            'GGTCAACCTA', 'CCAGAGTCAG', 'AACAGGCAGT', 'GCTCCATGAC', 'ATGTCTATCC', 'CTTGACAAGG', 'TGTTTCGTTA',
            'TGGAGTACCC', 'CCTTGATCAA', 'GGAAGTGGCA', 'AACATTCTAC', 'GACGCGAGTC', 'CTATAACACT', 'AGTCTCGTGT',
            'TCGGCCTATG', 'TTGCAGACGG', 'GCGTATGCGG',

            'TAGGTCCGAT', 'GTCCGAACTG', 'CGAACTTAGC', 'ACTTAGGTCA', 'GGACGGAATC', 'CCTACCTTGA', 'AAGTAAGGCT',
            'TTCGTTCCAG', 'CTTACTGCCG', 'AGGTAGCAAC', 'TCCGTCATTA', 'GAACGATGGT', 'ACCTAATTGA', 'TAAGTTGGCT',
            'GTTCGGCCAG', 'CGGACCAATC', 'CGGCAATCCG', 'ACCATTGAAC', 'TAATGGCTTA', 'GTTGCCAGGT', 'ATCAGGATTC',
            'TGATCCTGGA', 'GCTGAAGCCT', 'CAGCTTCAAG', 'TCATTCCAGA', 'GATGGAATCT', 'CTGCCTTGAG', 'AGCAAGGCTC',
            'GATGCTGGAT', 'CTGCAGCCTG', 'AGCATCAAGC', 'TCATGATTCA', 'TAGAGGACAA', 'GTCTCCTATT', 'CGAGAAGTGG',
            'ACTCTTCGCC', 'CCTAGCGAAT', 'AAGTCACTTG', 'TTCGATAGGC', 'GGACTGTCCA', 'AACCTAGATA', 'TTAAGTCTGT',
            'GGTTCGAGCG', 'CCGGACTCAC', 'CGCTATCGGC', 'ACAGTGACCA', 'TATCGCTAAT', 'GTGACAGTTG', 'GCAACGATGG',
            'CATTACTGCC', 'ATGGTAGCAA', 'TGCCGTCATT', 'GTTCGCTCTA', 'CGGACAGAGT', 'ACCTATCTCG', 'TAAGTGAGAC',
            'TCTCACACAT', 'GAGATATATG', 'CTCTGTGTGC', 'AGAGCGCGCA', 'CTGTTAGGAT', 'AGCGGTCCTG', 'TCACCGAAGC',
            'GATAACTTCA', 'CGCAGACGCG', 'ACATCTACAC', 'TATGAGTATA', 'GTGCTCGTGT', 'TTAGATGCAT', 'GGTCTGCATG',
            'CCGAGCATGC', 'AACTCATGCA', 'GTCCAGAGCT', 'CGAATCTCAG', 'ACTTGAGATC', 'TAGGCTCTGA', 'CACGTGATAG',
            'ATACGCTGTC', 'TGTACAGCGA', 'GCGTATCACT', 'CCACTAGTCC', 'AATAGTCGAA', 'TTGTCGACTT', 'GGCGACTAGG',
            'AAGACCTCTA', 'TTCTAAGAGT', 'GGAGTTCTCG', 'CCTCGGAGAC', 'AGTTGCCATA', 'TCGGCAATGT', 'GACCATTGCG',
            'CTAATGGCAC', 'TGCGCCACTT', 'GCACAATAGG', 'CATATTGTCC', 'ATGTGGCGAA', 'CCGCCTCAGA', 'AACAAGATCT',
            'TTATTCTGAG', 'GGTGGAGCTC', 'GCCGGTTATC', 'CAACCGGTGA', 'ATTAACCGCT', 'TGGTTAACAG', 'GGAATATTGA',
            'CCTTGTGGCT', 'AAGGCGCCAG', 'TTCCACAATC', 'ATTCAACGGA', 'TGGATTACCT', 'GCCTGGTAAG', 'CAAGCCGTTC',
            'GTACCTCAAT', 'CGTAAGATTG', 'ACGTTCTGGC', 'TACGGAGCCA', 'TGAAGCGTTG', 'GCTTCACGGC', 'CAGGATACCA',
            'ATCCTGTAAT', 'CGTGCGATCC', 'ACGCACTGAA', 'TACATAGCTT', 'GTATGTCAGG', 'TCGGAAGGCA', 'GACCTTCCAT',
            'CTAAGGAATG', 'AGTTCCTTGC', 'CCGATGTCGC', 'AACTGCGACA', 'TTAGCACTAT', 'GGTCATAGTG', 'ACTTAGAATG',
            'TAGGTCTTGC', 'GTCCGAGGCA', 'CGAACTCCAT', 'TCCAAGCCTG', 'GAATTCAAGC', 'CTTGGATTCA', 'AGGCCTGGAT',
            'CTCACAAGAC', 'AGATATTCTA', 'TCTGTGGAGT', 'GAGCGCCTCG', 'CGTTCCTACT', 'ACGGAAGTAG', 'TACCTTCGTC',
            'GTAAGGACGA', 'GAAGGCCTGC', 'CTTCCAAGCA', 'AGGAATTCAT', 'TCCTTGGATG', 'TAGCTTGCCA', 'GTCAGGCAAT',
            'CGATCCATTG', 'ACTGAATGGC', 'AGTCCATAGG', 'TCGAATGTCC', 'GACTTGCGAA', 'CTAGGCACTT', 'CTATCGCCTA',
            'AGTGACAAGT', 'TCGCTATTCG', 'GACAGTGGAC', 'ATCGTGGTCT', 'TGACGCCGAG', 'GCTACAACTC', 'CAGTATTAGA',
            'CAGTGCAGAG', 'ATCGCATCTC', 'TGACATGAGA', 'GCTATGCTCT', 'TCAGGCTGGT', 'GATCCAGCCG', 'CTGAATCAAC',
            'AGCTTGATTA', 'ATACTCACGC', 'TGTAGATACA', 'GCGTCTGTAT', 'CACGAGCGTG', 'ATGCTCCGCG', 'TGCAGAACAC',
            'GCATCTTATA', 'CATGAGGTGT', 'TGTGAACTTG', 'GCGCTTAGGC', 'CACAGGTCCA', 'ATATCCGAAT', 'GAGAGGTGCT',
            'CTCTCCGCAG', 'AGAGAACATC', 'TCTCTTATGA', 'TGCACTGTAA', 'GCATAGCGTT', 'CATGTCACGG', 'ATGCGATACC',
            'GCCTAGGCAA', 'CAAGTCCATT', 'ATTCGAATGG', 'TGGACTTGCC', 'CATGGTAATT', 'ATGCCGTTGG', 'TGCAACGGCC',
            'GCATTACCAA', 'CACCATGTCT', 'ATAATGCGAG', 'TGTTGCACTC', 'GCGGCATAGA', 'TCAAGACGTC', 'GATTCTACGA',
            'CTGGAGTACT', 'AGCCTCGTAG', 'CCGCTCAGTA', 'AACAGATCGT', 'TTATCTGACG', 'GGTGAGCTAC', 'TTCACGTAAG',
            'GGATACGTTC', 'CCTGTACGGA', 'AAGCGTACCT', 'CTCGGCGGAA', 'AGACCACCTT', 'TCTAATAAGG', 'GAGTTGTTCC',
            'GATTCTCTTC', 'CTGGAGAGGA', 'AGCCTCTCCT', 'TCAAGAGAAG', 'ATGTCTATCC', 'TGCGAGTGAA', 'GCACTCGCTT',
            'CATAGACAGG', 'CCTTGATCAA', 'AAGGCTGATT', 'TTCCAGCTGG', 'GGAATCAGCC', 'GGAAGTGGCA', 'CCTTCGCCAT',
            'AAGGACAATG', 'TTCCTATTGC', 'GACGCGAGTC', 'CTACACTCGA', 'AGTATAGACT', 'TCGTGTCTAG', 'CTATAACACT',
            'AGTGTTATAG', 'TCGCGGTGTC', 'GACACCGCGA', 'TCGGCCTATG', 'GACCAAGTGC', 'CTAATTCGCA', 'AGTTGGACAT',
        ]

        linenum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                   53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                   78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
                   102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121,
                   122, 123, 124, 125, 126, 127, 128]

        # CONST VALUES
        NUCLEN = 10  # lenght of barcode
        mind0 = 0.15
        maxd0 = 0.35
        minnoise0 = 0.17
        maxnoise0 = 0.54
        mind = 0.07
        maxd = 0.6
        minnoise = 0.07
        maxnoise = 0.67

        str1 = self.textEdit.toPlainText()
        str1.replace(" ", "")

        names1 = [str(x.strip()) for x in str1.split(',')]

        str2 = self.textEdit_2.toPlainText()
        str2.replace(" ", "")
        # print(str2, '2')
        if (str2 != 'all1') and (len(str2) != 0):
            rate2 = [float(x.strip()) for x in str2.split(',')]
        if (str2 == 'all1') or (len(str2) == 0):
            rate2 = ['all1']
            str2 = "equal rate"
        # print(rate2, '2')
        # print(str1, names1, str2, rate2)
        # self.textBrowser_3.setText(str1+str2)
        self.textBrowser_3.setText('barcodes:\n' + str1 + '\nrate:\n' + str2)

        # WHOLE CODE FOR SET ANALISYS WITH PLOTS
        names = names1
        rate = rate2
        ln = len(names)
        # print(names,rate,ln)
        # print(data_num)

        nucllen = ''
        for i in range(0, ln):
            nucllen = nucllen + '\n' + str(data_num[data_num.index(str(names[i]))]) + ' ' + str(
                data_seq[data_num.index(str(names[i]))])

        tablereit = [[0 for i in range(4)] for j in range(NUCLEN)]
        # print (tablereit)
        tablenoise = [[0 for i in range(4)] for j in range(NUCLEN)]
        # print(tablenoise)
        # ressetreit, tablereit = onesetanalisys(names, NUCLEN, data_seq, data_num, mind0, maxd0)
        # ressetnoise, tablenoise = noiselevel(names, NUCLEN, data_seq, data_num, minnoise0, maxnoise0)

        # RATE
        err_set_analysis = ''
        if (len(rate) != 0) and (len(rate) != len(names)):
            rate = [1] * len(names)
            err_set_analysis = 'Barcode and rate length are not the same, so I use equal rate'
            str2 = 'equal rate'
        if (rate[0] == 'all1') or (len(rate) == 0):
            rate = [1] * len(names)

        ressetreitfrac, tablereitfrac = onesetwithrateanalisys(names, rate, NUCLEN, data_seq, data_num, mind0, maxd0)
        # print(ressetreitfrac, tablereitfrac)

        # PLOT3
        # PLOT THE NUCLEOTIDES FRACTION FOR BARCODE SET WITH RATE
        x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        yA = []
        yT = []
        yG = []
        yC = []

        for i in range(0, NUCLEN):
            yA.append(tablereitfrac[i][0])
            yT.append(tablereitfrac[i][1])
            yG.append(tablereitfrac[i][2])
            yC.append(tablereitfrac[i][3])

        pr5 = "min values A T G C " + str(min(yA)) + ' ' + str(min(yT)) + ' ' + str(min(yG)) + ' ' + str(min(yC))
        pr6 = "\nmin values A T G C " + str(max(yA)) + ' ' + str(max(yT)) + ' ' + str(max(yG)) + ' ' + str(max(yC))
        pr7 = "\nmin " + str(min(min(yA), min(yT), min(yG), min(yC)))
        pr8 = "\nmax " + str(max(max(yA), max(yT), max(yG), max(yC)))

        # print(pr5,pr6,pr7,pr8)

        if ((min(min(yA), min(yT), min(yG), min(yC))) >= mind) and ((max(max(yA), max(yT), max(yG), max(yC))) <= maxd):
            lite_crit_info = 'Lite criteria: good set'
        else:
            lite_crit_info = 'Lite criteria: bad set'

        if ((min(min(yA), min(yT), min(yG), min(yC))) >= mind0) and \
                ((max(max(yA), max(yT), max(yG), max(yC))) <= maxd0):
            strong_crit_info = 'Strong criteria: good set'
        else:
            strong_crit_info = 'Strong criteria: bad set'
        self.textBrowser_3.setText(err_set_analysis + '\n\n' + 'barcodes:\n' + str1 + '\nrate:\n' + str2 +
                                   '\n' + nucllen + '\n\nmin and max values:\n' + pr5 + pr6 + pr7 + pr8 + '\n\n' +
                                   strong_crit_info + '\n' + lite_crit_info)
        # print(err_set_analysis + '\n' + 'barcodes:\n' + str1 + '\nrate:\n' + str2 + '\n' + nucllen +
        # '\n\nmin and max values:\n' + pr5 + pr6 + pr7 + pr8 + '\n\n' + strong_crit_info + '\n' + lite_crit_info)

        plt.figure()
        # A
        plt.plot(x, yA, label="fraction A")
        # T
        plt.plot(x, yT, label="fraction T")
        # G
        plt.plot(x, yG, label="fraction G")
        # C
        plt.plot(x, yC, label="fraction C")
        plt.plot([1, NUCLEN], [mind, mind], color='k', linestyle='-', linewidth=3)
        plt.plot([1, NUCLEN], [maxd, maxd], color='k', linestyle='-', linewidth=3)

        plt.plot([1, NUCLEN], [mind0, mind0], color='k', linestyle='-', linewidth=2)
        plt.plot([1, NUCLEN], [maxd0, maxd0], color='k', linestyle='-', linewidth=2)

        # naming the x axis
        plt.xlabel('nucleotide position in barcode')
        # naming the y axis
        plt.ylabel(' nucleotide fraction ')
        # giving a title to my graph
        plt.title('NUCLEOTIDES FRACTION FOR BARCODE SET WITH RATE:' + str1 + ' rate:' + str2)

        # show a legend on the plot
        plt.legend()

        # function to show the plot
        plt.show()

    def addtoset(self):

        data_num = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
            '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34',
            '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
            '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66',
            '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82',
            '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98',
            '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112',
            '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126',
            '127', '128', '999',
            '1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D', '3A', '3B', '3C', '3D', '4A', '4B', '4C', '4D',
            '13A', '13B', '13C', '13D', '14A', '14B', '14C', '14D', '15A', '15B', '15C', '15D',
            '16A', '16B', '16C', '16D', '25A', '25B', '25C', '25D', '26A', '26B', '26C', '26D',
            '29A', '29B', '29C', '29D', '32A', '32B', '32C', '32D', '33A', '33B', '33C', '33D',
            '35A', '35B', '35C', '35D', '36A', '36B', '36C', '36D', '37A', '37B', '37C', '37D',
            '38A', '38B', '38C', '38D', '41A', '41B', '41C', '41D', '42A', '42B', '42C', '42D',
            '43A', '43B', '43C', '43D', '44A', '44B', '44C', '44D', '47A', '47B', '47C', '47D',
            '48A', '48B', '48C', '48D', '51A', '51B', '51C', '51D', '53A', '53B', '53C', '53D',
            '55A', '55B', '55C', '55D', '56A', '56B', '56C', '56D', '57A', '57B', '57C', '57D',
            '59A', '59B', '59C', '59D', '61A', '61B', '61C', '61D', '62A', '62B', '62C', '62D',
            '63A', '63B', '63C', '63D', '64A', '64B', '64C', '64D', '65A', '65B', '65C', '65D',
            '66A', '66B', '66C', '66D', '68A', '68B', '68C', '68D', '69A', '69B', '69C', '69D',
            '71A', '71B', '71C', '71D', '72A', '72B', '72C', '72D', '75A', '75B', '75C', '75D',
            '76A', '76B', '76C', '76D', '77A', '77B', '77C', '77D', '79A', '79B', '79C', '79D',
            '80A', '80B', '80C', '80D', '81A', '81B', '81C', '81D', '82A', '82B', '82C', '82D',
            '83A', '83B', '83C', '83D', '84A', '84B', '84C', '84D', '85A', '85B', '85C', '85D',
            '86A', '86B', '86C', '86D', '88A', '88B', '88C', '88D', '89A', '89B', '89C', '89D',
            '92A', '92B', '92C', '92D', '93A', '93B', '93C', '93D', '95A', '95B', '95C', '95D',
            '100A', '100B', '100C', '100D', '104A', '104B', '104C', '104D', '117A', '117B', '117C', '117D',
            '121A', '121B', '121C', '121D', '122A', '122B', '122C', '122D', '124A', '124B', '124C', '124D',
            '125A', '125B', '125C', '125D', '127A', '127B', '127C', '127D'
        ]
        # MGI barcode sequence
        data_seq = [
            'TAGGTCCGAT', 'GGACGGAATC', 'CTTACTGCCG', 'ACCTAATTGA', 'TTCGTATCCG', 'GGTAACGAGC', 'CAACGTATAA',
            'ACGTCGCGTT', 'TTCTGCTAGC', 'AGGAAGATAG', 'GCTCTTGCTT', 'CAAGCACGCA', 'CGGCAATCCG', 'ATCAGGATTC',
            'TCATTCCAGA', 'GATGCTGGAT', 'GTGAGTGATG', 'GAGTCAGCTG', 'TGTCTGCGAA', 'ATTGGTACAA', 'CGATTGTGGT',
            'ACAGACTTCC', 'TCCACACTCT', 'CACCACAAGC', 'TAGAGGACAA', 'CCTAGCGAAT', 'GTAGTCATCG', 'GCTGAGCTGT',
            'AACCTAGATA', 'TTGCCATCTC', 'AGATCTTGCG', 'CGCTATCGGC', 'GCAACGATGG', 'TAATCGTTCA', 'GTTCGCTCTA',
            'TCTCACACAT', 'CTGTTAGGAT', 'CGCAGACGCG', 'AAGGATCATC', 'AGCGTTGAGC', 'TTAGATGCAT', 'GTCCAGAGCT',
            'CACGTGATAG', 'CCACTAGTCC', 'TGGACTTGGC', 'GCTTGACAGG', 'AAGACCTCTA', 'AGTTGCCATA', 'ATGTACGCAG',
            'TTAATGAGAT', 'TGCGCCACTT', 'CATTAAGGCC', 'CCGCCTCAGA', 'AATCGGCTCG', 'GCCGGTTATC', 'GGAATATTGA',
            'ATTCAACGGA', 'AACTGTACTG', 'GTACCTCAAT', 'GACTTCTAAT', 'TGAAGCGTTG', 'CGTGCGATCC', 'TCGGAAGGCA',
            'CCGATGTCGC', 'ACTTAGAATG', 'TCCAAGCCTG', 'AGACGATGAT', 'CTCACAAGAC', 'CGTTCCTACT', 'GTGGTTGTGA',
            'GAAGGCCTGC', 'TAGCTTGCCA', 'GACAATGCTC', 'GCTAATCACA', 'AGTCCATAGG', 'CTATCGCCTA', 'ATCGTGGTCT',
            'TGGCTAATAC', 'CAGTGCAGAG', 'TCAGGCTGGT', 'ATACTCACGC', 'ATGCTCCGCG', 'TGTGAACTTG', 'GAGAGGTGCT',
            'TGCACTGTAA', 'GCCTAGGCAA', 'CCATCATAGC', 'CATGGTAATT', 'CACCATGTCT', 'ATATGTCTGG', 'AAGGAAGCGT',
            'TCAAGACGTC', 'CCGCTCAGTA', 'GGTGTGTACA', 'TTCACGTAAG', 'GGTTCCACAC', 'AGGTATTCTT', 'CGAATGCAAC',
            'TTCAACGGCG', 'CTCGGCGGAA', 'ACGGTAATGG', 'GATCCGACGT', 'TCACGATACA', 'GATTCTCTTC', 'ACAATTAATA',
            'ACCAGCATTA', 'CATCAGGCCC', 'CCTTCTCAAG', 'TAGCTCAACG', 'TAGTGCCCGT', 'GTTGAGAGAA', 'GCCTCATGGA',
            'GGTCAACCTA', 'CCAGAGTCAG', 'AACAGGCAGT', 'GCTCCATGAC', 'ATGTCTATCC', 'CTTGACAAGG', 'TGTTTCGTTA',
            'TGGAGTACCC', 'CCTTGATCAA', 'GGAAGTGGCA', 'AACATTCTAC', 'GACGCGAGTC', 'CTATAACACT', 'AGTCTCGTGT',
            'TCGGCCTATG', 'TTGCAGACGG', 'GCGTATGCGG',

            'TAGGTCCGAT', 'GTCCGAACTG', 'CGAACTTAGC', 'ACTTAGGTCA', 'GGACGGAATC', 'CCTACCTTGA', 'AAGTAAGGCT',
            'TTCGTTCCAG', 'CTTACTGCCG', 'AGGTAGCAAC', 'TCCGTCATTA', 'GAACGATGGT', 'ACCTAATTGA', 'TAAGTTGGCT',
            'GTTCGGCCAG', 'CGGACCAATC', 'CGGCAATCCG', 'ACCATTGAAC', 'TAATGGCTTA', 'GTTGCCAGGT', 'ATCAGGATTC',
            'TGATCCTGGA', 'GCTGAAGCCT', 'CAGCTTCAAG', 'TCATTCCAGA', 'GATGGAATCT', 'CTGCCTTGAG', 'AGCAAGGCTC',
            'GATGCTGGAT', 'CTGCAGCCTG', 'AGCATCAAGC', 'TCATGATTCA', 'TAGAGGACAA', 'GTCTCCTATT', 'CGAGAAGTGG',
            'ACTCTTCGCC', 'CCTAGCGAAT', 'AAGTCACTTG', 'TTCGATAGGC', 'GGACTGTCCA', 'AACCTAGATA', 'TTAAGTCTGT',
            'GGTTCGAGCG', 'CCGGACTCAC', 'CGCTATCGGC', 'ACAGTGACCA', 'TATCGCTAAT', 'GTGACAGTTG', 'GCAACGATGG',
            'CATTACTGCC', 'ATGGTAGCAA', 'TGCCGTCATT', 'GTTCGCTCTA', 'CGGACAGAGT', 'ACCTATCTCG', 'TAAGTGAGAC',
            'TCTCACACAT', 'GAGATATATG', 'CTCTGTGTGC', 'AGAGCGCGCA', 'CTGTTAGGAT', 'AGCGGTCCTG', 'TCACCGAAGC',
            'GATAACTTCA', 'CGCAGACGCG', 'ACATCTACAC', 'TATGAGTATA', 'GTGCTCGTGT', 'TTAGATGCAT', 'GGTCTGCATG',
            'CCGAGCATGC', 'AACTCATGCA', 'GTCCAGAGCT', 'CGAATCTCAG', 'ACTTGAGATC', 'TAGGCTCTGA', 'CACGTGATAG',
            'ATACGCTGTC', 'TGTACAGCGA', 'GCGTATCACT', 'CCACTAGTCC', 'AATAGTCGAA', 'TTGTCGACTT', 'GGCGACTAGG',
            'AAGACCTCTA', 'TTCTAAGAGT', 'GGAGTTCTCG', 'CCTCGGAGAC', 'AGTTGCCATA', 'TCGGCAATGT', 'GACCATTGCG',
            'CTAATGGCAC', 'TGCGCCACTT', 'GCACAATAGG', 'CATATTGTCC', 'ATGTGGCGAA', 'CCGCCTCAGA', 'AACAAGATCT',
            'TTATTCTGAG', 'GGTGGAGCTC', 'GCCGGTTATC', 'CAACCGGTGA', 'ATTAACCGCT', 'TGGTTAACAG', 'GGAATATTGA',
            'CCTTGTGGCT', 'AAGGCGCCAG', 'TTCCACAATC', 'ATTCAACGGA', 'TGGATTACCT', 'GCCTGGTAAG', 'CAAGCCGTTC',
            'GTACCTCAAT', 'CGTAAGATTG', 'ACGTTCTGGC', 'TACGGAGCCA', 'TGAAGCGTTG', 'GCTTCACGGC', 'CAGGATACCA',
            'ATCCTGTAAT', 'CGTGCGATCC', 'ACGCACTGAA', 'TACATAGCTT', 'GTATGTCAGG', 'TCGGAAGGCA', 'GACCTTCCAT',
            'CTAAGGAATG', 'AGTTCCTTGC', 'CCGATGTCGC', 'AACTGCGACA', 'TTAGCACTAT', 'GGTCATAGTG', 'ACTTAGAATG',
            'TAGGTCTTGC', 'GTCCGAGGCA', 'CGAACTCCAT', 'TCCAAGCCTG', 'GAATTCAAGC', 'CTTGGATTCA', 'AGGCCTGGAT',
            'CTCACAAGAC', 'AGATATTCTA', 'TCTGTGGAGT', 'GAGCGCCTCG', 'CGTTCCTACT', 'ACGGAAGTAG', 'TACCTTCGTC',
            'GTAAGGACGA', 'GAAGGCCTGC', 'CTTCCAAGCA', 'AGGAATTCAT', 'TCCTTGGATG', 'TAGCTTGCCA', 'GTCAGGCAAT',
            'CGATCCATTG', 'ACTGAATGGC', 'AGTCCATAGG', 'TCGAATGTCC', 'GACTTGCGAA', 'CTAGGCACTT', 'CTATCGCCTA',
            'AGTGACAAGT', 'TCGCTATTCG', 'GACAGTGGAC', 'ATCGTGGTCT', 'TGACGCCGAG', 'GCTACAACTC', 'CAGTATTAGA',
            'CAGTGCAGAG', 'ATCGCATCTC', 'TGACATGAGA', 'GCTATGCTCT', 'TCAGGCTGGT', 'GATCCAGCCG', 'CTGAATCAAC',
            'AGCTTGATTA', 'ATACTCACGC', 'TGTAGATACA', 'GCGTCTGTAT', 'CACGAGCGTG', 'ATGCTCCGCG', 'TGCAGAACAC',
            'GCATCTTATA', 'CATGAGGTGT', 'TGTGAACTTG', 'GCGCTTAGGC', 'CACAGGTCCA', 'ATATCCGAAT', 'GAGAGGTGCT',
            'CTCTCCGCAG', 'AGAGAACATC', 'TCTCTTATGA', 'TGCACTGTAA', 'GCATAGCGTT', 'CATGTCACGG', 'ATGCGATACC',
            'GCCTAGGCAA', 'CAAGTCCATT', 'ATTCGAATGG', 'TGGACTTGCC', 'CATGGTAATT', 'ATGCCGTTGG', 'TGCAACGGCC',
            'GCATTACCAA', 'CACCATGTCT', 'ATAATGCGAG', 'TGTTGCACTC', 'GCGGCATAGA', 'TCAAGACGTC', 'GATTCTACGA',
            'CTGGAGTACT', 'AGCCTCGTAG', 'CCGCTCAGTA', 'AACAGATCGT', 'TTATCTGACG', 'GGTGAGCTAC', 'TTCACGTAAG',
            'GGATACGTTC', 'CCTGTACGGA', 'AAGCGTACCT', 'CTCGGCGGAA', 'AGACCACCTT', 'TCTAATAAGG', 'GAGTTGTTCC',
            'GATTCTCTTC', 'CTGGAGAGGA', 'AGCCTCTCCT', 'TCAAGAGAAG', 'ATGTCTATCC', 'TGCGAGTGAA', 'GCACTCGCTT',
            'CATAGACAGG', 'CCTTGATCAA', 'AAGGCTGATT', 'TTCCAGCTGG', 'GGAATCAGCC', 'GGAAGTGGCA', 'CCTTCGCCAT',
            'AAGGACAATG', 'TTCCTATTGC', 'GACGCGAGTC', 'CTACACTCGA', 'AGTATAGACT', 'TCGTGTCTAG', 'CTATAACACT',
            'AGTGTTATAG', 'TCGCGGTGTC', 'GACACCGCGA', 'TCGGCCTATG', 'GACCAAGTGC', 'CTAATTCGCA', 'AGTTGGACAT',
        ]

        linenum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                   51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                   75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,
                   99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117,
                   118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]

        # CONST VALUES

        NUCLEN = 10  # lenght of barcode
        mind0 = 0.15
        maxd0 = 0.35
        minnoise0 = 0.17
        maxnoise0 = 0.54
        mind = 0.07
        maxd = 0.6
        minnoise = 0.07
        maxnoise = 0.67

        message = ''
        str1 = self.textEdit.toPlainText()  # names
        # print(str1, '1')
        names0 = [int(x.strip()) for x in str1.split(',')]
        # print(names0, '1')
        str2 = self.textEdit_4.toPlainText()  # rate+add
        # print(str2, '2')
        if ((str2) != 'all1') and (len(str2) != 0):
            rateadd = [float(x.strip()) for x in str2.split(',')]

        if (str2 == 'all1') or (len(str2) == 0):
            rateadd = ['all1']
        # print(rateadd, '2')
        # print(str1, names0, str2, rate2)

        self.textBrowser_3.setText('barcodes:\n' + str1 + '\nrate:\n' + str2)

        # names exist
        howmanyadd = int(self.textEdit_5.toPlainText())
        # print(strhowmanyandcriteria)
        # howmanyandcriteria = int(strhowmanyandcriteria)
        # howmanyandcriteria=[int(x.strip()) for x in strhowmanyandcriteria.split(',')]
        # howmanyadd = howmanyandcriteria[0]
        strfromwhich = self.textEdit_6.toPlainText()
        # print(strfromwhich)
        fromwhich = [int(x.strip()) for x in strfromwhich.split(',')]

        # criteria = howmanyandcriteria[1]  # 0 for strong, 1 for light
        if self.radioButton.isChecked() == True:
            criteria = "strong"
        else:
            criteria = "lite"
        # print(fromwhich)

        errrateadd = ''
        if (rateadd[0] != 'all1'):
            flagrateadd = 0
            if (len(rateadd) > (len(names0) + howmanyadd)):
                errrateadd = errrateadd + 'rate is too long, so I make equal rate'
                rateadd = [1] * (howmanyadd + len(names0))
            if (len(rateadd) < (len(names0) + howmanyadd)):
                errrateadd = errrateadd + 'rate is too short, so I make equal rate'
                rateadd = [1] * (howmanyadd + len(names0))

        # print(names0,rateadd,howmanyadd,fromwhich,criteria)

        exclude = []
        if (criteria == 'strong'):
            mincriteria = mind0
            maxcriteria = maxd0
        if (criteria == 'lite'):
            mincriteria = mind
            maxcriteria = maxd

        # print(mincriteria,maxcriteria)
        if (rateadd[0] == 'all1'):
            rateadd = [1] * (howmanyadd + len(names0))
        # rateadd = [1] * (howmanyadd + len(names0))

        linenum = list(data_num)
        set1 = set(linenum)
        set2 = set(names0 + [0])
        set_difference = set1.difference(set2)

        allwithoutnames = set(fromwhich).difference(set(exclude))
        allwithoutnames = list(allwithoutnames)

        # list(set_difference)

        def findsubsets(s, n):
            return list(itertools.combinations(s, n))

        ln = len(names0)
        nucllen = ''
        for i in range(0, ln):
            nucllen = nucllen + '\n' + str(data_num[data_num.index(str(names0[i]))]) + ' ' + str(
                data_seq[data_num.index(str(names0[i]))])
        # print('nucllen',nucllen)
        flagr = 0

        for m in findsubsets(allwithoutnames, howmanyadd):
            names0m = names0 + list(m)
            k = onesetwithrateanalisys0or1(names0m, rateadd, NUCLEN, data_seq, data_num, mincriteria, maxcriteria)

            # print(k)

            if k[0] == 1:
                # for i in range(0, len(names0m)):
                # print(data_num[names0m[i] - 1], end=' ')

                # print('k[1]',k[1])
                # plotnuclreit(names0m, k[1])
                tablereitfrac = k[1]
                # print(tablereitfrac)
                x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
                yA = []
                yT = []
                yG = []
                yC = []
                # print('yyyy',yA,yT,yG,yC)
                for i in range(0, NUCLEN):
                    yA.append(tablereitfrac[i][0])
                    yT.append(tablereitfrac[i][1])
                    yG.append(tablereitfrac[i][2])
                    yC.append(tablereitfrac[i][3])

                pr5 = "min values A T G C " + str(min(yA)) + ' ' + str(min(yT)) + ' ' + str(min(yG)) + ' ' + str(
                    min(yC))
                pr6 = "\nmin values A T G C " + str(max(yA)) + ' ' + str(max(yT)) + ' ' + str(max(yG)) + ' ' + str(
                    max(yC))
                pr7 = "\nmin " + str(min(min(yA), min(yT), min(yG), min(yC)))
                pr8 = "\nmax " + str(max(max(yA), max(yT), max(yG), max(yC)))

                err = errrateadd + '\nI find it!'
                self.textBrowser_3.setText(
                    'barcodes:\n' + str1 + '\nyour rate:\n' + str2 + '\n' + nucllen + '\nhow many add:' + str(
                        howmanyadd) + '\ncriteria:' + str(criteria) + '\n' + err + '\n\nresult:' + '\nto add: ' + str(
                        m) + '\nall set: ' + str(names0m) + '\n\nmin and max values:\n' + pr5 + pr6 + pr7 + pr8)

                # print('yyyy', yA, yT, yG, yC)
                plt.figure()
                # A
                plt.plot(x, yA, label="fraction A")
                # T
                plt.plot(x, yT, label="fraction T")
                # G
                plt.plot(x, yG, label="fraction G")
                # C
                plt.plot(x, yC, label="fraction C")

                plt.plot([1, NUCLEN], [mind, mind], color='k', linestyle='-', linewidth=3)
                plt.plot([1, NUCLEN], [maxd, maxd], color='k', linestyle='-', linewidth=3)

                plt.plot([1, NUCLEN], [mind0, mind0], color='k', linestyle='-', linewidth=2)
                plt.plot([1, NUCLEN], [maxd0, maxd0], color='k', linestyle='-', linewidth=2)

                # naming the x axis
                plt.xlabel('nucleotide position in barcode')
                # naming the y axis
                plt.ylabel(' nucleotide fraction ')
                # giving a title to my graph
                plt.title('NUCLEOTIDES FRACTION FOR BARCODE SET WITH RATE:' + str(names0m) + ' rate:' + str(rateadd))

                # show a legend on the plot
                plt.legend()

                # function to show the plot
                plt.show()

                # print('ola!!!',m)
                # print('\t')
                # print('pr5',pr5,pr6,pr7,pr8)
                flagr = 1
                break
        1

        if (flagr == 0):
            err = errrateadd + '\nno good set exist'
            self.textBrowser_3.setText(
                'barcodes:\n' + str1 + '\nyour rate:\n' + str2 + '\n' + nucllen + '\nhow many add:' + str(
                    howmanyadd) + '\ncriteria:' + str(criteria) + '\n' + err)

        # print(err)
        # self.textBrowser_3.append('\nall set'+'\n'+str(names0m)+'\nadd barcodes:\n' + str(list(m)))


##########################
##########################
##########################

# Freguence analisys of set's nucleotides' fractions without rate

def onesetanalisys(names, nuclen, data_seq, data_num, mind, maxd):
    namesindex = []
    tableraiting = [[0 for i in range(4)] for j in range(nuclen)]
    ln = len(names)
    for i in range(0, ln):
        namesindex.append(data_num.index(str(names[i])))
    flag = 1
    set = ()
    for j in range(0, nuclen):
        reiting = [0, 0, 0, 0]  # A T G C
        for i in range(0, ln):
            if data_seq[namesindex[i]][j] == 'A': reiting[0] += 1
            if data_seq[namesindex[i]][j] == 'T': reiting[1] += 1
            if data_seq[namesindex[i]][j] == 'G': reiting[2] += 1
            if data_seq[namesindex[i]][j] == 'C': reiting[3] += 1
        tableraiting[j][0] = round(reiting[0] / ln, 3)
        tableraiting[j][1] = round(reiting[1] / ln, 3)
        tableraiting[j][2] = round(reiting[2] / ln, 3)
        tableraiting[j][3] = round(reiting[3] / ln, 3)
        if not ((reiting[0] >= (mind * ln)) and (reiting[0] <= (maxd * ln)) and (reiting[1] >= (mind * ln)) and (
                reiting[1] <= (maxd * ln)) and (reiting[2] >= (mind * ln)) and (reiting[2] <= (maxd * ln)) and (
                        reiting[3] >= (mind * ln)) and (reiting[3] <= (maxd * ln))):
            flag = 0
    if (flag == 1):
        result = 'good set'
    else:
        result = 'bad set, try another one'
    return result, tableraiting


# Freguence analisys of set's nucleotides' fractions with rate
def onesetwithrateanalisys(names, rate, nuclen, data_seq, data_num, mind, maxd):
    namesindex = []
    tableraiting = [[0 for i in range(4)] for j in range(nuclen)]
    ratesum = sum(rate)
    ln = len(names)
    for i in range(0, ln):
        namesindex.append(data_num.index(str(names[i])))
    flag = 1
    for j in range(0, nuclen):
        reiting = [0, 0, 0, 0]  # A T G C
        for i in range(0, ln):
            if data_seq[namesindex[i]][j] == 'A': reiting[0] += rate[i]
            if data_seq[namesindex[i]][j] == 'T': reiting[1] += rate[i]
            if data_seq[namesindex[i]][j] == 'G': reiting[2] += rate[i]
            if data_seq[namesindex[i]][j] == 'C': reiting[3] += rate[i]
        tableraiting[j][0] = round(reiting[0] / ratesum, 3)
        tableraiting[j][1] = round(reiting[1] / ratesum, 3)
        tableraiting[j][2] = round(reiting[2] / ratesum, 3)
        tableraiting[j][3] = round(reiting[3] / ratesum, 3)
        if not ((reiting[0] >= (mind * ratesum)) and (reiting[0] <= (maxd * ratesum)) and (
                reiting[1] >= (mind * ratesum)) and (reiting[1] <= (maxd * ratesum)) and (
                        reiting[2] >= (mind * ratesum)) and (reiting[2] <= (maxd * ratesum)) and (
                        reiting[3] >= (mind * ratesum)) and (reiting[3] <= (maxd * ratesum))):
            flag = 0
    if flag == 1:
        result = 'good set'
    else:
        result = 'bad set, try another one'

    return result, tableraiting


def onesetwithrateanalisys0or1(names, rate, nuclen, data_seq, data_num, mind, maxd):
    namesindex = []
    tableraiting = [[0 for i in range(4)] for j in range(nuclen)]
    ratesum = sum(rate)
    ln = len(names)
    for i in range(0, ln):
        namesindex.append(data_num.index(str(names[i])))
    flag = 1
    set = ()
    for j in range(0, nuclen):
        reiting = [0, 0, 0, 0]  # A T G C
        for i in range(0, ln):
            if data_seq[namesindex[i]][j] == 'A': reiting[0] += rate[i]
            if data_seq[namesindex[i]][j] == 'T': reiting[1] += rate[i]
            if data_seq[namesindex[i]][j] == 'G': reiting[2] += rate[i]
            if data_seq[namesindex[i]][j] == 'C': reiting[3] += rate[i]
        tableraiting[j][0] = round(reiting[0] / ratesum, 3)
        tableraiting[j][1] = round(reiting[1] / ratesum, 3)
        tableraiting[j][2] = round(reiting[2] / ratesum, 3)
        tableraiting[j][3] = round(reiting[3] / ratesum, 3)
        if not ((reiting[0] >= (mind * ratesum)) and (reiting[0] <= (maxd * ratesum)) and (
                reiting[1] >= (mind * ratesum)) and (reiting[1] <= (maxd * ratesum)) and (
                        reiting[2] >= (mind * ratesum)) and (reiting[2] <= (maxd * ratesum)) and (
                        reiting[3] >= (mind * ratesum)) and (reiting[3] <= (maxd * ratesum))):
            flag = 0
    return (int(flag), tableraiting)


# Freguence analisys of set's noise level without rate
def noiselevel(names, nuclen, data_seq, data_num, minnoise, maxnoise):
    namesindex = []
    noiselevel = [[0 for i in range(4)] for j in range(nuclen)]
    ln = len(names)
    for i in range(0, ln):
        namesindex.append(data_num.index(str(names[i])))
    flag = 1
    for j in range(0, nuclen):
        reiting = [0, 0, 0, 0]  # A T G C
        for i in range(0, ln):
            if data_seq[namesindex[i]][j] == 'A':
                reiting[0] += 1
            if data_seq[namesindex[i]][j] == 'T':
                reiting[1] += 1
            if data_seq[namesindex[i]][j] == 'G':
                reiting[2] += 1
            if data_seq[namesindex[i]][j] == 'C':
                reiting[3] += 1
        noiselevel[j][0] = round(reiting[0] / (ln - reiting[0]), 3)
        noiselevel[j][1] = round(reiting[1] / (ln - reiting[1]), 3)
        noiselevel[j][2] = round(reiting[2] / (ln - reiting[2]), 3)
        noiselevel[j][3] = round(reiting[3] / (ln - reiting[3]), 3)
        if not ((noiselevel[j][0] >= minnoise) and (noiselevel[j][0] <= maxnoise) and
                (noiselevel[j][1] >= minnoise) and (noiselevel[j][1] <= maxnoise) and
                (reiting[2] >= minnoise) and (noiselevel[j][2] <= maxnoise) and (noiselevel[j][3] >= (minnoise)) and
                (noiselevel[j][3] <= maxnoise)):
            flag = 0
    if flag == 1:
        result = 'good set noise'
    else:
        result = 'bad set noise, try another one'
    return result, noiselevel


def main():
    # CONST VALUES

    NUCLEN = 10  # lenght of barcode
    mind0 = 0.15
    maxd0 = 0.35
    minnoise0 = 0.17
    maxnoise0 = 0.54
    mind = 0.07
    maxd = 0.6
    minnoise = 0.07
    maxnoise = 0.67
    # print('values NUCLEN',NUCLEN)
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

    # print('main is ok!')


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
