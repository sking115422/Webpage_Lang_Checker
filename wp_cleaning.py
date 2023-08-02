from bs4 import BeautifulSoup
from langdetect import detect
import requests
import pandas as pd
from joblib import parallel_backend
from joblib import Parallel, delayed

wp_list = pd.read_csv("./top-1m.csv")

wp_list = wp_list["domain"].to_list()

inc = 0
keep = []

def check4English(url, inc):
    try:
        print(inc)
        response = requests.get("http://" + url, timeout=1)
        soup = BeautifulSoup(response.content, "html.parser")
        # print(soup.prettify())
        if "en" in soup.html["lang"].lower():
            keep.append(url)
            f.write(url + "\n")
    
    except Exception as e:
        print("error")    


with open("./wp_eng_mast_list.txt", "+a") as f:
    with parallel_backend('threading'):
        Parallel(n_jobs=-1)(delayed(check4English)(wp_list[i], i) for i in range(0, len(wp_list))) 
    

        







