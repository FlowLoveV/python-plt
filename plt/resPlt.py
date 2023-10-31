import matplotlib.pyplot as plt
import numpy as np
from readRes import PltConfig
from terminalMsg import *
from main import config


# 此文件用于定义作图函数

def create_single_axes_single_plot(axesSet: dict, x: np.ndarray, y: np.ndarray):
    """单个坐标区,单个plot

    Args:
        axesSet (dict): 作图配置
        x (np.ndarray): x轴数据
        y (np.ndarray): y轴数据
    """
    # 检查
    if not axesSet["type"] == "plot":
        printErrors("传入作图参数为非plot类型")
    # 必备参数
    plt.figure()
    plt.title(axesSet["title"])
    plt.xlabel(axesSet["xlabel"])
    plt.ylabel(axesSet["ylabel"])
    plt.plot(x, y, linestyle=axesSet["linestyle"], linewidth=axesSet["linewidth"],
             color=axesSet["color"], marker=axesSet["marker"], markersize=axesSet["markersize"])
    # 保存图片
    plt.savefig(axesSet["figname"], dpi=config.dpi)
    return


def create_single_axes_mul_plot(axesSet: dict, x: np.ndarray, y: np.ndarray):
    # 检查
    if not np.shape(y)[1] == axesSet["num"]:
        printErrors(f"作图配置为{axesSet['num']}个plot，但y有{np.shape(y)[1]}列")
    if not axesSet["type"] == "plot":
        printErrors("传入作图参数为非plot类型")
    # 作图
    plt.figure()
    plt.title(axesSet["title"])
    plt.xlabel(axesSet["xlabel"])
    plt.ylabel(axesSet["ylabel"])
    for i in range(np.shape(y)[1]):
        plt.plot(x, y[:, i], linestyle=axesSet["linestyle"][i], linewidth=axesSet["linewidth"][i],
                 color=axesSet["color"][i], marker=axesSet["marker"][i], markersize=axesSet["markersize"][i], label=axesSet["legend"][i])
    plt.legend()
    plt.savefig(axesSet["figname"], dpi=config.dpi)
    return


def create_mul_plot_axes(axesSet: dict, x: np.ndarray, y: np.ndarray):
    return
