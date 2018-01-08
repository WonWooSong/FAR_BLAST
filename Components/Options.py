# options

__author__ = 'Won Woo Song'
__version__ = '1.0'

class Options:
    def __init__(self, evalue = '', topForwardHits= '', topFarHits= '', coreNumber= ''):
        self.evalue = evalue
        self.topForwardHits = topForwardHits
        self.topFarHits = topFarHits
        self.coreNumber = coreNumber

    # sets evalue of the program
    def setEvalue(self, evalue):
        self.evalue = evalue

    # sets top hits for forward BLAST
    def setTopForwardHits(self, topForwardHits):
        self.topForwardHits = topForwardHits

    # sets top hits for FAR BLAST
    def setTopFarHits(self, topFarHits):
        self.topFarHits = topFarHits

    # sets number of cores/threads for the program
    def setCoreNumber(self, coreNumber):
        self.coreNumber = coreNumber

    # gets evalue for the program
    def getEvalue(self):
        return self.evalue

    # gets top hits for forward BLAST
    def getTopForwardHits(self):
        return self.topForwardHits

    # gets top hits for FAR BLAST
    def getTopFarHits(self):
        return self.topFarHits

    # gets number of cores/threads for the program
    def getCoreNumber(self):
        return self.coreNumber
