a = open("cursed.dat")
b = a.readlines()
for x in range(0, len(b)):
    z = b[x].strip().split()
    day = ""
    month = ""
    year = str(z[2])
    final_date = ""
    h = {"January":"01",
         "February":"02",
         "March":"03",
         "April":"04",
         "May":"05",
         "June":"06",
         "July":"07",
         "August":"08",
         "September":"10",
         "November":"11",
         "December":"12"
         }
    month = h[z[0]]
    if int(z[1].replace(",",""))<10:
        day = "0" + z[1].replace(",","")
    else:
        day = z[1].replace(",","")
    final_date = month+day+year
    if final_date[:4] == "".join(reversed(final_date[4:])):
        print(final_date + ": DON'T TRAVEL")
    else:
        print(final_date + ": OK TO TRAVEL")