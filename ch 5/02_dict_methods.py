marks = {
    "Bhavesh":100,
    "Arnav":95,
    "Abhay":73
}

print(marks.items())                           #This function prints total items in dict   
print(marks.values())                          # This will print right side things in dict
print(marks.keys())                            #This will print left side things in dict
marks.update({"Bhavesh":99,"Tanmay":95})       #This is function used to update dict values andd add new thing in dict 
print(marks)

print(marks.get("Arnav2"))                     #This will print none 
#print(marks["Arnav2"])                         #This will print error 

print(marks.fromkeys("Anu",89))
print(marks)
