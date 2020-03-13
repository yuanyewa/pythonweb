from flask import Flask, render_template, request
import plotter
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def plot_main():
    try:
        if request.method == 'POST':
            para = {'row':request.form.get('row'), 'col':request.form.get('col'),\
                    'mini':request.form.get('mini'), 'maxi':request.form.get('maxi'),\
                    'len':request.form.get('len')}
        else:
            para={'row': '5', 'col': '5', 'mini': '0', 'maxi': '9', 'len': '100'}
        html1 = plotter.plot1(int(para['row']), int(para['col']), int(para['mini']), int(para['maxi']))
        html2 = plotter.plot2(int(para['mini']), int(para['maxi']), int(para['len']))
        return render_template('index.html', para=para, html1=html1, html2=html2)
    except:
        return render_template('index.html', para = para, html1='wrong config!', html2='')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
