import io
with io.open('জাল(net).txt','r',encoding='utf8') as f:
    text = f.read()
# process Unicode text
with io.open('test2.txt','w',encoding='utf8') as f:
    f.write(text)