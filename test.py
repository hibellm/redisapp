#!/usr/bin/python	
	
	
def percent(num1, num2,dp):
	var = ' ({0:.'+str(dp)+'%}'
	print(var)
	return var.format((num1 / num2))+str(")") 
	
print(percent(123,442,2))