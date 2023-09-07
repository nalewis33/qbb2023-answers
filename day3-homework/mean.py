#!/usr/bin/env python


def my_mean(int_list=[]): #defining the mean function, where you supply a list of integers and the mean is calculated for it
	total = 0 #defining the variable total, set to zero before suppling the list
	for number in int_list: #for any number in the integer list:
		total +=number #add the number to the total
	list_mean = total/len(int_list) #divide the total sum by the length of the list to get the mean
	return(list_mean) #return the mean of the list


# Test case to see if the function works: with values, expected to return a mean of 2.5
#test_list = [1,2,3,4] #supplying test list of ints
#test_mean = my_mean(test_list) #saving the calculated mean to variable test_mean
#print(test_mean) #printing
