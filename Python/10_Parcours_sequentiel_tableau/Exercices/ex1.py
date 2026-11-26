L = [12, 15, 7, 12, 18, "chien", "chat", "fleurs", "tomates", "a", 0]


def contains_element(element):
  """Checks if an element is present in the global list L using a while loop."""
  i = 0
  while i < len(L):
    if L[i] == element:
      return True
    i += 1
  return False


# Example usage
print(contains_element("chat"))  # True
print(contains_element(42))  # False
