# MLP Network Modeling

## Description

This project analyzes the interactions between characters in the My Little Pony (MLP) series. It builds a network of interactions, where nodes represent characters and edges represent interactions between characters. The weight of an edge corresponds to the number of interactions between two characters.

## Installation

1. Clone this repository.
2. Install the required Python libraries: `networkx`, `pandas`, and `json`.

## Usage

1. Run the `build_interaction_network.py` script with the `-i` flag to specify the input CSV file and the `-o` flag to specify the output JSON file. This script will build the interaction network and save it as a JSON file.
2. Run the `analyze_network.py` script with the `-i` flag to specify the input JSON file and the `-o` flag to specify the output JSON file. This script will calculate the degree centrality, weighted degree centrality, closeness centrality, and betweenness centrality for each character and save the results as a JSON file.

## Contributing

Please submit a pull request or open an issue if you would like to contribute to this project.

