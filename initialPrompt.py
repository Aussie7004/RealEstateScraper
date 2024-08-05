import requests

from bs4 import BeautifulSoup


# Valid web scarping URLs (tested)
realtor = 'realtor.com'
domainAU = 'domain.com.au'

# Inputted Link
url = ""
validDomain = False

realtorCheck = False
domainAUCheck = False

class userData():
    
    def __init__(self) -> None:
        pass
    # Gets user input
    def userInputValidation(url, valid):
        
        print("Please enter a url from one of the below websites: ")
        print(realtor + "\n" + domainAU)
        
        url = input("Enter a URL: ")
        
        # Verifies that web page is scrapable from pre-set list.
        if realtor.lower() in url or domainAU.lower() in url:
            valid = True
            
            urlCheck = requests.get(url)
            urlValid = False
            
            # Verifies that URL is valid
            if urlCheck.status_code == 200:
                urlValid = True
                print("URL Good")
            else:
                if urlValid == False:
                    while urlValid == False:
                        url = input("Enter a valid URL: ")
                        
                        if urlCheck.status_code == 200:
                            urlValid = True
                            print("URL is now good")
                            
        elif valid == False:
            while valid == False:
                print("Please enter a url from one of the below websites: ")
                print(realtor + "\n" + domainAU)                
                url = input("Please enter a valid url: ")
                if realtor.lower() in url or domainAU.lower() in url:
                    valid = True
                    
                    urlCheck = requests.get(url)
                    urlValid = False

                    if urlCheck.status_code == 200:
                        urlValid = True
                        print("URL Good")
                    else:
                        if urlValid == False:
                            while urlValid == False:
                                url = input("Enter a valid URL: ")
                                urlCheck = requests.get(url)
                                if urlCheck.status_code == 200:
                                    urlValid = True
                                    print("URL is now good")
                                    

        else: 
            return "An error has occurred. Quitting"             
        

userData.userInputValidation(url, validDomain)
