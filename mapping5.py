def rep(text, mapping):
    return ''.join([mapping.get(char, char) for char in text])

mapping = {
    'R': 'H',
    'T': 'T',
    'E': 'E',
    'I': 'A',
    'B': 'B',
    'Y': 'Y',
    'S': 'N',
    'L': 'D',
    'N': 'S',
    'F': 'F',
    'A': 'O',
    'P': 'M',
    'H': 'I',
    'O': 'R',
    'G': 'U',
    'M': 'G',
    'U': 'P',
    'D': 'L',
    'Z': 'J',
}

cipher_text = """TRE RIOOY UATTEO NEOHEN, WOHTTES BY BOHTHNR IGTRAO Z.K. OAWDHSM, HN ASE AF TRE PANT UAUGDIO ISL HSFDGESTHID FISTINY NIMIN AF PALEOS DHTEOITGOE. NUISSHSM NEVES BAAKN, TRE NEOHEN FADDAWN TRE DHFE AF I YAGSM BAY, RIOOY UATTEO, WRA LHNCAVEON AS RHN QQTR BHOTRLIY TRIT RE HN I WHXIOL. RE HN HSVHTEL TA ITTESL RAMWIOTN NCRAAD AF WHTCRCOIFT ISL WHXIOLOY, WREOE RE DEIOSN IBAGT RHN PIMHCID REOHTIME, LEVEDAUN CDANE FOHESLNRHUN, ISL CASFOASTN TRE LIOK FAOCEN TRIT TROEITES TRE WHXIOLHSM WAODL.

TRE CESTOID UDAT OEVADVEN IOAGSL RIOOYEN ASMAHSM BITTDE WHTR DAOL VADLEPAOT, I LIOK WHXIOL HSTEST AS CASJGEOHSM BATR TRE PIMHCID ISL SASCPIMHCID WAODLN. IN RIOOY MOAWN ADLEO, RE DEIOSN PAOE IBAGT RHN AWS PYNTEOHAGN UINT, RHN CASSECTHAS TA VADLEPAOT, ISL TRE UOAURECY TRIT THEN TREHO FITEN TAMETREO. TROAGMRAGT TRE NEOHEN, TREPEN AF FOHESLNRHU, DAYIDTY, BOIVEOY, ISL TRE UAWEO AF DAVE IOE EAUDAOEL, WHTR I OHCR WAODL FHDDEL WHTR PIMHCID COEITGOEN, NUEDDN, ISL LEEU PYTRADAMY.

TRE BAAKN, NTIOTHSM WHTR RIOOY UATTEO ISL TRE URHDANAUREOEN NTASE NQOOTM ISL CASCDGLHSM WHTR HRIOOY UATTEO ISL TRE LEITRDY RIDDAWN NYJJTM, RIVE NADL AVEO VJJ PHDDHAS CAUHEN WAODLWHLE, BEES TOISNDITEL HSTA PAOE TRIS RJ DISMGIMEN, ISL ILIUTEL HSTA I NGCCENNFGD FHDP NEOHEN. TRE NEOHEN HN KSAWS SAT ASDY FAO HTN ESCRISTHSM WAODLCBGHDLHSM BGT IDNA FAO ILLOENNHSM LIOKEO, CAPUDEA TREPEN NGCR IN PAOTIDHTY, UOEZGLHCE, ISL TRE IBGNE AF UAWEO. TRE RIOOY UATTEO NEOHEN RIN DEFT IS HSLEDHBDE PIOK AS UAUGDIO CGDTGOE, FANTEOHSM I MDABID FIS BINE, HSNUHOHSM CAGSTDENN NUHSCAFFN, ISL CEPESTHSM HTN UDICE IN I DHTEOIOY URESAPESAS.
"""

dt = rep(cipher_text, mapping)

print(dt)