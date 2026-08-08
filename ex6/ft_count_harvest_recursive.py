def ft_count_harvest_recursive() -> None:
	a = int(input("Days until harvest: "))
	def helper(day): #nested function
		if day <= a:
			print("Day", day)
			helper(day + 1) #recursive part
		else:
			print("Harvest time!")
	helper(1)
