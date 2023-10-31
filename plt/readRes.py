import numpy as np
import yaml
import re
import terminalMsg as terminalMsg
import os


class PltConfig:
    def __init__(self) -> None:

        # 容错处理
        tragetFile = "pltSettings.yaml"
        curDir = os.path.dirname(os.path.abspath(__file__))
        targetPath = os.path.join(curDir, tragetFile)

        if not os.path.isfile(targetPath):
            terminalMsg.printErrors("请在配置文件目录plt下运行脚本文件")

        terminalMsg.printSuccess("正在读取配置文件:" + targetPath)
        # 读取配置
        with open(targetPath, mode="r", encoding="utf-8") as f:
            _settings = yaml.safe_load(f.read())

        # 分隔符
        delimiter = _settings["delimiter"]
        delimiter.append(" ")
        self.splitPattern = "|".join(map(re.escape, delimiter))

        # 文件路径
        self.resfilePath = _settings["resfilepath"]
        self.reffilePath = _settings["reffilepath"]

        # 全局作图参数
        self.fontName = _settings["fontName"]
        self.fontSize = _settings["fontSize"]
        self.dpi = _settings["dpi"]

        # 作图参数
        self.SingleAxesSinglePlotConfig = _settings["SingleAxesSinglePlotConfig"]
        self.SingleAxesMulPlotConfig = _settings["SingleAxesMulPlotConfig"]
        self.MulAxesConfig = _settings["MulAxesConfig"]


def _readFile(path: str, splitPattern: str) -> np.ndarray:
    # 读取文件
    with open(path, "r") as f:
        data = f.readlines()
        # 预处理确定文件列数
        fstLine = [s for s in re.split(
            splitPattern, data[0]) if not s == "" and not s == "\n"]
        res = np.zeros((len(data), len(fstLine)))
        index = 0
        # 读取结果文件
        for line in data:
            valuesStrList = [
                s for s in re.split(splitPattern, line) if not s == "" and not s == "\n"]
            res[index, :] = np.array([float(value) for value in valuesStrList])
            index += 1
    return res


def readFile(config: PltConfig) -> (np.ndarray, np.ndarray):
    spiltPattern = config.splitPattern
    return _readFile(config.resfilePath, spiltPattern), _readFile(config.reffilePath, spiltPattern)
