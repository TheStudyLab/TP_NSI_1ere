def echange(tab, i, j):
  """Swaps elements at indices i and j in the list tab."""
  temp = tab[i]
  tab[i] = tab[j]
  tab[j] = temp


def miroir(tab):
  """Reverses the list tab in place using the echange function."""
  n = len(tab)
  for i in range(n // 2):
    echange(tab, i, n - 1 - i)


# Example usage
my_list = [1, 2, 3, 4, 5]
miroir(my_list)
print(my_list)  # [5, 4, 3, 2, 1]
