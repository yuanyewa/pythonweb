import numpy as np
import pandas as pd
from plotly.offline.offline import _plot_html
def plot1(row, col, mini, maxi): # pandas
    return (
    pd.DataFrame(np.random.randint(mini, maxi+1, (row, col))).style
    .applymap(lambda value: 'background-color: ' + ('green' if value == mini else 'red' if value == maxi else 'while'))
    .applymap(lambda value: 'color: ' + ('red' if value == mini else 'blue' if value == maxi else 'green'))
    .set_properties(**{'border-color': 'black', 'border-style':'solid', 'border-width':' 1px'})
    .render()
    )

def plot2(mini, maxi, len): # plotly
    try:
        data = [{'x': list(range(len)), 'y': np.random.randint(mini, maxi, len)}]
        plot_html, plotdivid, width, height = _plot_html(data, '', False, '80%', 525, False, False)
        return plot_html
    except:
        return '<h1><font color="red">plot failed!</font></h1>'

if __name__ == "__main__":
    print(plot1(10, 10, 0, 5))
    print(plot2(0, 10, 100))

