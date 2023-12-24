import sys
import requests
import numpy as np
import pandas as pd

def get_info(bigg_id : str):
    url = f"http://bigg.ucsd.edu/api/v2/models/{bigg_id.split('.')[0]}/genes/{bigg_id.split('.')[1]}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        info = data['reactions'][0]['name']
    else:
        return np.nan
    return info

if __name__ == '__main__':
    input_file = sys.argv[1] # input file is the text file that contains BiGG id's
    output_file = sys.argv[2] # output csv file that will contains annotation information
    bigg_dictionary = {
        'Id' : [],
        'Info' : []
    }
    with open(input_file, 'r') as file:
        bigg_file = [i.strip() for i in file.readlines()]
        for i in bigg_file:
            info = get_info(i)
            bigg_dictionary['Id'].append(i)
            bigg_dictionary['Info'].append(info)
        file.close()
    df = pd.DataFrame(bigg_dictionary)
    if 'csv' in output_file:
        df.to_csv(output_file, index=False)
    else:
        df.to_csv(f'{output_file}.csv', index=False)