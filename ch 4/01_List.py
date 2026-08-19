# Unlike string lists are muitable means we can change the original list

a = ["Batman", "Rohan", 23, 578.34, True, "apple"]        #a is a list and it is storing various data types

print(a[0])                                               
print(a[3])

a[1] = "Kartik"                                  #here in original list we replace Rohan with Kartik

print(a[1])                                      #For lists slising works same as string just the diff is string slice words while list datatypes
print(a[0:3])

a = "Bhavesh"
print(a)