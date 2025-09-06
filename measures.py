
DATA = None
N = None
MEAN = None
MEDIAN = None
MODE = None
DEVIATION = None
LQK = None
IQR = None
OD = None
OUT = None
OUT_EX = None


# Read, parse and sort data
def getData():

    x = input("Entry = \n\n");
    DATA = x.split(" ");

    try:
        DATA = [int(i) for i in DATA];
    except ValueError:
        DATA = [float(i) for i in DATA];

    DATA.sort();
    return (DATA);

def printData():

    print(f"Data = {DATA}\n");
    print (f"N = {N}");
    print (f"Min = {min(DATA)}");
    print (f"Max = {max(DATA)}");
    print (f"Mean = {MEAN}");
    print (f"Median = {MEDIAN}");
    print (f"Mode = {MODE}");
    print (f"Standard Deviation = {DEVIATION}");
    print (f"LQK = {LQK}");
    print (f"IQR = {IQR}");
    print (f"Outlier detection points = {OD}");
    print (f"Outliers = {OUT}");
    print (f"Extreme Outliers = {OUT_EX}");

if (__name__ == "__main__"): 

    DATA = getData();
    N = len(DATA);

    # Get mean, median, mode, standard deviation and quartiles

    N = len(DATA);
    MEAN = sum(DATA) / N;
    MEDIAN = DATA[int(N/2)];
    MODE = [];
    DEVIATION = 0;
    LQK = [];

    for i in DATA:
        c = DATA.count(i); 
        if (c > 1):
            if (MODE.count((c, i)) == 0):
                MODE.append((c, i));
        DEVIATION += (i-MEAN)**2;

    for i in range(1, 4):
        tmp = int((i*(N+1)) / 4.0);
        LQK.append(DATA[tmp]);

    MODE.sort(reverse=True);
    DEVIATION = (DEVIATION/(N-1))**.5;

    # Get interquartile range
    IQR = LQK[2] - LQK[0];

    # Get outlier detection relevant points
    OD = [];
    toggle = -1;
    for i in (LQK[0], LQK[2]):
            OD.append(i + (1.5*IQR) * toggle);
            OD.append(i + (3*IQR) * toggle);
            toggle = -toggle;

    # Detect outliers and extreme outliers
    OUT = [];
    OUT_EX = [];
    for i in DATA:
        if ((i < OD[0]) or (i > OD[2]) ):
            if ((i < OD[1]) or (i > OD[3]) ):
                OUT_EX.append(i);
            else:
                OUT.append(i);

    printData();
