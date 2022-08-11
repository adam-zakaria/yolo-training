import json

import os
import shutil
import json

"""
Get some image samples by difficulty to show Nick 
"""
def get_difficult_and_nondifficult_images(): 
    with open('/Users/azakaria/Downloads/nightowls_validation.json', 'r') as f:
        j = json.loads(f.read())
        d = []
        nd = []
        for a in j['annotations']:
            if a['difficult'] == True:
                d.append(a)
            else:
                nd.append(a)

        s1 = 0
        ids = []
        for a in d[0:5]:
            for i in j['images']:
                if a['id'] == i['id']:
                    ids.append(i)
        s2 = 0
        inds = []
        for a in nd[0:5]:
            for i in j['images']:
                if a['id'] == i['id']:
                    inds.append(i)

get_difficult_and_nondifficult_images()