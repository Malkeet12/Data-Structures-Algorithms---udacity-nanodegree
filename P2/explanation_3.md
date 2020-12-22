first we are sorting the list in descending order with merge sort and it has a  
time complexity of O(nlogn)

highest integer will be the  most significant bit for our number,
so  we are iterating through the sorted list and 
adding values in two numbers, we are alternating find highest number and assigning the highest number as most significant bit
it has a time complexity of O(n)

so overall time complexity is O(nlogn)

we have used few variables but the number of variables doesn't depend on the input size
so space complexity is O(1)