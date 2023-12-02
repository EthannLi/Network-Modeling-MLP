import json
import networkx as nx
from argparse import ArgumentParser
from pathlib import Path

def getPath(fname):
    fp = Path(__file__).resolve().parent.parent / fname
    return fp

def parser():
    parser = ArgumentParser()
    parser.add_argument('-i','--input', type=str, required=True,help='Input file - /path/to/interaction_network.json')
    parser.add_argument('-o','--output', type=str, required=True,help='Output file - /path/to/interaction_network.gexf')
    return parser.parse_args()

def main():
    args = parser()
    with open(args.input, 'r') as f:
        data = json.load(f)
    G = nx.Graph(data)
    degree = sorted(G.degree, key=lambda x: x[1], reverse=True)[:3]
    weighted_degree = sorted(G.degree(weight='weight'), key=lambda x: x[1], reverse=True)[:3]
    closeness = sorted(nx.closeness_centrality(G).items(), key=lambda x: x[1], reverse=True)[:3]
    betweenness = sorted(nx.betweenness_centrality(G).items(), key=lambda x: x[1], reverse=True)[:3]
    result = {
        "degree": [node[0] for node in degree],
        "weighted_degree": [node[0] for node in weighted_degree],
        "closeness": [node[0] for node in closeness],
        "betweenness": [node[0] for node in betweenness]
    }
    with open(args.output, 'w') as f:
        json.dump(result, f,indent=4)

if __name__ == "__main__":
    main()