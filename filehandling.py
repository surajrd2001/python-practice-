list=['suraj\n','gaurav\n','PB\n','saurabh\n']
with open('data.txt','r') as f:
    #  f.write('suraj')
    #  f.writelines(list)
    print(f.read(10))
    f.seek(16)
    print(f.read(10))
    
    
    