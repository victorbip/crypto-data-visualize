import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()


def sanitize_response(obj, key, multiple: bool):
    # Get an X and Y axis for the key (prices, total_volumes, market_caps) for coins.
    # Multiple flag is used to see if there's multiple coins given

    # Creating response dictionary and x and y list
    response = dict()
    x = list()
    y = list()

    if multiple:
        for c in obj:
            response[c] = {}
            for arr in obj[c][key]:
                x.append(arr[0])
                y.append(arr[1])
            response[c]["x_axis"] = x
            response[c]["y_axis"] = y
    else:
        for arr in obj[key]:
            x.append(arr[0])
            y.append(arr[1])
        response["x_axis"] = x
        response["y_axis"] = y
    return response


class PlotArray:
    # Plot a graph from an array/list (x and y axis are lists)

    def __init__(self, x: list, y: list):
        self.x_axis = x
        self.y_axis = y

    def line_graph_price(self, coin: str, multiple: bool):
        # Plot a line graph for the price overtime
        if multiple:
            pass
        else:
            plt.plot(self.x_axis, self.y_axis)
            plt.xlabel('Timeframe (YYYY-MM)')
            plt.ylabel(f'{coin} price')
            plt.title(f'Coin price graph')
            plt.legend([coin])
        plt.show()
