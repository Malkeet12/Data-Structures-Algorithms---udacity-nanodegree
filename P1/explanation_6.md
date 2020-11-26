we are using dictionary for this problem

for union:

we are iterating both linked lists one by one and
updating our map and finally creating new linked list by iterating this map


for intersection: 
we will iterate first list and all elements in the map
and then  we will iterate second list
 push those elements in our output list which are present in the map
 and finally return the linked list generated from this output list
 
 
 union :
 time complexity: we are iterating through both linked list one by one 
 and in the end generating through output array,
 and complexity increases linearly with time
 so time complexity = O(n)+O(n)+O(n) =>O(n)
 
 so union has linear time complexity
 
 space complexity: space will grow with input and it is growing linearly
 so space complexity is linear => O(n)
 
 
 intersection:
 time complexity:
 we are iterating through both linked list one by one 
 and in the end generating through output array,
 and complexity increases linearly with time
 so time complexity = O(n)+O(n)+O(n) =>O(n)
 
 so intersection has linear time complexity
 
 space complexity: space will grow with input and it is growing linearly
 so space complexity is linear => O(n)