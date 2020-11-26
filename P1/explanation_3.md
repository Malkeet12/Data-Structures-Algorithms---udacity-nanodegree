    steps for encoding given text
    
    # create frequency generator
    # generate  priority queue(using heap)
    # generate huffman tree
    # generate codes for char
    
    steps for decoding the given message
    # decode input byte values using codes generated from the huffman tree
    
    
    Time complexity:
    huffman_encoding 
    
    lets calculate it function by function
    make_frequency => we are iterating through all the elements in the input text to calculate their frequency
    so time complexity is O(n) 
     
    make_heap => we are iterating through all the elements in the frequenct dict to generate priority queue
    so time complexity is O(n) 
    
    merge_codes => we are iterating through all the elements in the priority queue and
     adding element in the heapq  which takes O(logn)
     
    so time complexity is O(n) *O(logn)=>O(nlogn)
    
    
    make_codes => we are using recursion in this and in every new recursive call we are getting rid of half elements
    as per we are checking only left tree/ or right tree
    so time complexity is O(logn) 
    
    overall complexity is o(n) + o(n) + o(n) + o(logn) => O(n
    huffman_encoding is an example of linear time complexity.
    
    huffman_decoding
    we are iterating through all the elements to decode the bits
    so time complexity is O(n) 
    huffman_decoding is an example of linear time complexity.
    
    
    
    
    Space complexity:
    huffman_encoding
    
    we have used many variables, list and dictionary
    and heap tree and priority queue depends on the input size and will increase linearly as our input icreases
    so space complexity is O(n)
    
    huffman_decoding is an example of linear space complexity. 
     
     similarly huffman_decoding depends on the input size and grows linearly with the input
     so space complexity is O(n)
    
    huffman_decoding is an example of linear space complexity.
    