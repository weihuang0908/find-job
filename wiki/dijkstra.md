### dijkstra算法
关键词：有向图，权值非负，贪心
cut-and-paste: 最短路径的任意一段都是最短路径
时间复杂度 O( VlgV + E )
算法：优先队列Q, 集合S，距离数组d
```
Q = |V|
S = {s}
d[s] = 0, 其他均初始化为-INF
while Q:
    v = Extract-min(Q) # 贪心
    for neibor in v.neibors:
         if d[neibor] > d[v] + w(v, neibor): # 最短路径要么直达，要么通过某一段最短路径的终点转发
            d[neibor] = d[v] + w(v, neibor)
    S.add(v)
```

证明算法的正确性：
循环不变式
1、 初始化之后，任何情况下，delta(s, v) <= d[v]
2、 每当v加入S时， d[v] = delta(s,v)
第一条根据三角不等式可得，每次更新d[v]时，都存在一条可行路径，而所有边权非负，得证；
第二条反证法，假设u是第一个违反第二条的节点，即u已经完成了松弛，即将加入S,但delta(s, u) != d[u]
s到u的最短路径前半部分的节点在S内，后半部分不在，假设x是最短路径上的最后一个在S内的节点，y是路径上第一个不在S内的节点,即s—>x—>y—>u
最短路径的任意一段都是最短路径，这也是到y的最短路径，即delta(s, y) = delta(s, x) + w(x, y)
由于x没有违反第二条，即d[x] = delta(s, x), 故x松弛之后d[y] = delta(s, y) <= delta(s, u) <= d[u]
y, u都在Q里，但是Extract-min(Q)选出的是u而不是y, 矛盾
