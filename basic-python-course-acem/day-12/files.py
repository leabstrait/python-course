# import os

# # os.mkdir('tests')

# with open('tests/test.txt', 'w+') as f:

#     print(f.writelines(['this\n', 'is', 'a', 'list']))

#     print(f.closed)
	
# print(f.closed)


with open('test.txt' ,'w+') as f:
	f.write('asdgadgasdgas\ndfasdfasdf')
	f.seek(0)
	print(f.readlines())
	f.write('\nasdgadgasdgas\ndfasdfasdf')

