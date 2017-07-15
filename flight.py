from urllib import request
import json

origin = "DEL"
destination = "GOI"
dept_date ="21-10-2017"
adult = "1"
children = "0"
infant = "0"
f1=open('data.csv', 'w')
f1.write("Origin" + "," + "Destination" + "," + "Dept_Date" + "," + "Dept_Time" + "," + "Arr_Time" + "," + "Total_Fare" + "," + "Base_Fare" + "," + "Fuel_Fare" + "," + "Airways" + "," + "Available" + "," + "Duration" + "," + "Class_Type" + "," + "Flight Number"+ "," + "Flight Code" + "," + "FlightID" + "," + "Hopping"+"\n")

url = "http://flights.makemytrip.com/makemytrip/" + "search/O/O/E/" + adult +"/" + children + "/" + infant + "/S/V0/" + origin + "_" + destination + "_" + dept_date
print(dept_date + "\n" + url)
html = request.urlopen(url).read()
fil = open("html.txt","w")
fil.write(html.decode())
fil.close()
fil = open("html.txt","r")
for line in fil.readlines():
    if "flightsData" in line:
        flights_data = line
        break
flights_data = flights_data.replace("var flightsData = ","").strip()
flights_data = flights_data[:-1]
fil = open("flights_data.json","w")
fil.write(flights_data)
fil.close()
l=json.loads(flights_data)

for i in range(len(l)):  
    airways = l[i]['le'][0]['an'] 
    fare = l[i]['af']
    deptdate = l[i]['le'][0]['dep']
    depttime = l[i]['le'][0]['fdt']
    arrtime = l[i]['le'][0]['fat']
    avail = l[i]['le'][0]['flightFare']['bookingClass']['availability']
    basefare = l[i]['le'][0]['flightFare']['baseFare']
    fuel_surcharge = l[i]['le'][0]['flightFare']['fuelSurcharge']
    duration = l[i]['td']
    origin = l[i]['le'][0]['o']
    desti = l[i]['le'][0]['d']
    class_type = l[i]['le'][0]['cls']
    flight_number = l[i]['le'][0]['fn']
    flight_code = l[i]['le'][0]['oc']
    Flight_ID = l[i]['fi']
    hopping = l[i]['hff']
    f1.write(origin + "," + desti + "," + deptdate + "," + depttime + "," + arrtime + "," + str(fare) + "," + str(basefare) + "," + str(fuel_surcharge) + "," +airways+ "," + avail + ","+duration + "," + class_type + ","+ flight_number + "," + flight_code + ","  + Flight_ID + "," + str(hopping) +"\n")

f1.close()
