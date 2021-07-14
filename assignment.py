a=[]
S=""
for i in range(1,99):
    for j in range(i+1,100):
        for k in range(j+1,101):
            if (i*i +j*j)<k*k:
                break
            if (i*i +j*j)==k*k:
                s=str(i)+","+str(j)+","+str(k)
                a.append(s)
                break
print(a)