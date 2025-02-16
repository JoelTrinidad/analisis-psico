from operator import itemgetter


def getTPA_MET(
    P1: bool,
    P2: int,
    P3: int,
    P4: bool,
    P5: int,
    P6: int,
    P7: bool,
    P8: int,
    P9: int,
    P10: bool,
    P11: int,
    P12: int,
    P13: bool,
    P14: int,
    P15: int,
):
    vigWorkMET = (P2 * P3 * 8)
    modWorkMET = (P5 * P6 * 4)
    travelMET = (P8 * P9 * 4)
    vigRecreationMET = (P11 * P12 * 8)
    modRecreationMET = (P14 * P15 * 4)

    return vigWorkMET + modWorkMET + travelMET, vigRecreationMET + modRecreationMET


def getMeanMedianIndicators(
    P1: bool,
    P2: int,
    P3: int,
    P4: bool,
    P5: int,
    P6: int,
    P7: bool,
    P8: int,
    P9: int,
    P10: bool,
    P11: int,
    P12: int,
    P13: bool,
    P14: int,
    P15: int,
):
    P1t3 = P2*P3
    P4t6 = P5*P6
    P7t9 = P8*P9
    P10t12 = P11*P12
    P13t15 = P14*P15

    Ptotalday = (P1t3 + P4t6 + P7t9 + P10t12 + P13t15)/7
    Pworkday = (P1t3 + P4t6)/7
    Ptravelday = P7t9/7
    Precday = (P10t12 + P13t15)/7

    return {
        Ptotalday,
        Pworkday,
        Ptravelday,
        Precday,
    }


def getNoDoing(P1: bool, P4: bool, P7: bool, P10: bool, P13: bool) -> object:
    didWork = "Did work activity" if P1 or P4 else "Did no work activity"

    didTransport = "Did transport activity" if P7 else "Did no transport activity"

    didRecreation = "Did recreation activity" if P10 or P13 else "Did no recreation activity"
    return {
        didWork,
        didTransport,
        didRecreation,
    }


def categoricalIndicatorsEquations(
    P1: bool,
    P2: int,
    P3: int,
    P4: bool,
    P5: int,
    P6: int,
    P7: bool,
    P8: int,
    P9: int,
    P10: bool,
    P11: int,
    P12: int,
    P13: bool,
    P14: int,
    P15: int,
):
    TPA_MET = getTPA_MET(P1, P2, P3, P4, P5, P6, P7, P8,
                         P9, P10, P11, P12, P13, P14, P15)

    TPA_MET_Result = "Does not meet recommendations" if TPA_MET < 600 else "Meets recommendations"

    Ptotalday, Pworkday, Ptravelday, Precday = itemgetter(getMeanMedianIndicators(
        P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15))
    return {
        TPA_MET,
        TPA_MET_Result,
        Ptotalday,
        Pworkday,
        Ptravelday,
        Precday,
    }
