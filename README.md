# Poker lottery

Basically a pseudorandom, reproducible way to turn poker into a lottery.

Takes people's names, chip totals, and "lucky words" (aka seed components of the prng). Sorts the array of (name, chips, lucky word) alphabetically by name. Concatenates that all, uses that as a seed for python's random.random. Then picks a name with probability proportional to chip count.

NB I should make sure to use random.random for reproducibility.
