# def is_anagram(w1, w2):
#     if len(w1) == len(w2):
#         for c in w1:
#             if c in w2:
#                 still_true = True
#             else:
#                 still_true = False

#         return still_true
#     return False


# def is_anagram_simple(w1, w2):
#     return sorted(list(w1)) == sorted(list(w2))

is_anagram_simple_lambda = lambda w1, w2: sorted(list(w1)) == sorted(list(w2))



# print(is_anagram('mango', 'mang'))

# print(is_anagram('mango', 'ngoam'))

print(is_anagram_simple_lambda('mango', 'mang'))

print(is_anagram_simple_lambda('mango', 'ngoam'))