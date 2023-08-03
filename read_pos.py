import os
import glob
import numpy as np
import pandas as pd
import struct

File = 'YOUR_DATA.pos'
def read_epos(file):
    with open(file, 'rb') as in_file:
        file_size = os.path.getsize(file)
        n_row = int(file_size/16)
        data = np.zeros((n_row,4))
        for i in range(0,n_row):
            a = in_file.read(4*4)
            data[i,0:4] = np.asarray(struct.unpack('>4f',a))
    print("# of atoms =",n_row)
    return data

data = read_epos(File)
df = pd.DataFrame(data, columns=['x','y','z','m/n'])
store = pd.HDFStore('store_epos.h5')
store['data'] = df

cnt = 0
with open('fake_hit', 'w+') as out_file:
    for i in data:
        cnt += 1
        out_file.write("%s %s %s %s %s %s %s %s %s %s %s %s\n" %(cnt, cnt, 1, cnt, 0.0, 0.0, 0.0, 0.0, i[0], i[1], 10, 0.0))
