import requests
import pandas as pd
from bs4 import BeautifulSoup

def descargar_efemerides(object_name, start_date, num_days= 4001):
    # Variables
    interval = 1
    title = "Predefined title"
    base_url = "Predefined base url"
    efemerides = [['obs_date', 'delta', 'r', 'phase']]
    url_ephem = "https://cgi.minorplanetcenter.net/cgi-bin/mpeph2.cgi"
    
    # Request header
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Form fields needed:
    data = {
        'ty': 'e',  # Return ephemerides
        'd': start_date,    # Start date of ephemerides
        'l': num_days,  # Num days from start date
        'TextArea': object_name,    #Object name
        'i': interval,  # Sample interval
        'u': 'd',  # Sample interval measurements units = days
        'tit' : title,  
        'bu' : base_url,
        #... add more if needed
    }

    # Sending POST request with the form data
    response = requests.post(url_ephem, data=data, headers=headers)
    successful_download = False

    # If request succeeded, process content
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        print('Success in submitting the ephemeris form')
        
        data_element = soup.find('pre')
        successful_download = True

    else:
        print('The ephemeris form submission was not successful')        

        
    if successful_download:
        data_text = data_element.text.splitlines() # type: ignore

    else:
        print("Not available ephemeris data")
        print(response.text)     # -------------------->> Only for debugging
        successful_download = False

    if successful_download: 
        for line in data_text:
            parts = line.split()

            # Extract year, month, day, Delta, r and phase
            if len(parts) > 13:  # To make sure it is a data line
                year, month, day, delta, r, phase = parts[0], parts[1], parts[2], parts[8], parts[9], parts[11]
                efemerides.append(['-'.join([year, month, day]), float(delta), float(r), float(phase)]) # type: ignore
                
        print('Ephemeris data stored successfully')
        efemerides_df = pd.DataFrame(efemerides[1::], columns= efemerides[0]) # type: ignore
        efemerides_df['obs_date'] = pd.to_datetime(efemerides_df.obs_date)
        return efemerides_df
    
if __name__ == '__main__':
    descargar_efemerides()