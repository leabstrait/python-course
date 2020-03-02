# def converter(lot):
#     fahr_list = []
#     for ct in lot:
#         ft = 1.8*ct + 32
#         fahr_list.append(round(ft, 2))

#     return fahr_list


lotc = [-14, 1, 24, 26, 32, 36, 40, 42, 45, 49]
# print(converter(lotc))


# cel_to_fahr = lambda ct: round(1.8*ct + 32, 2)

# # def cel_to_fahr(ct):
# #     return 1.8*ct + 32

# lotf = map(cel_to_fahr, lotc)
# lotf = list(lotf)

# print(lotf)

def less_than_body_temp(tc):
    return tc < 36

print(list(filter(less_than_body_temp, lotc)))
print(list(filter(less_than_body_temp, lotc)) == [-14, 1, 24, 26, 32])

