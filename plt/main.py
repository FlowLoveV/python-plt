import matplotlib
from readRes import *
from resPlt import *
from dataProcess import *


# 读取配置文件
config = PltConfig()
# 设置字体
matplotlib.rc("font", family=config.fontName)
plt.rcParams['font.size'] = config.fontSize
plt.rcParams['axes.unicode_minus'] = False


def main():
    # 读取文件
    (res, ref) = readFile(config)
    ################################################## data process and plot from here ################################################
    # 处理数据
    data = process_vdr_test(res=res, ref=ref)
    # 作图
    x = np.array(range(0, np.shape(res)[0]))
    create_single_axes_mul_plot(
        config.SingleAxesMulPlotConfig[0], x=x, y=data[0])
    # create_single_axes_single_plot(config.SingleAxesSinglePlotConfig[0], x=x, y=norm2(data[0]))
    # create_single_axes_single_plot(config.SingleAxesSinglePlotConfig[1], x=x, y=norm2(data[1]))
    # create_single_axes_single_plot(config.SingleAxesSinglePlotConfig[2], x=x, y=data[2])
    ############################################################ done #################################################################
    plt.show()
    print("done")


if __name__ == "__main__":
    main()
