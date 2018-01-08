# local forward BLAST starts here

__author__ = 'Won Woo Song'
__version__ = '1.0'

import os

class LocalForwardBLAST:

    def __init__(self):
        eval = '10e-5'
        outputName = "Output/test"
        topForward = '5'
        # os.system('blastn')

        # forward BLAST TEST
        sourceOrganism = 'Cyanidioschyzon_Merolae'
        query = 'Q85FV4.1'
        subject = 'nr'

        remote_database = 'makeblastdb -in DataBase/' + sourceOrganism + '.txt -parse_seqids -dbtype prot -out DataBase/' + sourceOrganism
        # print (remote_database)
        os.system(remote_database)

        remote_databaseCmd = 'blastdbcmd -db DataBase/' + sourceOrganism + ' -dbtype prot -entry ' + query + ' -out DataBase/' + query + '.txt'
        os.system(remote_databaseCmd)

        remote_test = "makeblastdb -in DataBase/" + query + ".txt -out Database/" + query + " -parse_seqids -dbtype prot"
        os.system(remote_test)

        forwardBlastTest = 'blastp -query DataBase/' + query + '.txt -db DataBase/' + subject + ' -evalue ' + eval + ' -out ' + outputName + '_Full_Version.txt'
        os.system(forwardBlastTest)

        forwardTopHits = "blastp -query DataBase/" + query + ".txt -db DataBase/" + subject + " -evalue " + eval + " -max_target_seqs " + topForward + " -outfmt \"6 sacc \" -out " + outputName + '_TopHits.txt'
        os.system(forwardTopHits)