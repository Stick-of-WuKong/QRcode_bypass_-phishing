'''
Author: your name
Date: 2025-03-17 17:41:49
LastEditTime: 2025-03-21 09:58:40
LastEditors: StickWK
Description: In User Settings Edit
FilePath: \邮件钓鱼\qrcode_table.py
'''
from xml.etree import ElementTree as ET
#使用 Python 标准库 xml.etree.ElementTree 解析 SVG 文件，无需额外安装依赖
#假设 SVG 文件中的方块是通过 <use> 元素引用的 <rect> 元素
def svg_to_table(svg_file, output_file):
    # 解析 SVG 文件
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # 获取 SVG 的宽度和高度
    #width = int(root.attrib['width'])
    #height = int(root.attrib['height'])
    width = 300
    height = 300

    # 获取方块的大小（假设所有方块大小相同）
    #block_size = int(root.find('rect').attrib['width'])
    block_size = 12
    # 计算表格的行数和列数
    rows = height // block_size
    cols = width // block_size

    # 初始化表格数据
    table = [[0 for _ in range(cols)] for _ in range(rows)]

    # 提取所有 <use> 元素的位置信息
    for use in root.findall('.//{http://www.w3.org/2000/svg}use'):
        x = int(float(use.attrib['x']))
        y = int(float(use.attrib['y']))
        # 计算表格中的行和列
        row = y // block_size
        col = x // block_size
        # 标记该位置为黑色方块
        table[row][col] = 1

    # 生成 HTML 表格
    html = ['<table border="0" cellspacing="0" cellpadding="0" width="{}" height="{}">'.format(width, height)]
    for row in table:
        html.append('<tr height="{}">'.format(block_size))
        for cell in row:
            if cell == 1:
                html.append('<td width="{}" bgcolor="#000000"></td>'.format(block_size))
            else:
                html.append('<td width="{}"></td>'.format(block_size))
        html.append('</tr>')
    html.append('</table>')

    # 将 HTML 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html))

    print(f"HTML 表格已生成并保存到 {output_file}")

# 示例用法
svg_file = 'qrcode.svg'  # 输入的 SVG 文件路径
output_file = 'qrcode_table.html'  # 输出的 HTML 文件路径
svg_to_table(svg_file, output_file)