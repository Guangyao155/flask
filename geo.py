from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
def show_geo():
    c = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "搜索指数",
            [("北京", 100), ("上海", 78.72), ("深圳", 59.57), ("杭州", 55.32), ("广州", 55.32), ("成都", 53.19), ("郑州", 42.55), ("苏州", 38.30), ("重庆", 38.29), ("武汉", 31.91), ("长沙", 25.66), ("西安", 23.89), ("青岛", 19.88)],
            type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="地域分布"),
        )
    )
    html='geo.html'
    c.render('./templates/'+html)
    return html
