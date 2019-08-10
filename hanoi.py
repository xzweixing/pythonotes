#汉诺塔：count代表需要多少步，n代表汉诺塔第一根有几个盘子，src参数代表源（即汉诺塔第一根柱子），dst代表目标（即汉诺塔第一根柱子）,mid代表中间的（即汉诺塔中间的柱子）
count=0
def hanoi(n,src,dst,mid):
    global count
    if n==1:
        print("{}:{}->{}".format(1,src,dst))
        count +=1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count +=1
        hanoi(n-1,mid,dst,src)
hanoi(1,"A","C","B")
print(count)
