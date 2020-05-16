import xml.etree.ElementTree as et
import pandas as pd 

xtree = et.parse("cd_catalog.xml")
xroot = xtree.getroot()

def print_subtree(subtree):
    for y in subtree:
        print ("\t", y.tag, ":", y.text)

for node in xroot:
    #print (node.tag, node.attrib)
    print_subtree(node.getchildren())
"""
tags = {"tags":[]}
for node in xroot:
    tag = {}
    tag["TITLE"] = node.tag['TITLE']
    tag["ARTIST"] = node.tag['ARTIST']
    tag["COUNTRY"] = node.attrib['COUNTRY']
    tags["tags"]. append(attrib)

df_users = pd.DataFrame(tags["tags"])
df_users.head()

"""
