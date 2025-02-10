def getP2CLN(P1: bool, P2NegativePath, P2PositivePath):
    return P1 and (P2PositivePath or P2NegativePath)

def getP3CLN(P2CLN: bool, P2PositivePath: bool, P2NegativePath: bool, P3PositivePath: bool, P3NegativePath: bool):
    P3CLNPositivePath = P2PositivePath and P3PositivePath
    P3CLNNegativePath = P2NegativePath and P3NegativePath
    return P2CLN and (P3CLNPositivePath or P3CLNNegativePath)

def getP1t3CLN(valid: bool, P2NegativePath: bool, P3NegativePath: bool):
    return P2NegativePath and P3NegativePath and valid

def cleanDomain(P1: bool, P2: int, P3: int) -> object:
    P2PositivePath = P2 >= 1 and P2 <= 7
    P2NegativePath = P2 == 0 or P2 == 99
    P3PositivePath = P3 > 9 and P3 < 961
    P3NegativePath = P3 == 0

    P2CLN = getP2CLN(P1, P2NegativePath, P3NegativePath)
    P3CLN = getP3CLN(P2CLN, P2PositivePath, P2NegativePath,
                     P3PositivePath, P3NegativePath)

    P1t3CLN = getP1t3CLN(not P1, P2NegativePath, P3NegativePath)

    return {P1t3CLN, P3CLN, P2CLN}

def getP16CLN(P16: int) -> object:
    P16CLN = P16<1441
    return { P16CLN }