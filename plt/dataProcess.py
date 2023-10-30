# 作图时，不可避免的需要对结果文件和参考文件进行一定的计算
# 在此文件中定义你所需要进行的运算

from coordinateTrans import *


def norm2(array: np.ndarray) -> np.ndarray:
    """ calculate norm of the row of array

    Args:
        array (np.ndarray): R * C size

    Returns:
        np.ndarray: R * 1 size
    """
    return np.linalg.norm(array, axis=1).reshape(-1, 1)


def formatDiffYaw(array: np.ndarray) -> np.ndarray:
    return [i + 360 if abs(i + 360) < 10.0 else i - 360 if abs(i - 360) < 10.0 else i for i in array]


def process_vdr_test(res: np.ndarray, ref: np.ndarray) -> list[np.ndarray]:
    # 位置之差
    resPos = blh2xyz(res[:, 43:46])
    refPos = blh2xyz(ref[:, 1:4])
    dXYZ = refPos - resPos

    # 速度之差
    resVel = res[:, 49:52]
    refVel = ref[:, 5:8]
    dV_eun = refVel - resVel

    # 姿态误差-航向角
    resYaw = R2D(res[:, 48])
    refYaw = ref[:, 4]
    dYaw = formatDiffYaw(refYaw - resYaw)
    np.savetxt("YAW.txt", dYaw, delimiter=" , ")
    return [dXYZ, dV_eun, dYaw]
