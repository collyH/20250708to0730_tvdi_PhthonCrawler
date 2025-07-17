import json

from pprint import pprint

# 建立一個空的Site類別，叫做Site
class Site:
    def __init__(self, 
                 sitename,
                 county,
                 aqi,
                 pollutant, status, pm2_5, longitude, datacreationdate):
        self.sitename = sitename
        self.county = county
        self.aqi = aqi
        self.pollutant = pollutant
        self.status = status
        self.pm2_5 = pm2_5
        self.longitude = longitude
        self.datacreationdate = datacreationdate
# 解析JSON檔案，並將每個站點的資料轉換為Site實體

def parse_sites_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    site_list = []
    for record in data['records']:
        site = Site(
            sitename=record['sitename'],
            county=record['county'],
            aqi=record['aqi'],
            pollutant=record['pollutant'],
            status=record['status'],
            pm2_5=record['pm2.5'],
            longitude=record['longitude'],
            datacreationdate=record['datacreationdate']
        )
        site_list.append(site)
    return site_list

# 讀取JSON檔案並解析
parse_sites = parse_sites_from_json('aqx_p_488.json')
for site in parse_sites:
    print(f"站點名稱：{site.sitename}, 所在縣市：{site.county}, 空氣品質指標：{site.aqi}, 主要污染物：{site.pollutant}, 資料建立日期：{site.datacreationdate}")