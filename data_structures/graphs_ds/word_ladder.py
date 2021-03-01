from data_structures.graphs_ds.graph_adt import Graph

word_file = "data_structures/graphs_ds/words_file"


def word_ladder(words_file):
    """The program gradually morphs a word gradually to a form a new word.
    Using the graph ADT, we are able to keep track of how and where each
    metamorphosis changes and its continued path. Using Breadth First Search
    algorithm"""
    word_dict = {}
    graph = Graph()
    w_file = open(words_file, 'r')
    # Create buckets of words that differ by one letter
    for line in w_file:
        word = line[:1]
        for i in range(len(word)):
            bucket = f"{word[:i]}_{word[i + 1:]}"
            if bucket in word_dict:
                word_dict[bucket].append(word)
            else:
                word_dict[bucket] = [word]

    # Add vertices and edges for words in the same bucket
    for bucket in word_dict.keys():
        for word1 in word_dict[bucket]:
            for word2 in word_dict[bucket]:
                if word1 is not word2:
                    word_dict.add_edge(word1, word2)

    return graph
