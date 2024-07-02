#!/usr/bin/env python3

# Initial lists
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

# Display initial lists
print("Initial proto list:", proto)
print("Initial protoa list:", protoa)

# Append "dns" to both lists
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print("\nAfter appending 'dns' to both lists:")
print("proto list:", proto)
print("protoa list:", protoa)

# List of common ports
proto2 = [22, 80, 443, 53]

# Extend proto with proto2
proto.extend(proto2) # pass proto2 as an argument to the extend method
print("\nAfter extending proto with proto2:")
print("proto list:", proto)

# Append proto2 as a single element to protoa
protoa.append(proto2) # pass proto2 as an argument to the append method
print("\nAfter appending proto2 to protoa:")
print("protoa list:", protoa)

# Demonstrate the use of the insert method
proto.insert(1, "ftp") # this will insert "ftp" at index 1
print("\nAfter inserting 'ftp' at index 1 in proto:")
print("proto list:", proto)

# Demonstrate the use of the remove method
proto.remove("https") # this will remove the first occurrence of "https"
print("\nAfter removing 'https' from proto:")
print("proto list:", proto)

# Demonstrate the use of the pop method
removed_element = proto.pop() # this will remove and return the last item in the list
print("\nAfter popping the last element from proto:")
print("proto list:", proto)
print("Removed element:", removed_element)

# Demonstrate the use of the reverse method
proto.reverse() # this will reverse the elements of the list in place
print("\nAfter reversing proto:")
print("proto list:", proto)

# Demonstrate the use of the sort method
proto2.sort() # this will sort the list proto2 in ascending order
print("\nAfter sorting proto2:")
print("proto2 list:", proto2)

# Demonstrate the use of the clear method
protoa.clear() # this will remove all items from protoa
print("\nAfter clearing protoa:")
print("protoa list:", protoa)

