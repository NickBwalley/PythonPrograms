#Dictionaries can be useful to store Key value pairs 
monthsConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: "Sunday"
}

print (monthsConversion["Mar"])#First Way to Print Values from a dictionary using the key
print(monthsConversion.get("Dec", "Key Not Found!.."))#Second way to Print Values from a Dictionary using the get()
print(monthsConversion.get(1, "Invalid Key!"))#Default Value if invalid key is entered