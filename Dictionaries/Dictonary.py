
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
    "Dec": "December"
}

print (monthsConversion["Mar"])#First Way to Print Values from a dictionary using the key
print(monthsConversion.get("Dec"))#Second way to Print Values from a Dictionary using the get()
print(monthsConversion.get("Marse", "Invalid Key!"))#fails gracefully if invalid key is entered