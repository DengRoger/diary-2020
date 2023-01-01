count = 0
for i in range(5):
	for j in range(7):
		count += 1 
		print("self.B"+ str(count) +" = QtWidgets.QPushButton(self)")
		print("self.B"+ str(count) +".setGeometry("+str(142*(j+1))+","+ str(120*(i+1)) +", 142, 120)")
		print("self.B"+ str(count) +".setText(num)")
		print("self.B"+ str(count)  +".clicked.connect(self.label_"+str(count)  +"Clicked)")
		print( )
		print( )

'''count = 0 
for i in range(1,36):
	count += 1
	print("def label_"+str(i)+"Clicked(self):")
	print("    pass")
'''
'''
for i in range(35):
	print("self.B"+str(i+1)+".setText(num["+str(i)+"])")

'''
for i in range(35):
	print("self.B"+str(i+1)+".show()")
