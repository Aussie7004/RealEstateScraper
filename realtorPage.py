import requests

from bs4 import BeautifulSoup

from initialPrompt import url

# Initiating variables for extracted info
price = ""
address = ""
City = ""
State = ""


class realtor():

        
    
    def webPageData(propertyValue, propertyAddress, propertyCity, propertyState):
        global price
        global address
        global City
        global State
        
        response = requests.get(url)
        page = BeautifulSoup(response.text, features='html.parser')
        
        propertyValue = page.find('div', class_ = 'property-price').text
        propertyAddress = page.find('h1', class_ = 'display-address').text
   
        price = propertyValue
        address = propertyAddress
        City = propertyCity
        State = propertyState
        
        print(propertyValue, propertyAddress)
    
    
    def readableData():
        
        global price
        global address
        global City
        global State
        
        priceFormatted = ""
        addressFormatted = ""
        CityFormatted = ""
        StateFormatted = ""

        position = 0
        # Cycles through global String variables and makes them formatted nicer for CSV file
        
        for p in range(len(price)):
            if price[p] == "$":
                p += 1
            elif price[p] == ",":
                p+=1
            else:
                priceFormatted += price[p]

        #Gets street address       
        for a in range(len(address)):
            if address[a] == ",":
                position = a+2
                break
            else:
                addressFormatted += address[a]
        # Sets position to where address ends in the string   
        address = address[position:len(address)-1]
        
        # Gets City
        for c in range(len(address)):

            if address[c] == ",":
                position += c
                break
            else:
                CityFormatted += address[c]
        
        address = address[position:len(address)-1]
        
        # Gets State
        for c in range(len(address)):

            if address[c] == ",":
                position += c
                break
            else:
                StateFormatted += address[c]

                
        
        price = int(priceFormatted)
        address = addressFormatted
        City = CityFormatted
        State = StateFormatted
        
        print(url, priceFormatted, addressFormatted, CityFormatted, StateFormatted)
            
        
        
        
        


realtor.webPageData(price, address, City, State)
realtor.readableData()
