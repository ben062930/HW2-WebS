import bs4 as bs4
import requests
import time

def webScraper():
    # write into txt file:
    with open('D:/pycharm/New project/FE595HW2/companies.txt', "wt") as f:
        for i in range(0,50):
            try:
                times = i+1
                print(times, file=f)    # print the times into file
                # make a request
                rr = requests.get('http://3.95.249.159:8000/random_company')
                soup = bs4.BeautifulSoup(rr.text, 'html.parser')

                Li = soup.select('li')
                for text in Li:
                    content = text.getText()
                    a = 'Name'    # get name
                    b = 'Purpose'  # get purpose
                    if a in content:
                        print(content, file=f)   # print name into file
                    if b in content:
                        print(content, file=f)   # print purpose into file
                 time.sleep(0.5)
            except:
                print("error", file=f)

if __name__ == "__main__":
    webScraper()
