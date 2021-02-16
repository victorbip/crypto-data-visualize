import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def sanitize_response(obj, key, multiple: bool):
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

    def __init__(self, x: list, y: list):
        self.x_axis = x
        self.y_axis = y


    def plot_graph(self):
        pass
