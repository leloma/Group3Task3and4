# -*- coding: utf-8 -*-
"""Task 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19s2jQKLFipbDX1K66G2xliqY_vN44_zH
"""

grammar = {
    "E": ["T E'"],
    "E'": ["+ T E'", ""],
    "T": ["F T'"],
    "T'": ["* F T'", ""],
    "F": ["( E )", "id"],
}


# Define the terminals and non-terminals
terminals = set(["+", "*", "(", ")", "id", "$"])
non_terminals = set(["E", "E'", "T", "T'", "F"])


# Create an LL(1) parsing table
parsing_table = {}

def compute_first(symbol):
  first_set = set()
  if symbol in terminals:
    return {symbol}

  for production in grammar[symbol]:
    if "" != production:
      split = production.split()
      first = split[0]
      first_set.update(compute_first(first))

    else:
      first_set.update("$")

  return first_set


first_dict = dict()

for key in grammar.keys():
  first_dict.update({key: compute_first(key)})

print(first_dict)

follow_dict = dict()

def compute_follow(symbol):
  viable_productions = {}
  follow_set = set()
  for (nont, productions) in grammar.items():
    for production in productions:
      if symbol in production.split():
        viable_productions.update({nont: {production}})

  for (key,prods) in viable_productions.items():
    for prod in prods:
      chars = prod.split()
      symbol_index = chars.index(symbol)
      next = symbol_index+1

      if symbol == list(grammar.keys())[0]:
        follow_set.update("$")

      if symbol_index == len(chars)-1:
        follow_set.update(compute_first(key))
      else:

        follow_set.update(compute_first(chars[next]) )

  return follow_set

for key in grammar.keys():
  follow_dict.update({key: compute_follow(key)})

print(follow_dict)

print(follow_dict)

for nt in non_terminals:
    for terminal in terminals:
        parsing_table[(nt, terminal)] = []

for nt, production in grammar.items():
    for prod in production:
        if prod != "":
          char = prod.split()
          first_set = compute_first(char[0])
          for terminal in first_set:
            parsing_table[(nt, terminal)].append(prod)
        else:
          follow_set = compute_follow(nt)
          parsing_table[(nt, terminal)].append(prod)

print(parsing_table)

print("LL(1) Parsing Table:")
for nt in non_terminals:
    for terminal in terminals:
        key = (nt, terminal)
        print(f"{key}: {parsing_table[key]}")