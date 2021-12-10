

#Data Preparation for YOLO
"""

#mounting drive - for working directory

#going to the directory

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/EagleView/assignment/Custom_data_2C/

"""# creating free text files for each image with same name"""

#to print all the files inside image dataset
import os
lists = os.listdir()
lists

#removing jupyter notebook from list
lists.remove('Data_prep.ipynb')

#number of images
len(lists)

#replace .jpg by .txt

text_list = []
for x in lists:
  k=x.replace('.jpg','.txt')
  text_list.append(k)

text_list

#making text file using this names

for i in text_list:
  f= open(i,"w+")

"""# Filling annotated object(instance) description into text files for each images

Annotated bounding box descriptions are in the form of COCO.
"""

#loading the annotated json file

import json
s=open('/content/drive/MyDrive/EagleView/assignment/bbox-annotations.json')
data=json.load(s)

#images key from data
img_inf = data['images']
print('number of images :', len(img_inf))

#annotations key from data
ann_inf = data['annotations']
print('number of instances from all frames :', len(ann_inf))

#first 10 from img_inf
img_inf[:10]

#first 10 from ann_inf
ann_inf[:10]

"""# Filling the text files : """

for i in range(len(ann_inf)):
  bbox1 = ann_inf[i]['bbox']
  category_id = ann_inf[i]['category_id']
  image_id = ann_inf[i]['image_id']

  #adding lines to text files
  img_name = 'image_00000000'+str((image_id)+1)+'.txt'
  #print(img_name)
  
  for j in range(len(img_inf)):
    if img_inf[j]['id']==image_id:
      W = img_inf[j]['width']
      H = img_inf[j]['height']
  
  bbox=[0,0,0,0]         #initialize
  #filling by COCO > YOLO conversion, sharing pics files for better understanding
  bbox[0]= ((2*bbox1[0])+(bbox1[2]))/(2*W)
  #bbox[0] = format(bbox[0], '.2f')

  bbox[1]= ((2*bbox1[1])+(bbox1[3]))/(2*H) 
  #bbox[1] = format(bbox[1], '.2f')

  bbox[2]= bbox1[2]/W
  #bbox[2] = format(bbox[2], '.2f')

  bbox[3]= bbox1[3]/H
  #bbox[3] = format(bbox[3], '.2f')

  bbox = [bbox[0],bbox[1],bbox[2],bbox[3]]

  with open(img_name, "a+") as obj:
    
    obj.seek(0)
    # if empty, go with first line. else new line
    data = obj.read(100)
    if len(data) > 0 :
        obj.write("\n")        
    obj.write(str(category_id-1)+' '+str(bbox)[1:])  # bcz initial symbol '[' removal  problem

#look at one text file, how look like

with open('image_000000001.txt') as f:
    contents = f.read()
    print(contents)

"""Here, we can see symbel ',' and ']' needs to remove.

format

[class_index Xc Yc w h]

where Xc, Yc are the centre point of objects and w,h are width and height of objects with respect to entire frame. 
"""

#delete unwanted for yolo format

import re

lists1=os.listdir()
#print(lists1)

for list in lists1:
    if list.endswith('.txt'):
        with open(list, 'r+') as f:
            text1 = f.read()
            text1 = re.sub(',', '', text1)    #subst by empty
            f.seek(0)
            f.write(text1)
            f.truncate()

#same for ']' 

lists1=os.listdir()
#print(lists1)

for list in lists1:
    if list.endswith('.txt'):
        with open(list, 'r+') as f:
            text1 = f.read()
            text1 = re.sub(']', '', text1)
            f.seek(0)
            f.write(text1)
            f.truncate()

#let's check now, how text files look like,

with open('image_000000001.txt') as f:
    contents = f.read()
    print(contents)

"""Yeah, everything is fine. 

