from singleLinkage import single_cluster

if __name__ == '__main__':
    inputDemo = [
        [1, 2, 3],
        [2, 3, 5],
        [4, 7, 9, 10],
        [6, 8],
        [7, 11]
    ]

    result = single_cluster(inputDemo)
    print(result)
