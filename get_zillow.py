import requests
from bs4 import BeautifulSoup as soup
import pandas as pd


def scrapping_zillow(address_from_file):
    '''
    This is the function for scrapping data from Zillow.
    It cannot scrap data if the there is no field for bed, bath and the area in Acres.
    :param address_from_file: type: text, address
    :return: bed, bath, area, z_estimate, z_estimate_rent
    '''
    # Set Header
    hdr1 = address_from_file.split(",")[0].replace(" ", "-")
    hdr2 = address_from_file.split(",")[1].replace(" ", "-").replace('Â\xa0', '')
    hdr3 = address_from_file.split(",")[2].replace(" ", "-")
    url = 'https://www.zillow.com/homes/{}, {},{}_rb/'.format(hdr1, hdr2, hdr3)
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'referer': url}

    # Send a get request:
    html = requests.get(url=url, headers=header)
    bsobj = soup(html.content, 'lxml')

    # Accessing data
    summary_container = bsobj.findAll('div', {'class': 'summary-container'})[0]
    bed_bath_area = summary_container.find('div').find('div').find('div').find('span').text

    bed = bed_bath_area.split('bd')[0].strip()
    bath = bed_bath_area.split('bd')[1].split('ba')[0].strip()
    area = bed_bath_area.split('bd')[1].split('ba')[1].split('sqft')[0].strip()
    address = summary_container.find('div').find('div').findAll('div')[1].text.replace('\xa0', ' ')
    z_estimate = summary_container.findAll('span', {'data-testid': 'zestimate-text'})[0].text.split(":")[1]
    try:
        z_estimate_rent = summary_container.findAll('span', {'data-testid': 'zestimate-text'})[1].text.split(":")[1]
    except:
        z_estimate_rent = 'None'

    return bed, bath, area, z_estimate, z_estimate_rent


# file_name = input('What is the file name?: ')
file_name = 'Zillow/house_addresses.txt'
address_list = []
bed_list = []
bath_list = []
area_list = []
z_estimate_list = []
z_estimate_rent_list = []
not_processed_list = []
with open(file_name) as f:
    lines = f.readlines()
f.close()
for line in lines:
    address = line.strip()
    try:
        bed, bath, area, z_estimate, z_estimate_rent = scrapping_zillow(address)
        address_list.append(address.replace('Â\xa0', ''))
        bed_list.append(bed)
        bath_list.append(bath)
        area_list.append(area)
        z_estimate_list.append(z_estimate)
        z_estimate_rent_list.append(z_estimate_rent)
    except:
        print('Not Processed: {}'.format(address.replace('Â\xa0', '')))
        not_processed_list.append(address.replace('Â\xa0', ''))

# Saving data in dictionary format and dataframe
result_dict = {'Address': address_list, 'Bed': bed_list, 'Bath': bath_list,
               'Area(sqft)': area_list, 'Zestimate($)': z_estimate_list, 'Rent Zestimate($)': z_estimate_rent_list}
df = pd.DataFrame(result_dict)
# Saving dataframe as csv file
saving_file_name = 'Zillow/Zillow_Data.csv'
df.to_csv(saving_file_name, sep=',', encoding='utf-8')
print('File Saved')
print("Following addrsses were not processed.")
print(not_processed_list)