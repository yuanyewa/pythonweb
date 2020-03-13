https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3
brew install python3
sudo pip3 install virtualenv
virtualenv -p python3 tmp
source tmp/bin/activate
pip install flask
pip install pandas
pip install plotly==3.7.0
python web_main.py
