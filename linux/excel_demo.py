import xlsxwriter

workbook=xlsxwriter.Workbook('demo.xlsx')

#添加新的工作表
worksheet1=workbook.add_worksheet()
worksheet2=workbook.add_worksheet('Foglio2')
worksheet3=workbook.add_worksheet('Data')
worksheet4=workbook.add_worksheet()

#设置格式
bold=workbook.add_format()
bold.set_bold()

#创建图表对象
chart=workbook.add_chart({'type':'line'})

#关闭工作表
# workbook.close()

worksheet1.write_string(0,0,'your text here')
worksheet1.write_number('A2',2.3451)
worksheet1.write_blank('A2',None)
worksheet1.write_formula(2,0,'=SUM(B1:B5)')
worksheet1.write_url('A1','http://www.baidu.com')
worksheet1.write_boolean(0,0,True)

#设置行单元格的属性
worksheet2.write('A1','hello')
worksheet2.write('B1','world')
cell_format=workbook.add_format({'bold':True})
worksheet2.set_row(0,40,cell_format)
worksheet2.set_row(1,None,None,{'hidden':True})

worksheet2.set_column(0,1,10,cell_format)
worksheet2.set_column('C:D',20)
worksheet2.set_column('E:G',None,None,{'hidden':1})

#插入图片到单元格
worksheet2.insert_image('B5','img/python-logo.png',{'url':'http://python.org'})


