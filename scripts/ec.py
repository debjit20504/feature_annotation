import sys
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

def scrap_info(ec_number : str):
    url = f'https://enzyme.expasy.org/EC/{ec_number}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        td_colspan_2 = soup.find('td', colspan='2')
        if td_colspan_2:
            enzyme_name_tag = td_colspan_2.find('strong', {'property': 'schema:name'})
            enzyme_name = enzyme_name_tag.text.strip() if enzyme_name_tag else np.nan
        else:
            enzyme_name = np.nan
    return enzyme_name

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    ec_data = {
        'Id' : [],
        'Info' : [],
    }
    
    with open(input_file, 'r') as file:
        ec_file = [i.strip() for i in file.readlines()]
        
        for i in ec_file:
            info = scrap_info(i)
            ec_data['Id'].append(i)
            ec_data['Info'].append(info)
        file.close()

    df = pd.DataFrame(ec_data)
    
    if 'csv' in output_file:
        df.to_csv(output_file, index=False)
    else:
        df.to_csv(f'{output_file}.csv', index=False)