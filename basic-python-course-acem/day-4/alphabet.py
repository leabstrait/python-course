magic_distance =  ord('a') - ord('A')
print(magic_distance)

for c in range(ord('A'), ord('Z') + 1):
    print(chr(c) + chr(c+magic_distance), end=" ")