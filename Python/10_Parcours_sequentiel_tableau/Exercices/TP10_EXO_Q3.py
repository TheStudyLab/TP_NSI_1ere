Liste = [1, 4, 8, 11, 33, 32, 45, 48, 56, 72, 86]


# a- With a for loop
def nombres_pairs_1(tab):
  """Counts even numbers in a list using a for loop."""
  count = 0
  for number in tab:
    if number % 2 == 0:
      count += 1
  return count


# b- With a while loop
def nombres_pairs_2(tab):
  """Counts even numbers in a list using a while loop."""
  count = 0
  i = 0
  while i < len(tab):
    if tab[i] % 2 == 0:
      count += 1
    i += 1
  return count


# Example usage
print(nombres_pairs_1(Liste))  # 7
print(nombres_pairs_2(Liste))  # 7
