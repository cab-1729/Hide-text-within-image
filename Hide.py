import random
import shutil
from PIL import Image
def ranget(how_many,within):
    ss=list(range(1,within))
    random.shuffle(ss)
    en=random.randint(how_many-1,within-1)
    rnd=ss[en-how_many:en]
    rnd.sort()
    return rnd
def b5(n):
    f=''
    while True:
        t=divmod(n,5)
        r=t[1]
        q=t[0]
        f=str(r)+f
        n=q
        if q==0:
            break
    while len(f)!=3:
        f='0'+f
    return f
typable='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-+=|\\{[]}:;’‘”“\"\'>.<,?/~` \n'
loc_original=input('Enter the path of the original image : ')
loc_new=input('Enter the path of the new image : ')
loc_info=input('Enter the path of the information to be hidden : ')
shutil.copy(loc_original,loc_new)
original=Image.open(loc_original)
hide=Image.open(loc_new)
f=open(loc_info,'r')
message=f.read()
f.close()
chars=[typable.index(c)+1 for c in message]
shrinked=list(map(b5, chars))
width=original.size[0]
height=original.size[1]
rand_nums=ranget(len(chars),width*height)
for dif,stash in list(zip(shrinked,rand_nums)):
    r=divmod(stash,width)
    pixel=(r[1],r[0])
    o_color=original.getpixel(pixel)
    rv=o_color[0]-(int(dif[0]) if o_color[0]>int(dif[0]) else (-1*int(dif[0])))
    gv=o_color[1]-(int(dif[1]) if o_color[1]>int(dif[1]) else (-1*int(dif[1])))
    bv=o_color[2]-(int(dif[2]) if o_color[2]>int(dif[2]) else (-1*int(dif[2])))
    hide.putpixel(pixel,(rv,gv,bv))
print("Done")
hide.save(loc_new)
