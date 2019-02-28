from flask import Flask,request,render_template,make_response,jsonify,url_for,redirect,flash
import requests
from utils import get_citys_weather,make_cookies_respon
app = Flask(__name__)
app.config['SECRET_KEY'] = 'zzr'
@app.route('/',methods=['GET','POST'])
def weather():
    data = []
    if request.method == 'GET':
        cookies = request.cookies.get('citys')
        if cookies:
            get_name_list = cookies.split(',')
            data = get_citys_weather(get_name_list,byid=True)
    if request.method == 'POST':
        name = request.form.get('city').strip()
        cookies = request.cookies.get('citys')
        # print(cookies)
        if not name:
            return redirect(url_for('weather'))
        # cookies not exist
        if not cookies:
            data = get_citys_weather(name,single=True,byid=True)
            respon = make_response(render_template('weather.html',citys=data))
            cookies_respon = make_cookies_respon(respon,name)
            return cookies_respon
        if name in cookies:
            return redirect(url_for('weather'))
        # check single city weather when the request is POST
        data = get_citys_weather(name,single=True,byid=True)
        respon = make_response(render_template('weather.html',citys=data))
        cookies_respon = make_cookies_respon(respon,name,cookies=cookies)
        return cookies_respon
    return render_template('weather.html',citys=data)
if __name__ == "__main__":
    app.run(debug=True)