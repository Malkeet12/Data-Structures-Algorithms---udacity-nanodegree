we are using linked list to implement block chain

we have created a node(block for blockchain) that accepts 3 parameters (timestamp, data, previous_hash)
and we are using list to maintain the block chain
and when we to have add element in the blockchain, we will push the node in the chain list

time complexity :
 we are maintaining a list and appending that list whenever new block is added,
 
 so time complexity is O(n)
 linear time complexity
 
 
 space complexity:
 
 size of block chain list will increase with the input size
 and it increased linearly
 so space complexity is O(n)
 linear space complexity