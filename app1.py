from flask import Flask,render_template
from geo import show_geo
from pyecharts.commons.utils import JsCode
from pyecharts.charts import PictorialBar,Calendar,Page,Tree
from pyecharts.charts import Geo
from pyecharts.components import Image
from pyecharts.globals import ChartType
import datetime
from pyecharts import options as opts
from pyecharts.charts import Grid, PictorialBar

#绘图数据准备

app = Flask(__name__)

Baidu_index  = [{"date": "2021-07-22", "search_index": 67212, "news_index": 308609},
                {"date": "2021-07-23", "search_index": 340916, "news_index": 7525262},
                {"date": "2021-07-24", "search_index": 1214600, "news_index": 65411973},
                {"date": "2021-07-25", "search_index": 1050973, "news_index": 81867958},
                {"date": "2021-07-26", "search_index": 613263, "news_index": 85827011},
                {"date": "2021-07-27", "search_index": 346757, "news_index": 62905141},
                {"date": "2021-07-28", "search_index": 217668, "news_index": 41413095},
                {"date": "2021-07-29", "search_index": 151547, "news_index": 26295496},
                {"date": "2021-07-30", "search_index": 103230, "news_index": 14781083},
                {"date": "2021-07-31", "search_index": 74974, "news_index": 12034886},
                {"date": "2021-08-01", "search_index": 61666, "news_index": 13415477},
                {"date": "2021-08-02", "search_index": 59781, "news_index": 10173154},
                {"date": "2021-08-03", "search_index": 38506, "news_index": 5872987},
                {"date": "2021-08-04", "search_index": 31564, "news_index": 6033511},
                {"date": "2021-08-05", "search_index": 36328, "news_index": 3181309},
                {"date": "2021-08-06", "search_index": 25388, "news_index": 2369043},
                {"date": "2021-08-07", "search_index": 22190, "news_index": 1798590},
                {"date": "2021-08-08", "search_index": 21884, "news_index": 1261899},
                {"date": "2021-08-09", "search_index": 18232, "news_index": 1230029},
                {"date": "2021-08-10", "search_index": 17020, "news_index": 1485596},
                {"date": "2021-08-11", "search_index": 15934, "news_index": 1087679},
                {"date": "2021-08-12", "search_index": 13879, "news_index": 879184},
                {"date": "2021-08-13", "search_index": 13144, "news_index": 959142},
                {"date": "2021-08-14", "search_index": 13701, "news_index": 1470233},
                {"date": "2021-08-15", "search_index": 13305, "news_index": 951614},
                {"date": "2021-08-16", "search_index": 12632, "news_index": 1405281},
                {"date": "2021-08-17", "search_index": 11286, "news_index": 1179124},
                {"date": "2021-08-18", "search_index": 12958, "news_index": 1225821},
                {"date": "2021-08-19", "search_index": 12928, "news_index": 562049},
                {"date": "2021-08-20", "search_index": 10783, "news_index": 941884},
                {"date": "2021-08-21", "search_index": 18658, "news_index": 2669253},
                {"date": "2021-08-22", "search_index": 15133, "news_index": 5587886},
                {"date": "2021-08-23", "search_index": 11595, "news_index": 2059817},
                {"date": "2021-08-24", "search_index": 10179, "news_index": 1075092},
                {"date": "2021-08-25", "search_index": 10107, "news_index": 979452},
                {"date": "2021-08-26", "search_index": 9609, "news_index": 1288399},
                {"date": "2021-08-27", "search_index": 9663, "news_index": 1244091},
                {"date": "2021-08-28", "search_index": 9607, "news_index": 892604},
                {"date": "2021-08-29", "search_index": 9276, "news_index": 1224709},
                {"date": "2021-08-30", "search_index": 8264, "news_index": 511689},
                {"date": "2021-08-31", "search_index": 7556, "news_index": 734049},
                {"date": "2021-09-01", "search_index": 6525, "news_index": 877229},
                {"date": "2021-09-02", "search_index": 4469, "news_index": 253237},
                {"date": "2021-09-03", "search_index": 4329, "news_index": 336369},
                {"date": "2021-09-04", "search_index": 5333, "news_index": 350319},
                {"date": "2021-09-05", "search_index": 5113, "news_index": 407127},
                {"date": "2021-09-06", "search_index": 4620, "news_index": 411074},
                {"date": "2021-09-07", "search_index": 4354, "news_index": 5368160},
                {"date": "2021-09-08", "search_index": 4211, "news_index": 2996743},
                {"date": "2021-09-09", "search_index": 4204, "news_index": 791072},
                {"date": "2021-09-10", "search_index": 4138, "news_index": 685344},
                {"date": "2021-09-11", "search_index": 4475, "news_index": 645714},
                {"date": "2021-09-12", "search_index": 4216, "news_index": 668409},
                {"date": "2021-09-13", "search_index": 4785, "news_index": 387917},
                {"date": "2021-09-14", "search_index": 5097, "news_index": 149404},
                {"date": "2021-09-15", "search_index": 5267, "news_index": 677702},
                {"date": "2021-09-16", "search_index": 4933, "news_index": 503397},
                {"date": "2021-09-17", "search_index": 4549, "news_index": 161762},
                {"date": "2021-09-18", "search_index": 4570, "news_index": 254994},
                {"date": "2021-09-19", "search_index": 5109, "news_index": 905812},
                {"date": "2021-09-20", "search_index": 5547, "news_index": 246144},
                {"date": "2021-09-21", "search_index": 5442, "news_index": 285527},
                {"date": "2021-09-22", "search_index": 4634, "news_index": 578862},
                {"date": "2021-09-23", "search_index": 4328, "news_index": 455304},
                {"date": "2021-09-24", "search_index": 4529, "news_index": 1281211},
                {"date": "2021-09-25", "search_index": 4911, "news_index": 818767},
                {"date": "2021-09-26", "search_index": 4390, "news_index": 438664},
                {"date": "2021-09-27", "search_index": 4401, "news_index": 204809},
                {"date": "2021-09-28", "search_index": 4289, "news_index": 175907},
                {"date": "2021-09-29", "search_index": 3799, "news_index": 133667},
                {"date": "2021-09-30", "search_index": 3889, "news_index": 100987},
                {"date": "2021-10-01", "search_index": 4842, "news_index": 149014},
                {"date": "2021-10-02", "search_index": 4753, "news_index": 578947},
                {"date": "2021-10-03", "search_index": 4629, "news_index": 633439},
                {"date": "2021-10-04", "search_index": 4442, "news_index": 281562},
                {"date": "2021-10-05", "search_index": 4617, "news_index": 235697},
                {"date": "2021-10-06", "search_index": 4432, "news_index": 430429},
                {"date": "2021-10-07", "search_index": 4902, "news_index": 183709},
                {"date": "2021-10-08", "search_index": 4244, "news_index": 99782},
                {"date": "2021-10-09", "search_index": 4362, "news_index": 63692},
                {"date": "2021-10-10", "search_index": 5544, "news_index": 76409},
                {"date": "2021-10-11", "search_index": 12221, "news_index": 4308250},
                {"date": "2021-10-12", "search_index": 7305, "news_index": 1076409},
                {"date": "2021-10-13", "search_index": 5997, "news_index": 1076059},
                {"date": "2021-10-14", "search_index": 5289, "news_index": 4991201},
                {"date": "2021-10-15", "search_index": 4969, "news_index": 1293469},
                {"date": "2021-10-16", "search_index": 5394, "news_index": 1040704},
                {"date": "2021-10-17", "search_index": 5596, "news_index": 730764},
                {"date": "2021-10-18", "search_index": 4733, "news_index": 537159},
                {"date": "2021-10-19", "search_index": 5167, "news_index": 385599},
                {"date": "2021-10-20", "search_index": 5219, "news_index": 249564},
                {"date": "2021-10-21", "search_index": 4329, "news_index": 149527},
                {"date": "2021-10-22", "search_index": 4592, "news_index": 134882},
                {"date": "2021-10-23", "search_index": 4898, "news_index": 51229},
                {"date": "2021-10-24", "search_index": 4746, "news_index": 37552},
                {"date": "2021-10-25", "search_index": 4103, "news_index": 32404},
                {"date": "2021-10-26", "search_index": 4118, "news_index": 33687},
                {"date": "2021-10-27", "search_index": 4312, "news_index": 102944},
                {"date": "2021-10-28", "search_index": 4113, "news_index": 30064},
                {"date": "2021-10-29", "search_index": 3949, "news_index": 46072},
                {"date": "2021-10-30", "search_index": 4251, "news_index": 59232},
                {"date": "2021-10-31", "search_index": 4368, "news_index": 31144}]

Weibo_search = [
             {"date": "2021-07-22", "tag": "2",
              "trending_hashtag1": '#鸿星尔克的微博评论好心酸#',
              "trending_hashtag2": ' ',
              "trending_hashtag3": ' ',
              "trending_hashtag4": ' ',
              "trending_hashtag5": ' ',
              "trending_hashtag6": ' '},
             {"date": "2021-07-23", "tag": "1",
              "trending_hashtag1": '#鸿星尔克的会员被充到了2140年#',
              "trending_hashtag2": ' ',
              "trending_hashtag3": ' ',
              "trending_hashtag4": ' ',
              "trending_hashtag5": ' ',
              "trending_hashtag6": ' '},
             {"date": "2021-07-24", "tag": "1",
              "trending_hashtag1": '#鸿星尔克立志成为百年品牌#',
              "trending_hashtag2": '#鸿星尔克7月23日销量增长超52倍#',
              "trending_hashtag3": ' ',
              "trending_hashtag4": ' ',
              "trending_hashtag5": ' ',
              "trending_hashtag6": ' '},
             {"date": "2021-07-25", "tag": "1",
              "trending_hashtag1": '#男子在鸿星尔克买500付1000拔腿就跑#',
              "trending_hashtag2": '#什么是鸿星尔克式消费#',
              "trending_hashtag3": '#鸿星尔克门店货品几乎被扫空#',
              "trending_hashtag4": '#壹基金回应鸿星尔克2000万物资捐赠#',
              "trending_hashtag5": '#鸿星尔克董事长否认濒临破产#',
              "trending_hashtag6": '#郑州慈善总会回应鸿星尔克捐赠#'},
             {"date": "2021-07-26", "tag": "1",
              "trending_hashtag1": '#鸿星尔克董事长请求网友理性消费#',
              "trending_hashtag2": '#鸿星尔克门店深夜12点挤满顾客#',
              "trending_hashtag3": '#鸿星尔克库存告急#',
              "trending_hashtag4": '#顾客边剪鸿星尔克发型边抢服装#',
              "trending_hashtag5": '#雷军晒鸿星尔克鞋#',
              "trending_hashtag6": '#多地景区穿鸿星尔克等国货可享优惠#'},
             {"date": "2021-07-29", "tag": "1",
              "trending_hashtag1": "#鸿星尔克系统崩溃恳请退款#",
              "trending_hashtag2": ' ',
              "trending_hashtag3": ' ',
              "trending_hashtag4": ' ',
              "trending_hashtag5": ' ',
              "trending_hashtag6": ' '},
             {"date": "2021-08-01", "tag": "0",
              "trending_hashtag1": "#小心有人冒充鸿星尔克发红包# ",
              "trending_hashtag2": ' ',
              "trending_hashtag3": ' ',
              "trending_hashtag4": ' ',
              "trending_hashtag5": ' ',
              "trending_hashtag6": ' '},
             {"date": "2021-08-03", "tag": "1",
              "trending_hashtag1": "#扬州确诊病例曾去鸿星尔克专卖店#",
              "trending_hashtag2": ' ',
              "trending_hashtag3": ' ',
              "trending_hashtag4": ' ',
              "trending_hashtag5": ' ',
              "trending_hashtag6": ' '},
             {"date": "2021-08-21", "tag": "1",
              "trending_hashtag1": '#鸿星尔克向河南博物院捐赠一百万元#',
              "trending_hashtag2": '#鸿星尔克 携全国网友#',
              "trending_hashtag3": ' ',
              "trending_hashtag4": ' ',
              "trending_hashtag5": ' ',
              "trending_hashtag6": ' '},
             {"date": "2021-08-27", "tag": "1",
              "trending_hashtag1": "#鸿星尔克客服自动回复#",
              "trending_hashtag2": ' ',
              "trending_hashtag3": ' ',
              "trending_hashtag4": ' ',
              "trending_hashtag5": ' ',
              "trending_hashtag6": ' '},
             {"date": "2021-10-11", "tag": "1",
              "trending_hashtag1": "#鸿星尔克悄悄给山西捐物资#",
              "trending_hashtag2": ' ',
              "trending_hashtag3": ' ',
              "trending_hashtag4": ' ',
              "trending_hashtag5": ' ',
              "trending_hashtag6": ' '}]


pic0 = "M511.986835 0a511.986835 511.986835 0 0 1 386.915765 847.26507l114.392487 114.246205a36.570488 36.570488 0 0 1-46.663943 55.952847l-5.119869-4.169035-114.246205-114.319346A511.986835 511.986835 0 1 1 511.986835 0z m0 73.140976a438.845858 438.845858 0 1 0 0 877.691717A438.845858 438.845858 0 0 0 511.986835 73.140976z m-51.491248 146.281953c71.824439 50.028428 107.809799 125.290493 107.809799 225.786194 14.774477-8.99634 38.106449-42.421766 69.849633-100.495701 72.62899 67.143416 104.957301 158.05765 97.131216 272.742701C729.288675 705.225294 660.243594 804.55074 519.300932 804.55074c-140.942661 0-216.49729-97.277499-225.566771-187.094617-8.557494-84.258405 35.107669-169.979629 88.061736-242.023491l10.751723-14.18935C430.800351 311.361136 453.474054 264.038925 460.495587 219.422929z m21.284024 141.015803l-6.290124 10.166595-11.99512 17.553835-13.165375 17.700116C390.719096 483.461854 360.731295 553.384627 366.436292 610.068884 373.238402 677.578005 430.288364 731.409764 519.300932 731.409764c86.306352 0 138.455868-52.368939 143.06375-118.927228 3.364485-49.882146-2.047947-92.815899-16.237297-129.825233l-3.583908-8.26493-1.901665 2.413652c-9.215763 10.971146-18.285244 19.748064-27.501007 26.330751l-6.948393 4.681023-111.028002 67.143416V445.209123c0-27.647289-3.218203-52.149516-9.654609-73.872386l-3.73019-10.898005z"
pic1 = "M851.2 14.324h-678.4c-75.748 0-137.143 61.44-137.143 137.143v678.4c0 75.748 61.394 137.143 137.143 137.143h678.4c75.748 0 137.143-61.394 137.143-137.143v-678.4c0-75.703-61.394-137.143-137.143-137.143zM241.28 817.751l-64.412-27.794c34.423-44.663 50.468-73.189 68.068-125.075l55.588 18.286c-20.48 57.052-35.84 90.652-59.245 134.583zM359.817 557.273c0 43.154-13.898 57.052-103.863 73.235-2.24-17.6-11.749-47.588-25.645-65.828 66.56 5.075 75.292-5.897 75.292-25.645v-65.143c-39.452 10.285-68.754 19.017-101.668 32.138-2.926-19.017-10.285-47.498-17.6-65.097 40.274-5.897 80.503-12.388 119.269-20.435v-94.446c-49.006 0-84.846 2.195-112.686 5.852v-57.829c28.525 2.286 63.68 4.48 112.686 4.48 0-54.857-3.657-98.103-6.628-113.372 23.406 3.657 49.006 5.806 64.366 5.806 14.629 0 16.183 4.48 6.628 12.434-4.434 3.657-10.285 18.24-10.285 28.525v65.782c27.748-0.731 49.783-2.149 68.8-3.657v57.875c-18.971-2.24-40.914-4.388-68.754-5.12v81.188c24.137-5.852 48.32-12.434 71.68-19.017-2.88 16.822-2.88 43.885-0.731 57.052-27.109 5.852-50.468 10.331-70.994 15.36v95.863h0.137zM383.954 807.467c0.731-46.765-2.195-84.114-10.331-122.149l57.875-6.674c10.972 45.395 19.017 85.623 24.092 125.897l-71.634 2.926zM556.708 805.318c-3.657-49.828-9.554-81.188-23.452-125.897l61.486-7.314c13.942 49.006 21.897 80.548 32.96 126.674l-70.994 6.537zM754.24 810.439c-18.24-51.977-40.274-96.548-68.8-139.794l57.052-24.137c28.571 44.708 53.44 87.817 78.308 133.165l-66.56 30.766zM739.612 612.816c-33.646-22.674-49.006-54.812-56.32-109.028-6.628-51.155-4.48-109.715 1.418-177.829l-75.338 3.657c-4.388 46.811-13.165 88.549-27.063 127.268 25.645 19.017 51.977 40.32 75.338 59.337l-44.708 46.080c-17.555-19.794-35.154-37.257-53.394-54.172-24.914 46.765-60.023 88.595-107.612 128.092-16.091-13.988-35.795-26.332-60.709-35.154 60.023-32.228 101.76-73.92 128.092-128.092-19.017-14.583-37.303-28.571-57.052-40.96l35.154-38.858c12.388 8.777 26.332 19.017 40.96 29.989 8.092-27.748 13.165-58.468 16.137-91.475-27.109 2.195-64.366 5.852-87.040 10.331l-5.943-60.709c24.914 1.463 58.56 1.463 94.4 0 0.777-46.080 0-103.817-1.462-117.76 19.017 4.434 55.634 8.092 69.532 8.732 13.12 0.823 15.36 5.12 3.657 16.183-2.926 2.88-9.508 46.765-13.943 90.697 54.857-2.88 107.612-7.314 138.24-11.749-17.555 111.954-22.674 176.32-11.703 242.88 2.195 13.211 7.268 29.303 18.24 44.663 9.554 13.165 19.794 9.554 34.377-60.023 12.434 17.6 34.468 33.646 54.218 35.154-27.017 96.731-64.32 112.045-107.474 82.743z"
pic2 = "M377.410202 46.794574c-5.067254 33.455547-11.105792 67.216091-15.103509 101.226364-4.414274 37.647725-5.108194 75.517545 4.012045 112.721079 2.914874 11.882614 8.009762 23.280099 12.757691 34.621292 1.915956 4.566772 5.247387 8.662743 8.453953 12.5489 8.48261 10.300313 10.439506 10.828429 22.78064 5.969965 34.204735-13.506879 64.106755-34.052236 92.592278-56.777608 54.250634-43.311669 101.31029-93.730389 144.038574-148.05062 26.486665-33.635679 51.028715-68.75643 76.461195-103.211917 1.055209-1.444132 2.360147-2.720412 4.636369-5.330289 7.884898 11.06383 16.019524 21.32218 22.905505 32.34507 29.373904 46.907157 41.590174 98.950142 44.866336 153.380909 3.803255 63.427164-4.331372 125.700865-19.767512 187.155781-4.359006 17.394059-9.912413 34.496427-14.881414 51.737988-0.222095 0.749188-0.222095 1.554668-0.499459 3.553526 42.089632 7.330171 81.792507 1.665204 119.023675-18.87913 37.009073-20.406164 62.218433-51.765622 81.292025-90.191192 0.638652 2.567914 1.083866 3.733659 1.194402 4.955695 7.996457 86.59468 5.052926 172.66329-13.21621 257.925398-6.718129 31.205935-15.546676 61.801876-26.486665 91.814433-10.633968 29.151809-23.098943 57.499162-37.925088 84.735015-43.006671 79.043437-97.451766 149.285961-173.690865 198.594205-90.009012 58.22174-189.015446 80.153914-295.961022 57.693624-41.979096-8.801937-82.361562-22.323144-120.758475-40.952545C167.266015 912.830416 89.694343 812.907966 61.944703 675.171988c-9.925719-49.225342-4.83083-98.144663 5.733541-146.676085 11.41079-52.389945 30.165055-102.309207 53.916979-150.284879 24.627-49.724801 53.945636-96.687226 86.761507-141.525928 50.307161-68.743124 107.556594-131.280883 169.247934-189.973424C377.743857 46.585784 377.979258 46.571456 377.410202 46.794574L377.410202 46.794574 377.410202 46.794574zM290.343698 617.81202c-6.594288-46.975731-13.785265-88.122737-21.670163-123.354023l-31.497628 7.82963c10.494774 53.528056 17.047099 94.646405 19.698939 123.355047L290.343698 617.81202 290.343698 617.81202zM701.857771 788.170431c1.277304-1.277304 2.6109-4.552443 3.943472-9.77322 6.551302-11.771055 11.798689-20.876965 15.742161-27.430314-39.396854-11.744444-70.881176-30.651209-94.508235-56.777608l88.594562 0L715.629731 658.958002l-82.679865 0 0-31.345129 66.937704 0 0-33.288719-66.937704 0 0-29.373904 51.195543 0L684.145409 420.036599 406.506744 420.036599l0 80.279802-25.598283-15.659259c-13.132285 24.820438-24.945302 45.033164-35.440076 60.691399l0-140.984507-43.311669 0 0 88.122737c-1.319267 43.089573-1.971224 74.407068-1.971224 94.008776 1.29061 104.447259-19.68461 187.350243-63.009584 248.680294 17.047099 16.963174 27.569508 28.06999 31.497628 33.288719 31.511956-45.698426 51.196566-88.761389 59.067135-129.240062 14.437223 14.381955 26.250241 27.40268 35.454405 39.173735l7.870569-9.799831c3.942449 9.134568 7.870569 16.324522 11.813018 21.544275 27.569508-13.048359 51.196566-27.401657 70.881176-43.089573 5.233058 3.914815 13.104651 9.134568 23.627059 15.686893 6.552325 5.219753 11.132403 8.495916 13.784242 9.77322-47.254117 18.295746-85.346033 32.010392-114.20615 41.118349l17.726691 37.203534 120.106518-47.004388-15.75649-35.23231 17.726691-25.45909c-11.813018-6.497057-23.627059-13.715669-35.440076-21.545298 9.162202-7.828606 17.713386-16.936563 25.598283-27.40268l74.822601 0c7.884898 11.744444 16.380813 22.210561 25.598283 31.345129-10.550042 7.82963-21.654811 14.381955-33.483181 19.574074l21.655834 27.40268-21.655834 31.317495c41.979096 14.381955 79.404726 30.041214 112.220597 47.004388l19.713267-35.23231c-44.644241-16.963174-80.071012-30.679866-106.335581-41.118349 11.827346-7.857264 23.653669-15.686893 35.454405-23.516523C651.939533 764.043913 674.288264 776.425986 701.857771 788.170431L701.857771 788.170431zM453.760861 451.368423l185.074021 0L638.834882 478.784408 453.760861 478.784408 453.760861 451.368423 453.760861 451.368423zM459.674534 594.323131l-66.953056 0 0 33.288719 66.953056 0 0 31.345129L378.937236 658.956979l0 35.23231 78.766074 0c-15.75649 15.659259-38.091916 30.679866-66.953056 45.033164-15.742161-15.659259-33.469875-33.288719-53.154485-52.86177 3.942449-28.708642 5.913673-62.663647 5.913673-101.837382l0-1.94359 13.770937 7.801996c17.047099-24.76517 33.469875-49.585607 49.225342-74.379434l0 48.946955 53.167791 0L459.673511 594.323131 459.674534 594.323131zM587.637292 658.958002l-80.708641 0 0-31.345129 80.708641 0L587.637292 658.958002 587.637292 658.958002zM587.637292 594.323131l-80.708641 0 0-29.373904 80.708641 0L587.637292 594.323131 587.637292 594.323131zM453.760861 533.632755l0-29.388233 185.074021 0 0 29.388233L453.760861 533.632755 453.760861 533.632755zM569.92493 709.848548l-43.311669 0 0 101.837382c1.304938 14.353297-6.579959 20.850355-23.626035 19.574074-13.132285 0-23.627059-0.666286-31.497628-1.94359 1.29061 3.887181 2.609877 10.411872 3.92812 19.573051 2.623182 7.82963 3.942449 13.688035 3.942449 17.630484l39.382525 0c35.4411 0 52.488199-16.991831 51.183261-50.918179L569.925954 709.848548 569.92493 709.848548zM569.92493 709.848548"

data_search, data_news = [], []
twitter_data_tag_0, twitter_data_tag_1, twitter_data_tag_2 = [], [], []
for item in Baidu_index:
    temp_list = [datetime.datetime.strptime(item['date'], '%Y-%m-%d'), item['search_index'], item['news_index'],None]
    for twitter in Weibo_search:
        if twitter['date'] == item['date']:
            temp_list.insert(-1, twitter)
            temp_list.pop(-1)
            if twitter['tag'] == '0':
                twitter_data_tag_0.append(temp_list)
            elif twitter['tag'] == '1':
                twitter_data_tag_1.append(temp_list)
            elif twitter['tag'] == '2':
                twitter_data_tag_2.append(temp_list)
            break
    data_search.append(temp_list)
    data_news.append([datetime.datetime.strptime(item['date'], '%Y-%m-%d'), item['news_index']])

tooltips_js = """
        function(p){

            let backColorStr = `background-color:${p.data[1] > 20000 ? '#CACACA' : '#000'};`;
            let backColorStr1 = `background-color:${p.data[1] > 20000 ? '#CACACA' : '#000'};`;
            let date = p.data[0].split('T')[0];
            let resMsg = `${date}<br/>
            搜索指数：<span style='color:${p.color};${backColorStr}'>&nbsp&nbsp${p.data[1]}&nbsp&nbsp</span>，
            资讯指数：<span style='color:${p.color};${backColorStr1}'>&nbsp&nbsp${p.data[2]}&nbsp&nbsp</span>`;
            const msg = p.data[3];
            if (msg==null) {
                console.log(p);
                return resMsg;
            }
            const msgContent = `<div style='width:350px;height:130px;display:flex;'>
              <div style='width:270px;height:100px;white-space:normal;word-wrap:break-word;word-break:break-all;'>
                <span>${msg.trending_hashtag1}</span><br/>
                <span>${msg.trending_hashtag2}</span><br/>
                <span>${msg.trending_hashtag3}</span><br/>
                <span>${msg.trending_hashtag4}</span><br/>
                <span>${msg.trending_hashtag5}</span><br/>
                <span>${msg.trending_hashtag6}</span>
              </div>
            <div>`;
            return resMsg + '<br/>' + msgContent;
}
"""

data_good = [
    {
        "children": [
            {
                "children": [
                    {"name": "舒服"},
                    {"name": "质量"},
                    {"name": "喜欢"},
                    {"name": "鞋底"},
                    {"name": "舒适度"},
                    {"name": "轻便"},
                    {"name": "感觉"},
                    {"name": "跑步"},
                    {"name": "手感"},
                ],
                "name": "质量",
            },
            {
                "children": [
                    {"name": "支持"},
                    {"name": "国货"},
                    {"name": "国产"},
                    {"name": "周到"},
                    {"name": "爱"},
                ],
                "name": "情怀",
            },
            {
                "children": [
                    {"name": "便宜"},
                    {"name": "推荐"},
                    {"name": "实惠"},
                    {"name": "快递"},
                    {"name": "介绍"},
                    {"name": "特别"},
                    {"name": "好评"},
                ],
                "name": "性价比",
            },
        ],
        "name": "好评",
    }
]

data_bad = [
    {
        "children": [
            {
                "children": [
                    {"name": "臭脚"},
                    {"name": "味道"},
                    {"name": "一股"},
                    {"name": "做工"},
                    {"name": "换"},
                    {"name": "尺码"},
                    {"name": "款式"},
                    {"name": "晾"},
                ],
                "name": "质量",
            },
            {
                "children": [
                    {"name": "走路"},
                    {"name": "几天"},
                    {"name": "硌脚"},
                    {"name": "硬"},
                    {"name": "跑步"},
                    {"name": "紧"},
                    {"name": "挤脚"},
                    {"name": "换货"},
                ],
                "name": "舒适度",
            },
            {
                "children": [
                    {"name": "客服"},
                    {"name": "垃圾"},
                    {"name": "到货"},
                    {"name": "回复"},
                    {"name": "售后"},
                    {"name": "退货"},
                    {"name": "服务态度"},
                    {"name": "太慢"},
                    {"name": "烂"},
                    {"name": "无语"},
                ],
                "name": "服务",
            },
        ],
        "name": "差评",
    }
]


js_func_1 = 'const pic0 = "%s";' % pic0
js_func_2 = 'const pic1 = "%s";' % pic1
js_func_3 = 'const pic2 = "%s";' % pic2
js_func_4 = 'const picArr = [pic0, pic1, pic2];'

symbols = [
    'path://M959.868788 975.714146c0.599824 1.299619-227.733281 48.285854-447.968759 48.285854-220.035536 0-450.168115-45.786586-447.768817-48.285854 3.998828-29.991214 17.994728-77.27736 35.689544-101.770184 16.495167-23.093234 38.688665-41.187933 61.981841-56.383482 25.29259-15.895343 52.284682-27.991799 79.676657-39.38846 24.192912-9.997071 48.685737-19.494289 72.378795-30.391096 6.798008-3.099092 13.496046-6.398126 20.194084-9.79713 25.692473-14.09587 53.38436-32.090598 63.481402-61.681929 0.399883-3.399004 0.699795-6.798008 0.999707-10.296984 1.899444-21.693644 1.799473-43.48726 1.599532-65.280874-0.099971-8.49751-0.199941-17.094992-0.199942-25.592503-12.59631-9.597188-20.793908-23.693059-28.391682-37.588987-12.69628-24.492824-21.893586-50.885092-25.792444-78.277067-0.099971-0.799766-0.699795-1.499561-1.599531-1.699503-13.9959-3.199063-24.292883-15.195548-29.691301-28.291711-6.298155-14.895636-9.397247-30.89095-10.396954-46.886264-0.799766-15.39549 5.298448-30.990921 16.695109-41.087962 1.099678-0.999707 1.599531-2.499268 1.199648-3.898858-11.596603-48.185883-20.094113-97.671385-18.094699-147.4568 1.299619-31.290833 6.897979-62.981548 20.194084-91.27326 10.896808-23.193205 27.192034-43.887142 47.686029-58.882749C412.929025 9.397247 465.213707 0.799766 514.79918 0c27.991799 0.499854 57.283218 4.498682 81.576101 19.794201 8.997364 5.498389 16.295226 13.496046 22.093527 22.293469 23.593088 3.698916 47.286147 12.396368 65.180904 29.191447 25.892414 24.192912 37.788929 59.982427 41.287904 94.872206 5.898272 57.883042-5.198477 115.866055-21.193791 171.049888-0.399883 1.499561 0 3.099092 1.199649 4.098799 11.996485 10.596895 17.994728 27.292004 16.395196 43.487259-1.799473 19.194377-5.698331 39.188519-16.495167 55.683687-5.498389 8.297569-13.895929 14.395782-23.493117 16.795079-0.799766 0.199941-1.39959 0.799766-1.499561 1.699502-4.098799 28.991506-13.695988 57.083276-27.391975 82.87572-6.798008 12.296398-14.295812 24.492824-25.492532 33.090306 0 8.797423-0.199941 17.594845-0.199941 26.392268-0.199941 21.793615-0.299912 43.58723 1.699502 65.380845l0.899737 9.297277c8.197598 24.492824 29.291419 41.287904 50.085326 54.284096 10.596895 6.098213 21.393732 11.696573 32.490481 16.79508 23.493117 10.996778 47.786 20.394025 71.778971 30.291125 31.490774 12.996193 62.581666 26.992092 90.673436 46.786293 30.091184 20.693937 56.483452 48.685737 70.379381 83.375574 7.197891 17.094992 12.796251 49.685444 15.095577 68.180025z',
    'path://M959.9 976S832 1024 514 1024 64.1 976 64.1 976s0-125.7 63-187.2c12.5-12.2 27.5-21.9 45.5-27.5 5.1-1.6 10.2-3.2 15.2-4.8 102.8-32.6 197.8-65.3 197.8-97.9v-62.3c0-2.2-1.8-3.8-3.8-3.8-0.5 0-1 0.1-1.5 0.3-6.2 2.6-18.3 6-38.4 6-16.1 0-37.3-2.2-64.8-8.8l-25-7.9-59.9-18.9c-10.7-3.4-14.7-16.4-7.7-25.2 21.3-26.7 56.5-81.7 56.5-153.3C241 282 241 111 349.4 42.5 403.3 8.4 456.8 0 497.3 0c5.1 0 10.1 0.1 14.8 0.4 4.5-0.2 9.3-0.3 14.2-0.3 40.6 0 94.2 8.3 148.4 42.5 108.4 68.5 108.4 239.5 108.4 342.2 0 71.6 35.3 126.6 56.5 153.3 7 8.8 3 21.8-7.7 25.2l-60 18.9L747 590c-27.5 6.6-48.7 8.8-64.8 8.8-20.1 0-32.2-3.5-38.3-6-0.5-0.2-1-0.3-1.5-0.3-2 0-3.8 1.6-3.8 3.8v62.3c0 32.5 94.8 65.3 197.6 97.9 5.1 1.6 10.1 3.2 15.2 4.8 18 5.7 33 15.3 45.5 27.5 63 61.5 63 187.2 63 187.2z',
    'path://M653.724793 510.209254v-16.270211c59.759768-43.182572 98.644549-113.379834 98.644548-192.684321C752.369341 170.069751 646.050165 63.750575 514.865194 63.750575S277.361047 170.069751 277.361047 301.254722c0 79.304487 38.884781 149.501749 98.644549 192.684321v14.018986c-148.580793 57.610872-254.695313 206.805636-254.695313 381.275508 0 35.200959 35.507944 63.750575 79.304487 63.750574h622.668132c43.796542 0 79.304487-28.549615 79.304487-63.750574 0.102328-172.218647-103.249325-319.776157-248.862596-379.024283z'
]

img_src1=('https://s2.loli.net/2021/12/25/vFQq7xVD5KXN63e.png')

bar_sex = (
    PictorialBar()
        .add_xaxis(["男", "女"])
        .add_yaxis(
        "鸿星尔克",
        [
            {"value": 57.33, "symbol": symbols[0]},
            {"value": 42.67, "symbol": symbols[1]},
        ],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=30,
        symbol_repeat="fixed",
        symbol_offset=[0, 25],
        is_symbol_clip=True,
        # color= "#BF360C"
    )
        .add_yaxis(
        "全网分布",
        [
            {"value": 50.5, "symbol": symbols[0]},
            {"value": 49.5, "symbol": symbols[1]},
        ],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=30,
        symbol_repeat="fixed",
        symbol_offset=[0, -25],
        is_symbol_clip=True,
        # color= "#BF360C"
    )
        .reversal_axis()
        .set_global_opts(
        title_opts=opts.TitleOpts(title="性别分布"),
        legend_opts=opts.LegendOpts(pos_left="20%"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0),

            ),
        ),
    )
)

bar_age = (
    PictorialBar()
        .add_xaxis(["≥50", "40~49", "30~39", "20~29", "≤19"])
        .add_yaxis(
        "鸿星尔克",
        [
            {"value": 5.05, "symbol": symbols[2]},
            {"value": 14.29, "symbol": symbols[2]},
            {"value": 33.92, "symbol": symbols[2]},
            {"value": 32.72, "symbol": symbols[2]},
            {"value": 14.02, "symbol": symbols[2]},
        ],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=20,
        symbol_repeat="fixed",
        symbol_offset=[0, 15],
        is_symbol_clip=True,
    )
        .add_yaxis(
        "全网分布",
        [
            {"value": 8.19, "symbol": symbols[2]},
            {"value": 16.43, "symbol": symbols[2]},
            {"value": 35.13, "symbol": symbols[2]},
            {"value": 29.91, "symbol": symbols[2]},
            {"value": 10.34, "symbol": symbols[2]},
        ],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=20,
        symbol_repeat="fixed",
        symbol_offset=[0, -15],
        is_symbol_clip=True,
    )
        .reversal_axis()
        .set_global_opts(
        title_opts=opts.TitleOpts(title="年龄分布", pos_right="5%"),
        legend_opts=opts.LegendOpts(pos_right="20%"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
)

#绘图函数

def shuxing():
    grid = (
        Grid()
        .add(bar_sex, grid_opts=opts.GridOpts(pos_left="55%"))
        .add(bar_age, grid_opts=opts.GridOpts(pos_right="55%"))
        )
    html='shuxing.html'
    grid.render('./templates/'+html)
    return html

def calendar_chart():
    chart = Calendar(init_opts=opts.InitOpts(theme='macarons',
                                             width='1000px',
                                             height='550px'))

    chart.add_js_funcs(js_func_1)
    chart.add_js_funcs(js_func_2)
    chart.add_js_funcs(js_func_3)
    chart.add_js_funcs(js_func_4)
    chart.add('',
              yaxis_data=data_search,
              label_opts=opts.LabelOpts(is_show=True,
                                        position='inside',
                                        font_size=10,
                                        formatter=JsCode('function(params) {'
                                                         'if(params.data[3]==null) {return params.data[1];}'
                                                         'else{return ``}}')),
              tooltip_opts=opts.TooltipOpts(is_show=True,
                                            trigger='item',
                                            formatter=JsCode(tooltips_js)
                                            ),
              calendar_opts=opts.CalendarOpts(pos_left='25%',
                                              pos_right='2%',
                                              pos_top='20%',
                                              cell_size=50,
                                              range_=['2021-07-22', '2021-10-31'],
                                              yearlabel_opts=opts.CalendarYearLabelOpts(
                                                  margin=60,
                                                  label_color='rgba(130,134,112,0.8)'
                                              ),
                                              monthlabel_opts=opts.CalendarMonthLabelOpts(
                                                  name_map='cn',
                                                  label_font_weight='bold',
                                                  label_color='#778633'
                                              ),
                                              daylabel_opts=opts.CalendarDayLabelOpts(
                                                  name_map='cn',
                                                  label_font_weight='bold',
                                                  label_color='#778633'
                                              )
                                              ),
              )

    chart.add('',
              yaxis_data=data_news,
              label_opts=opts.LabelOpts(is_show=False),
              tooltip_opts=opts.TooltipOpts(is_show=False)
              )

    chart.add('普通词条',
              yaxis_data=twitter_data_tag_0,
              label_opts=opts.LabelOpts(is_show=False),
              tooltip_opts=opts.TooltipOpts(is_show=True,
                                            trigger='item',
                                            formatter=JsCode(tooltips_js)
                                            )
              )

    chart.add('词条标签：热、沸',
              yaxis_data=twitter_data_tag_1,
              label_opts=opts.LabelOpts(is_show=False),
              tooltip_opts=opts.TooltipOpts(is_show=True,
                                            trigger='item',
                                            formatter=JsCode(tooltips_js)
                                            )
              )

    chart.add('词条标签：爆',
              yaxis_data=twitter_data_tag_2,
              label_opts=opts.LabelOpts(is_show=False),
              tooltip_opts=opts.TooltipOpts(is_show=True,
                                            trigger='item',
                                            formatter=JsCode(tooltips_js)
                                            )
              )

    chart.set_global_opts(visualmap_opts=[opts.VisualMapOpts(is_show=True,
                                                             is_piecewise=True,
                                                             dimension=1,
                                                             series_index=0,
                                                             orient='vertical',
                                                             pos_left='2%',
                                                             pos_top='40%',
                                                             range_text=['搜索指数', ''],
                                                             pieces=[{'min': 500000},
                                                                     {'min': 20000, 'max': 500000},
                                                                     {'min': 5000, 'max': 20000},
                                                                     {'max': 5000}],
                                                             range_color=["#CCD3D9", "#E6B6C2", "#D4587A", "#BF360C"]),
                                          opts.VisualMapOpts(is_show=True,
                                                             is_piecewise=True,
                                                             dimension=1,
                                                             series_index=1,
                                                             orient='vertical',
                                                             pos_left='2%',
                                                             pos_top='65%',
                                                             range_text=['资讯指数', ''],
                                                             pieces=[{'min': 50000000},
                                                                     {'min': 10000000, 'max': 50000000},
                                                                     {'min': 1000000, 'max': 10000000},
                                                                     {'min': 500000, 'max': 1000000},
                                                                     {'max': 500000}],
                                                             range_color=["#000", "#8B0000", "#632A7E", "#A13E97",
                                                                          "#D3B7D8", "#FFF"][::-1]
                                                             )],

                          legend_opts=opts.LegendOpts(is_show=True,
                                                      pos_left='1%',
                                                      pos_top='10%',
                                                      orient='vertical',
                                                      item_width=40,
                                                      item_height=40
                                                      ),
                          title_opts=opts.TitleOpts(title='捐款100天内，鸿星尔克在各网络平台上拥有的热度',
                                                    subtitle='日历主色调代表每日百度搜索指数，右上角的小三角代表每日百度资讯指数。'
                                                             '鼠标移至热搜图标可查看当日微博热搜词条。')
                          )

    chart.options['series'][1]['type'] = 'scatter'
    chart.options['series'][1]['symbol'] = 'path://M0 0l10 0-0 10z'
    chart.options['series'][1]['symbolOffset'] = [19, -19]

    chart.options['series'][2]['type'] = 'scatter'
    chart.options['series'][2]['symbol'] = "path://" + pic0
    chart.options['series'][2]['symbolSize'] = 40
    chart.options['series'][2]['color'] = "#2c2c2c"
    chart.options['series'][3]['type'] = 'scatter'
    chart.options['series'][3]['symbol'] = "path://" + pic1
    chart.options['series'][3]['symbolSize'] = 40
    chart.options['series'][3]['color'] = "#2c2c2c"
    chart.options['series'][4]['type'] = 'scatter'
    chart.options['series'][4]['symbol'] = "path://" + pic2
    chart.options['series'][4]['symbolSize'] = 40
    chart.options['series'][4]['color'] = "#2c2c2c"

    html = 'chart.html'
    chart.render('./templates/' + html)
    return html


def bar_sex():
    c = (
        PictorialBar()
            .add_xaxis(["男", "女"])
            .add_yaxis(
            "鸿星尔克",
            [
                {"value": 57.33, "symbol": symbols[0]},
                {"value": 42.67, "symbol": symbols[1]},
            ],
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=30,
            symbol_repeat="fixed",
            symbol_offset=[0, 25],
            is_symbol_clip=True,
            # color= "#BF360C"
        )
            .add_yaxis(
            "全网分布",
            [
                {"value": 50.5, "symbol": symbols[0]},
                {"value": 49.5, "symbol": symbols[1]},
            ],
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=30,
            symbol_repeat="fixed",
            symbol_offset=[0, -25],
            is_symbol_clip=True,
            # color= "#BF360C"
        )
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="性别分布"),
            xaxis_opts=opts.AxisOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
            ),
        )
    )
    html = 'bar_sex.html'
    c.render('./templates/' + html)
    return html


def bar_age():
    c = (
        PictorialBar()
            .add_xaxis(["≥50", "40~49", "30~39", "20~29", "≤19"])
            .add_yaxis(
            "鸿星尔克",
            [
                {"value": 5.05, "symbol": symbols[2]},
                {"value": 14.29, "symbol": symbols[2]},
                {"value": 33.92, "symbol": symbols[2]},
                {"value": 32.72, "symbol": symbols[2]},
                {"value": 14.02, "symbol": symbols[2]},
            ],
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=20,
            symbol_repeat="fixed",
            symbol_offset=[0, 15],
            is_symbol_clip=True,
        )
            .add_yaxis(
            "全网分布",
            [
                {"value": 8.19, "symbol": symbols[2]},
                {"value": 16.43, "symbol": symbols[2]},
                {"value": 35.13, "symbol": symbols[2]},
                {"value": 29.91, "symbol": symbols[2]},
                {"value": 10.34, "symbol": symbols[2]},
            ],
            label_opts=opts.LabelOpts(is_show=False),
            symbol_size=20,
            symbol_repeat="fixed",
            symbol_offset=[0, -15],
            is_symbol_clip=True,
        )
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="年龄分布"),
            xaxis_opts=opts.AxisOpts(is_show=False),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(opacity=0)
                ),
            ),
        )
    )
    html = 'bar_age.html'
    c.render('./templates/' + html)
    return html


def geo():
    c = (
        Geo()
            .add_schema(maptype="china")
            .add(
            "搜索指数",
            [("北京", 100), ("上海", 78.72), ("深圳", 59.57), ("杭州", 55.32), ("广州", 55.32), ("成都", 53.19), ("郑州", 42.55),
             ("苏州", 38.30), ("重庆", 38.29), ("武汉", 31.91), ("长沙", 25.66), ("西安", 23.89), ("青岛", 19.88)],
            type_=ChartType.HEATMAP,
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="地域分布"),
            legend_opts=opts.LegendOpts(pos_left="20%"),
        )
    )
    html = 'geo.html'
    c.render('./templates/' + html)
    return html


def good_comment():
    c = (
        Tree()
            .add("", data_good, collapse_interval=2, layout="radial")
            .set_global_opts(title_opts=opts.TitleOpts(title="产品评价-好评"))
    )
    html = 'good_comment.html'
    c.render('./templates/' + html)
    return html


def bad_comment():
    c = (
        Tree()
            .add("", data_bad, collapse_interval=2, layout="radial")
            .set_global_opts(title_opts=opts.TitleOpts(title="产品评价-差评"))
    )
    html = 'bad_comment.html'
    c.render('./templates/' + html)
    return html


def image1():
    image1 = (
        Image()
            .add(
            src=img_src1,
            style_opts={"width": "1200px", "height": "700px", "style": "margin-top: 0px"},
        )
    )
    html = 'image1.html'
    image1.render('./templates/' + html)
    return html

img_src2=('https://s2.loli.net/2021/12/26/IV6TrH79fFjqtZO.png')
def image2():
    image2=(
        Image()
        .add(
        src=img_src2,
        style_opts={"width": "1200px", "height": "300px", "style": "margin-top: 150px"},
        )
    )
    html = 'image2.html'
    image2.render('./templates/' + html)
    return html

img_src3=('https://s2.loli.net/2021/12/26/Dnk5wEsYjZ7Fiau.png')
def image3():
    image3=(
        Image()
        .add(
        src=img_src3,
        style_opts={"width": "1000px", "height": "500px", "style": "margin-top: 20px"},
        )
    )
    html = 'image3.html'
    image3.render('./templates/' + html)
    return html

#设置生成图片的网关

@app.route("/geo")
def geo():
    show_geo()
    return render_template('geo.html')

@app.route("/chart")
def chart():
    calendar_chart()
    return render_template('chart.html')

@app.route("/bar_age")
def bar_age1():
    bar_age()
    return render_template('bar_age.html')

@app.route("/image1")
def image11():
    image1()
    return render_template('image1.html')

@app.route("/bar_sex")
def bar_sex1():
    bar_sex()
    return render_template('bar_sex.html')

@app.route("/bar_shuxing")
def bar_shuxing1():
    image3()
    return render_template('image3.html')

@app.route("/shouye")
def shouye():
    image2()
    return render_template('image2.html')

@app.route("/good_comment")
def good_comment1():
    good_comment()
    return render_template('good_comment.html')

@app.route("/bad_comment")
def bad_comment1():
    bad_comment()
    return render_template('bad_comment.html')



@app.route('/')
def wangye():  # put application's code here

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
