
# Create a frozen set named frozen_set containing elements "hello", "world".
frozen_set = frozenset({"hello", "world"})

# Try to add "!" to frozen_set
# Raises an AttributeError: 'frozenset' object has no attribute 'add'

# Create a normal set named normal_set containing elements "let's", "learn".
normal_set = {"let's", "learn"}

# Try to add frozen_set to normal_set. Why does it work? Explain.
# Print normal_set.
normal_set.add(frozen_set)
print(normal_set)
# After running it half a dozen times: The order of the items changes
