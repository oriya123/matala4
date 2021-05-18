import requests
import re
ditancecity=list()
def places ():
    city1='' 
    city2=''
    city3=''
    ditancecity1=0 
    ditancecity2=0
    ditancecity3=0
    file= open("dests.txt",encoding="utf8")
    destinations_list=list()
    distanceslist = [] 
    for line in file:
            destinations_list.append(line.strip()) 
    for i in range(len(destinations_list)):
        distance(destinations_list[i]) 
    print(destinationsPerCity)
    distance11 = re.compile(r"([^km]+)") 
    for j in ditancecity:
        includekm = distance11.search(j)
        if includekm:
            distanceslist.append(j[includekm.span()[0]:includekm.span()[1]].replace(' ','').replace(',','')) 
    distanceslist = [float(j) for j in distanceslist] 
    for j in range(len(distanceslist)):
        if distanceslist[j]>ditancecity1:
            ditancecity3=ditancecity2
            ditancecity2=ditancecity1
            ditancecity1=distanceslist[j]
            city3=city2
            city2=city1
            city1=destinations_list[j] 
        elif distanceslist[j]>ditancecity2:
            ditancecity3=ditancecity2
            ditancecity2=distanceslist[j]
            city3=city2
            city2=destinations_list[j]
        elif distanceslist[j]>ditancecity3:
            ditancecity3=distanceslist[j]
            city3=destinations_list[j]

    print('\n' ,"The 3 furthest cities from Tel-aviv are:", 
          '\n','1)', city1.strip(),' = ', ditancecity1, 'km'
          '\n','2)', city2.strip(),' = ', ditancecity2, 'km'
          '\n','3)', city3.strip(),' = ', ditancecity3, 'km')
    
def distance(distance1):
        adress="תל אביב"
        api_key="מופיע בקובץ שהועלה למודל"
        url="https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&key=%s" %(adress,distance1,api_key)
        response=requests.get(url).json()
        url2="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" %(distance1,api_key)
        response2=requests.get(url2).json()
        try:
            distance =response['rows'][0]['elements'][0]['distance']['text']
            duration = response['rows'][0]['elements'][0]['duration']['value']
            latitude = response2['results'][0]['geometry']['location']['lat']
            longitude = response2['results'][0]['geometry']['location']['lng']
            ditancecity.append(distance)
            latitude ='lat:'+ str(latitude)
            longitude ='lng:'+ str(longitude)
            if((duration/3600)<1):
                duration=duration/60
                duration=str(duration) +""+ 'min'
            else:
                hours=int(duration/3600)
                min=round(((duration%3600)/3600)*60,2)
                duration=str(hours)+' hours '+ str(min)+ ' min '
            detailsPerCity = (distance, duration) + (latitude, longitude) 
            destinationsPerCity[distance1] = detailsPerCity
        except:
            print("לא מזהה את הערך" +" "+ distance1)
    
    
destinationsPerCity=dict()
places ()