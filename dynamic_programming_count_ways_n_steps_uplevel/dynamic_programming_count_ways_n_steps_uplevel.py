
# Complete the countWaysToClimb function below.
def countWaysToClimb(steps, n):

   if n == 1 or n == 2: return n

   table = [n + 1]

   for i in range(2, n):
        table[i] = table[i - 1] + table[i - 2]

   return table[n]




print(countWaysToClimb([2, 3], 7))
