import xml.etree.ElementTree as ET
import os
i = 0
for z in os.listdir('./Images'):
    temp = z.split('.')
    if temp[1] == 'xml':    
        with open(f'./Images/{z}', 'r') as f:
            tree = ET.parse(f)
            root = tree.getroot()
            for child in root.findall('object'):
                for inner_child in child:
                    if inner_child.tag == 'name':
                        if inner_child.text != 'head' and inner_child.text != 'head_with_helmet':
                            root.remove(child)
                        elif inner_child.text == 'head':
                            inner_child.text = 'NoHelmet'
                        elif  inner_child.text == 'head_with_helmet':
                            inner_child.text = 'Helmet' 
            tree.write(f'./Images/{z}') 
                  
#     print(child)

# for child in root.iter('object'):  
#     print(child.tag, child[0].text)

# print('********************************************')


# for child in root.findall('object'):  
#     root.remove(child)

# for child in root.iter('object'):  
#     print(child.tag, child[0].text)

