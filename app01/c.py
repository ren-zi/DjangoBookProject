import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar,Timeline


tl = Timeline()
gdp = pd.read_csv('C:/Users/hp/Desktop/GDP.csv')

for year in range(1960,2020):
    year = str(year)
    gdp.sort_values(year, inplace = True, ascending = False)
    data = gdp[0:20][["Country Name", year]]    #GDP排序，取前20名
    data.sort_values(year, inplace = True, ascending = True)
    data[year] = data[year] / 10 ** 8           # GDP单位：亿美元
    print(data.head(10))

    # 设置GDP数据条颜色，中国为红色，其他国家为蓝色
    data["color"] = data["Country Name"].apply(lambda x: "red" if x == "中国" else "blue")

    country_list = list(data["Country Name"])
    GDP_list = list(data[year])
    color_list = list(data["color"])

    # 给各个国家的GDP数据条设置颜色
    y = []
    for rank in range(20):
        y.append(
            opts.BarItem(
                name=country_list[rank],
                value=GDP_list[rank],
                itemstyle_opts=opts.ItemStyleOpts(color=color_list[rank])
            )
        )

    # 创建某一年的世界GDP排名条形图
    bar = (
        Bar(init_opts=opts.InitOpts(width='720px', height='600px'))
            .add_xaxis(xaxis_data=country_list)
            .add_yaxis(series_name='亿美元', y_axis=y, label_opts=opts.LabelOpts(position="right", font_weight="bold"))
            .reversal_axis()
            .set_global_opts(
            legend_opts=opts.LegendOpts(pos_left="left", padding=[30, 30]),
            title_opts=opts.TitleOpts("世界各国GDP排名（{} 年）".format(year), pos_left=320, padding=[20, 20]),
            xaxis_opts=opts.AxisOpts(max_=250000)
        )
    )

    # 将某一年的世界GDP排名条形图加入时间线对象
    tl.add(bar, "{}年".format(year))
    tl.add_schema(play_interval=200, is_loop_play=False)

tl.render("gdp.html")