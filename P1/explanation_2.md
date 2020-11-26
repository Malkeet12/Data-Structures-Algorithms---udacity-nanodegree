we are using recursion for this problem
if we encounter any folder we are calling the recursive function again 
and otherwise if it is a file then and it is ending with our desired suffix, add the file into 
our output list
we are calling find_files_recursive function recursivelt, so 
Time complexity depends on the find_files_recursive function

we are usually concerned with the worst-case time complexity, and it depends on the depth of the folder, so 
 the time complexity of is  dependent on depth 𝑇(𝑛) .
 
 we are visiting every item only once
  so it is linearly dependent on input size
  T(n) = n (we can ignore the smaller values)
  This is an example of linear time complexity.
  
  
  
  
  Space complexity:
  
  we have used few variables
  out_list -> list
  complete_path -> string
  files -> list
  
space complexity depends on the input size and it is increasing linearly with that
    => O(n)

This is an example of linear space complexity.