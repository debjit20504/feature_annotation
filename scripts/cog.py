import sys
import requests
import numpy as np
import pandas as pd

def get_info(cog_id : str):
    url = f"https://www.ncbi.nlm.nih.gov/research/cog/api/cog/?cog={cog_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info = data['results'][0]['cog']['name']
    else:
        return np.nan
    return info

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    cog_data = {
        'Id' : [],
        'Info' : []
    }
    
    with open(input_file, 'r') as file:
        cog_file = [i.strip() for i in file.readlines()]
        
        for i in cog_file:
            info = get_info(i)
            cog_data['Id'].append(i)
            cog_data['Info'].append(info)
        file.close()
        
    df = pd.DataFrame(cog_data)
    
    if 'csv' in output_file:
        df.to_csv(output_file, index=False)
    else:
        df.to_csv(f'{output_file}.csv', index=False)