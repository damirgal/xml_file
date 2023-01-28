# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from datetime import datetime
tree = ET.parse('DESADV_7b250f28-99a7-11ed-b355-d80e624df92e.xml')
root = tree.getroot()

d = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
d = d + '<invoice>'
d = d + '<comments>EDI Korus.message number: '+str(root[0][0].text)+' DESADV info: DESADV D 01B UN EAN007</comments>'
d = d + '<confirmed>1</confirmed>'
d = d + '<createDate>'+datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+'</createDate>'
d = d + '<currency>RUR</currency>'
d = d + '<date>'+str(root[2][0][1].text[:4])+'-'+str(root[2][0][1].text[4:6])+'-'+str(root[2][0][1].text[6:])+'T00:00:00'+'</date>'
d = d + '<doctype>9</doctype>'


n = 44;
m = 2
while m <= n:

    d = d+ '<invoiceItemSet>'
    d = d+ '\t<description>'+ root[13][m][4][1][0].text +'</description>'
    d = d+ '\t<grprice>0</grprice>'
    #print('\t\t<invoiceLotSet>') - добавить серии
    d = d+ '\t<itemIdSupplier>'+root[13][m][2][1][0].text+'</itemIdSupplier>'
    if float(root[13][7][10][0][1].text) == 0:
        pr = float(root[13][7][11][0][1].text) / float(root[13][7][5][0][1].text)
    else:
        pr = root[13][7][10][0][1].text
        
    #print('\t<price>'+root[13][m][10][0][1].text+'</price>')
    d = d+ '\t<price>'+str(pr)+'</price>'
    d = d+ '\t<qty>'+root[13][m][5][0][1].text+'</qty>'
    d = d+ '\t<sum>' +root[13][m][11][0][1].text+'</sum>'
    d = d+ '\t<sumNds>'+root[13][m][13][0][1].text+'</sumNds>'
    d = d+ '\t<tax>'+root[13][m][8][1][0].text+'</tax>'
    d = d+ '</invoiceItemSet>\n'
    m = m + 1;
    itemqty = m-1;
    
    
d = d+ '<itemqty>'+str(itemqty)+'</itemqty>'
d = d+ '<number>'+str(root[1][1][0].text)+'</number>'
d = d+ '<paymentterm>Предоплата</paymentterm>'
d = d+ '<shipdate>'+str(root[3][0][1].text[:4])+'-'+str(root[3][0][1].text[4:6])+'-'+str(root[3][0][1].text[6:])+'T00:00:00'+'</shipdate>'
d = d+ '<sum>'+str(root[5][0][1].text)+'</sum>'
d = d+ '<sumnds>'+str(root[4][0][1].text)+'</sumnds>'
d = d+ '<supplier>2002520638</supplier>'
d = d+ '<torg>'+str(root[1][1][0].text)+'</torg>'
d = d+ '</invoice>'

#print(d)

my_file = open("nakl.xml", "w", encoding="utf-8")
my_file.write(d)
my_file.close()

