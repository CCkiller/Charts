#  使用import导入openpyxl模块
import openpyxl
#  使用from...import从pyecharts.charts导入Sankey
from pyecharts.charts import Sankey
#  使用from...import从pyecharts导入options，简写为opts
from pyecharts import options as opts

#  使用openpyxl.load_workbook()读取文件，路径为"/Users/taotao/song.xlsx"，赋值给wb
wb = openpyxl.load_workbook("/Users/song.xlsx")

#  使用中括号读取工作表年度歌单，赋值给sheet
sheet = wb["年度歌单"]

# 定义标签数据列表，赋值给变量list_labels
list_labels = []
# 定义信息流列表，赋值给变量links
links = []
#  通过for循环，读取sheet2-48行数据
for row in range(2,49):
    #  .value属性获取元组索引为0的单元格值，并用append()函数添加进list_labels
    list_labels.append(sheet[row][0].value)
    #  .value属性获取元组索引为1的单元格值，并用append()函数添加进list_labels
    list_labels.append(sheet[row][1].value)
    # 定义字典，赋值给变量dic
    dic = {}
    #  .value属性获取元组索引为0的单元格值，为dic创建（"source":"标签名1"）键：值对
    dic["source"] = sheet[row][0].value
    #  .value属性获取元组索引为1的单元格值，为dic创建（"target":"标签名2"）键：值对
    dic["target"] = sheet[row][1].value
    #  .value属性获取元组索引为2的单元格值，为dic创建（"value":值）键：值对
    dic["value"] = sheet[row][2].value
    #  使用append()函数将dic添加进links
    links.append(dic)

#  使用set()函数对list_labels去重
# 使用list()函数对去重后的结果转化为列表
# 赋值给变量list_nodes
link_nodes = list(set(list_labels))

# 定义节点列表，赋值给变量nodes
nodes = []
#  通过for循环遍历list_nodes
for cell in link_nodes:
    # 定义字典，赋值给变量dic
    dic = {}
    #  为dic创建（"name":"标签名"）键：值对
    dic["name"] = cell
    #  使用append()函数将dic添加进nodes
    nodes.append(dic)

#  使用Sankey()函数创建对象赋值给sankey
# 使用InitOpts()，传入参数theme="dark",bg_color="#253441"，赋值给init_opts
sankey = Sankey(init_opts = opts.InitOpts(theme = "dark",bg_color = "#253441"))

# 为创建的实例增加名字（sankey）、传入节点和信息流列表
sankey.add("sankey",
        nodes,
        links,
        #  使用LineStyleOpts()，传入参数opacity=0.3, curve=0.5, color="source"，赋值给linestyle_opt 
        linestyle_opt = opts.LineStyleOpts(opacity = 0.3,curve = 0.5,color = "source"),
        #  使用LabelOpts()，传入参数position="right",color="#FFFFFF",font_size=10，赋值给label_opts
        label_opts = opts.LabelOpts(position = "right",color = "#FFFFFF",font_size = 10)
        )

#  使用TitleOpts()，传入参数title="年度歌单"，赋值给title_opts
# 使用LegendOpts()，传入参数is_show=False，赋值给legend_opts 
# 调用set_global_opts()
sankey.set_global_opts(title_opts = opts.TitleOpts(title = "年度歌单"),
                      legend_opts = opts.LegendOpts(is_show = False))

#  使用render()生成桑基图保存到/Users/taotao/song.html
sankey.render("/Users/taotao/song.html")