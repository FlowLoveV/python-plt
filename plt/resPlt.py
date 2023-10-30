import matplotlib.pyplot as plt
import numpy as np
from readRes import PltConfig
from terminalMsg import *


# 此文件用于定义作图函数

def create_single_plot_axes(axesSet: dict, x: np.ndarray, y: np.ndarray):
    plt.figure()
    # 验证
    if not axesSet["type"] == "plot":
        printErrors("传入作图参数为非plot类型")
    # 必备参数
    plt.title(axesSet["title"])
    plt.xlabel(axesSet["xlabel"])
    plt.ylabel(axesSet["ylabel"])
    plt.plot(x, y, linestyle=axesSet["linestyle"], linewidth=axesSet["linewidth"],
             color=axesSet["color"], marker=axesSet["marker"], markersize=axesSet["markersize"])
    # 保存图片
    plt.savefig(axesSet["figname"])
    return
