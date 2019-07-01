# Weather

Django example for climate service management

## To RUN

git clone https://github.com/danielstp/Clima.git
cd Clima
python3 -m venv venv
source venv/bin/activate
pip install django
createdb clima
../manage.py migrate
../manage.py runserver


## URLs examples

http://localhost:8000/prom/55/44
http://localhost:8000/prom/55/44/noaa,weatherdotcom,accuweather