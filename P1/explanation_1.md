we are using OrderedDict to  retrieve  and add the the element in constant time 

while setting the element we are checking the length of cache, 
if it is greater than the capcity of cache then remove the first element from the orderedDict

Time complexity: 

retrieving the element: T(1) =>  O(1) means the time is constant
                        (lookup from dictionary takes constant time) 
setting the element: T(1) =>  O(1) means the time is constant
                        (adding item in dictionary takes constant time) 
                        
Space complexity: 

we have two variable cache and capacity,
cache size will increase as we keep adding elements

if we assume int takes 4 bytes

4*n(cache dict) + n(capacity variable)
=> O(n)

This is an example of linear space complexity.
