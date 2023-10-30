import numpy as np
import math


a = 6378137.0  # WGS84椭球长半轴
e2 = 6.69437999014e-3  # WGS84椭球第一偏心率的平方


def D2R(array: np.ndarray) -> np.ndarray:
    """deg -> rad

    Args:
        array (np.ndarray): ndarray of deg

    Returns:
        np.ndarray: ndarray of rad
    """
    return array * math.pi / 180


def R2D(array: np.ndarray) -> np.ndarray:
    """rad -> deg

    Args:
        array (np.ndarray): ndarray of rad

    Returns:
        np.ndarray: ndarray of deg
    """
    return array * 180 / math.pi


def PosD2R(array: np.ndarray) -> np.ndarray:
    """coordinate (deg,deg,~) -> (rad,rad,~)

    Args:
        array (np.ndarray): coordinate

    Returns:
        np.ndarray: coordinate
    """
    array[:, 0] = D2R(array[:, 0])
    array[:, 0] = D2R(array[:, 0])
    return array


def PosR2D(array: np.ndarray) -> np.ndarray:
    """coordinate (rad,rad,~) -> (deg,deg,~)

    Args:
        array (np.ndarray): coordinate

    Returns:
        np.ndarray: coordinate
    """
    array[:, 0] = R2D(array[:, 0])
    array[:, 0] = R2D(array[:, 0])
    return array


def blh2xyz(array: np.ndarray) -> np.ndarray:
    """ blh(rad,rad,m) -> xyz(m,m,m)

    Args:
        array (np.ndarray): coordinate

    Returns:
        np.ndarray: coordinate
    """
    cosB = np.cos(array[:, 0])
    sinB = np.sin(array[:, 0])
    cosL = np.cos(array[:, 1])
    sinL = np.sin(array[:, 1])

    h = array[:, 2]
    N = a / np.sqrt(1 - e2 * sinB ** 2)  # 卯酉圈曲率半径

    array[:, 0] = (N + h) * cosB * cosL
    array[:, 1] = (N + h) * cosB * sinL
    array[:, 2] = (N * (1 - e2) + h) * sinB
    return array
