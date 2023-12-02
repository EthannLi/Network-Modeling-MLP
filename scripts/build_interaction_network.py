from argparse import ArgumentParser
from pathlib import Path
import pandas as pd 
import json

def getPath(fname):
    fp = Path(__file__).resolve().parent.parent / fname
    return fp

def parser():
    parser = ArgumentParser()
    parser.add_argument('-i','--input', type=str, required=True,help='Input file - /path/to/script_input.csv')
    parser.add_argument('-o','--output', type=str, required=True,help='Output file - /path/to/interaction_network.json')
    return parser.parse_args()

def build_network(df):
    Network = {}
    for i in range(len(df) - 1):
        if df['title'][i] != df['title'][i+1]:
            continue
        p1 = df['pony'][i]
        p2 = df['pony'][i+1]
        if p1 == p2:
            continue
        else:
            if p1 not in Network:
                Network[p1] = {}
            if p2 not in Network:
                Network[p2] = {}
            if p2 not in Network[p1]:
                Network[p1][p2] = 0
            if p1 not in Network[p2]:
                Network[p2][p1] = 0
            Network[p1][p2] += 1
            Network[p2][p1] += 1
    return Network
def fix_network(Network):
    pass

def main():
    args = parser()
    df = pd.read_csv(getPath(args.input))
    #df = pd.read_csv('/home/nemo/repos/ethann-github/Network-Modeling-MLP/data/output/script_output.csv')
    Network = build_network(df)
    # Network = fix_network(Network)
    with open(getPath(args.output), 'w') as fp:
        json.dump(Network, fp,indent=4)
    

if __name__ == "__main__":
    main()
