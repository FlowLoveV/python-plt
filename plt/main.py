import matplotlib
from readRes import *
from resPlt import *
from dataProcess import *

# 设置字体为仿宋
matplotlib.rc("font",family='YouYuan')

def main():
    # 读取配置文件
    config = PltConfig()
    # 读取文件
    (res, ref) = readFile(config)
    # 处理数据
    data = process_vdr_test(res=res, ref=ref)
    # 作图
    x = np.array(range(0, np.shape(res)[0]))
    create_single_plot_axes(config.SingleAxesConfig[0], x=x, y=norm2(data[0]))
    create_single_plot_axes(config.SingleAxesConfig[1], x=x, y=norm2(data[1]))
    create_single_plot_axes(config.SingleAxesConfig[2], x=x, y=data[2])
    plt.show()
    print("done")


if __name__ == "__main__":
    main()
