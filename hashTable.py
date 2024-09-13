
size = 5 #size of the hash table
map={} #empty hash table
array_list=[[] for i in range(size)]
primme_num = 6700417 # larger prime number
a = 6 # random value from {1,2 ... p-1}
b = 5 # random value from {0,1,2 ... p-1}

def hash_func(key):
          # Using universal family of hash function where is k is key of the hash table
          # size is the number of slot available for storage     
        return ((a * key + b) % primme_num) % size
        
def insert(key, value):
        if len(map) >= size:
               print("Size exceeded for the hashTable") #Could implement dynamic increse in side
               return
        hashed_key = hash_func(key)

        for i, j in enumerate(array_list[hashed_key]): #loop through the array at index "hashed_key"
               if key == j[0]: #if the input key matches any key in the tuple, replace the key, value pair
                    array_list[hashed_key][i] = ((key, value))
                    return

        array_list[hashed_key].append((key, value)) #in case when the k is first hash value, append the tuple at index "hashed_key"
   
def search(key):
        hashed_key = hash_func(key)
        print("Searching key", hashed_key)

        for i,j in enumerate(array_list[hashed_key]):
              if key == j[0]: # if the hashed key is found then check it loops through the list to get the key
                    print(f"The value for {key} is {j[1]}")
              else:
                    print("Key not found while searching")
                          
def delete(key):
        print("Before Deleting key", array_list)
        
        hashed_key = hash_func(key)
        print("Deleting key", hashed_key)

        for i, j in enumerate(array_list[hashed_key]):
            if key == j[i]: # if the hashed key is found then check it loops through the list to get the key and delete the tuple
                   del array_list[hashed_key][i]
            else:
                print("Key not found")        
  
        print("After Deleting key", array_list)


insert(1, "cat")
insert(2, "dog")
insert(3, "sheep")
insert(4, "tiger")
insert(5, "w")
insert(6, "e")

search(1)

delete(1)

