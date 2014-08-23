import os

#"rdsamp -r gaitndd/als1 -c -H -f 0 -t 300 -v -pd >samples.csv"

INPUT_DATA = {
        "als": 13,
        "control": 16,
        "hunt": 20,
        "park": 15
}

DATA_DIR = "gaitndd/"
OUT_DIR  = "output/"

def rdsamp_cmd(inp):
    inp_file = DATA_DIR + inp
    out_file = OUT_DIR + inp + ".csv"
    return "rdsamp -r " + inp_file + " -c -H -f 0 -t 300 -v -pd > " + out_file

def data_input():
    for file_prefix in INPUT_DATA:
        max_file = INPUT_DATA[file_prefix]
        for i in range(1, max_file+1):
            yield (file_prefix + str(i))

def process_data():
    for inp in data_input():
        cmd = rdsamp_cmd(inp)
        print "Executing: ", cmd
        os.system(cmd)

process_data()
