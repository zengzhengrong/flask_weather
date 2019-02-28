import requests

def get_citys_weather(citys,single=None,byid=None):
    data = []
    citys_id = []
    city_code_url = 'https://cdn.huyahaha.com/tianqiapi/city.json'
    if single:
        city = []
        city.append(citys)
        citys = city
    # mapping city id
    city_code_repson = requests.get(city_code_url).json()
    for city in city_code_repson:
        if city['cityZh'] in citys:
            citys_id.append(city['id'])
    # by id
    if byid:
        citys = citys_id
    for name in citys:
        url = f'https://www.tianqiapi.com/api/?version=v1&city={name}'
        if byid:
            url = f'https://www.tianqiapi.com/api/?version=v1&cityid={name}'
        respon = requests.get(url).json()
        weather = {
            'name':respon['city'],
            'description':respon['data'][0]['wea'],
            'temp':respon['data'][0]['tem'],
            'icon':respon['data'][0]['wea_img']
        }
        data.append(weather)
    # print(data)
    return data

def make_cookies_respon(respon,name,cookies=None):
    split_tag = ','
    name_list = []
    if cookies:
        name_list.append(cookies)
    name_list.append(name)
    citys = split_tag.join(name_list)
    respon.set_cookie('citys', citys)
    return respon
