#iterator



nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i']
]



class FlatIterator:

	def __init__(self, my_list):
		self.my_list = my_list
		self.position = -1

	def __iter__(self):
		return self

	def __next__(self):
		new_list = sum(self.my_list, [])
		if len(new_list) - 1 == self.position:
			raise StopIteration
		else:
			self.position += 1
			return new_list[self.position]



if __name__ == '__main__':
	for item in FlatIterator(nested_list):
		print(item)
	print('\n')



#generator


my_list_simple = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

my_list_hard = [
    [],
    [1, [2], 3, 4, [5, 6, 7]],
    [8, 9, 10, 11],
    [12, 13, 14, [[[[15]]]]], []
]


class FlatIterator:

    def __init__(self, multi_list):

        self.multi_list = multi_list  # список с воложенными списками

    def __iter__(self):
        self.multi_list_iter = iter(self.multi_list)
        self.nested_list = []  # вложенный список с элементами
        self.nested_list_cursor = -1
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if len(self.nested_list) == self.nested_list_cursor:
            self.nested_list = None
            self.nested_list_cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.multi_list_iter)
                #  если  список пустой, то получаем следующий
                #  если списки закончаться, получим stop iteration

        return self.nested_list[self.nested_list_cursor]


print('Задача 2')
for item in FlatIterator(my_list_simple):
    print(item)
print('*' * 25)