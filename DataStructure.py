# %%
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask


# %%
class ChampionNetwork:
    """
    A network analysis class for examining League of Legends champion data.
    This class builds a graph of champion interactions based on game data.
    """

    def __init__(self, game_data):
        """
        Initializes the ChampionNetwork with provided game data.
        :param game_data: A DataFrame containing League of Legends champion game data.
        """
        self.game_data = game_data
        self.graph = nx.Graph()
        self._build_graph()

    def _build_graph(self):
        """
        Private method to build a graph from the game data.
        Champions are nodes, and edges are weighted by co-occurrence in games.
        """
        for i in range(1, 6):
            self.game_data.apply(lambda row: self._add_edges(row, i), axis=1)
        pair_counts = self._get_pair_counts()
        for (u, v), count in pair_counts.items():
            self.graph.add_edge(u, v, weight=count)

    def _add_edges(self, row, i):
        """
        Adds edges between champion nodes within the same team based on their appearance together in matches.
        :param row: A row from the DataFrame of game data.
        :param i: Index for champion in the team roster.
        """
        for j in range(i + 1, 6):
            self.graph.add_edge(row[f"t1_champ{i}id"], row[f"t1_champ{j}id"])
            self.graph.add_edge(row[f"t2_champ{i}id"], row[f"t2_champ{j}id"])

    def _get_pair_counts(self):
        """
        Aggregates and counts all pairs of champions appearing together in matches.
        :return: A Series of pair counts.
        """
        pairs = pd.concat(
            [
                self.game_data.apply(
                    lambda row: tuple(
                        sorted((row[f"t1_champ{i}id"], row[f"t1_champ{j}id"]))
                    ),
                    axis=1,
                )
                for i in range(1, 6)
                for j in range(i + 1, 6)
            ]
            + [
                self.game_data.apply(
                    lambda row: tuple(
                        sorted((row[f"t2_champ{i}id"], row[f"t2_champ{j}id"]))
                    ),
                    axis=1,
                )
                for i in range(1, 6)
                for j in range(i + 1, 6)
            ]
        )
        return pairs.value_counts()

    def query_champion(self, champ_id):
        """
        Retrieves and displays connections for a given champion.
        :param champ_id: The champion ID to query in the graph.
        :return: A dictionary of edges and weights if the champion exists, else a not found message.
        """
        if champ_id in self.graph:
            return self.graph[champ_id]
        else:
            return "Champion not found."

    def common_pairs(self):
        """
        Returns the top 10 most frequently appearing champion pairs.
        :return: A list of tuples (pairs) with their weights.
        """
        edges = sorted(
            self.graph.edges(data=True), key=lambda x: x[2]["weight"], reverse=True
        )
        return edges[:10]

    def champion_pairs(self, champ_id):
        """
        Finds and lists pairs involving a specific champion, sorted by weight.
        :param champ_id: The champion ID to find pairs for.
        :return: A list of tuples (champion pairs and their interaction weight).
        """
        if champ_id in self.graph:
            connected = sorted(
                self.graph[champ_id],
                key=lambda x: self.graph[champ_id][x]["weight"],
                reverse=True,
            )
            return [
                (champion, self.graph[champ_id][champion]["weight"])
                for champion in connected
            ]
        else:
            return "Champion not found."

    def find_isolated_champions(self):
        """
        Identifies champions that have no connections to other champions.
        :return: A list of isolated champion IDs.
        """
        isolated = [
            node for node, degree in dict(self.graph.degree()).items() if degree == 0
        ]
        return isolated

    def most_influential_champions(self):
        """
        Identifies the most influential champions in the network based on degree centrality.
        """
        centrality = nx.degree_centrality(self.graph)
        # Returns a sorted list of nodes based on their centrality score
        return sorted(centrality.items(), key=lambda item: item[1], reverse=True)


    def plot_network(self):
        """
        Visualizes the champion network graph.
        """
        pos = nx.spring_layout(self.graph)
        weights = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=weights)
        plt.show()


# %%
