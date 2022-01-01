def numberOfPaths(matrix):

    # Write your code here

    m = len(matrix)
    n = len(matrix[0])

    table = [[0 for x in range(m)] for y in range(n)]

    for i in range(0, m - 1):
        table[i][0] = 1

    for j in range(0, n - 1):
        table[0][j] = 1

    for row in range(1, m - 1):
        for col in range( 1, n - 1):
            table[row][col] = table[row - 1][col] + table[row][col - 1]

    results = len(table)

    return results


print(numberOfPaths([3,4]))
        
