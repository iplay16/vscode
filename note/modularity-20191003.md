#### 社团检测
社团检测，就是要在一个图（包含顶点和边）上发现社团结构，也就是要把图中的结点进行聚类，构成一个个的社团。关于社团（community），目前还没有确切的定义，一般认为社团内部的点之间的连接相对稠密，而不同社团的点之间的连接相对稀疏。  
![社团](./scrn20170308230905.png)

#### 模块度
Modularity，中文称为模块度，是 Community Detection（社区发现/社团检测） 中用来衡量社区划分质量的一种方法。要理解Modularity，我们先来看社团和社团检测的概念。

##### 算法
$e：k*k的矩阵$  
$e_{ii}：社团i内部边占总边数的比例$  
$e_{ij}：社团i和社团j连接的边占总边数的比例乘\frac{1}{2}$  
可得矩阵e： 
$\left[             
\begin{array}{l}  
\frac{5}{23} & \frac{1}{23}×\frac{1}{2} & 0 \\         
\frac{1}{23}×\frac{1}{2} & \frac{7}{23} & \frac{2}{23}×\frac{1}{2}  \\
0 & \frac{2}{23}×\frac{1}{2} & \frac{8}{23} 
\end{array}           
\right] \\$  

> 推论1：矩阵e的迹tr(e)=$\sum e_{ii}$为社团内部的边的比例。这个值越大，代表社团内部联系越紧密。然而这样有一个缺陷，如果把整张图分成1个社团，这个值就是最大值1 。  

> 推论2：e的行和a，$a_i=\sum e_{ij}$它表示连接到 社团i中的边占总边数的比例。

$a_i=\frac{k_{c_i}}{2m}$,$k_{c_i}$是表示社团i的所有点的度数之和。   
$e_i$表示社团i内部的边数，则$e_{ii}=\frac{e_i}{m}$

modularity(模块度)的定义：  
$Q=\sum_{i}(e_{ii}-a_i^2)$
把$e_i$和$a_i$带入可得计算modularity最常用的公式：
$$Q=\sum_i({\frac{e_i}{m}}-({\frac{k_{c_i}}{2m}})^2)$$

还可以推导一下，得到矩阵公式:
$Q=\sum_{i}(e_{ii}-a_i^2)=\sum_i e_{ii}-\sum_i a_i^2=Tre-||e^2||$其中Tre是矩阵e的迹，$e^2=
\left[             
\begin{array}{l}  
\frac{5}{23} & \frac{1}{23}×\frac{1}{2} & 0 \\         
\frac{1}{23}×\frac{1}{2} & \frac{7}{23} & \frac{2}{23}×\frac{1}{2}  \\
0 & \frac{2}{23}×\frac{1}{2} & \frac{8}{23} 
\end{array}           
\right] \\×
\left[             
\begin{array}{l}  
\frac{5}{23} & \frac{1}{23}×\frac{1}{2} & 0 \\         
\frac{1}{23}×\frac{1}{2} & \frac{7}{23} & \frac{2}{23}×\frac{1}{2}  \\
0 & \frac{2}{23}×\frac{1}{2} & \frac{8}{23} 
\end{array}           
\right] \\$，其中$||e^2||$是指$e^2$的所有元素之和


#### 模块度的论文表示形式
G=(V,E),V是点集，E是边集
$A_{ij}表示顶点i到顶点j的边的权值\\$
$\overline V_1$表示$V_1$的补集
$V_i为V的子集，V_1和V_2是V的两个不相交的子集\\$
$L(V_1,V_1)=\sum_{i\in V_1,j\in V_1}A_{ij}    表示V_1内部的所有边的权值和\\$
$L(V_1,V_2)=\sum_{i\in V_1,j\in V_2}A_{ij}   表示V_1到V2之间的所有边的权值和$
$L(V_1,\overline V_1)=\sum_{i\in V_1,j\in \overline V_1}A_{ij}   表示V_1到\overline V_1之间的所有边的权值和$  
在这里，我们可以理解$V_i$就是社团,这样，我们刚才的公式也可以写成
$$Q=\sum_{i=1}^m[\frac{L(V_i,V_i)}{L(V_i,V_i)}-(\frac{L(V_i,V)}{L(V,V)})^2]$$

#### 模块度公式改进版
以上定义有不足之处，就是不包含社区顶点的数量，这会导致区分度会完全取决于社区内部的连接数，于是我们引入测量方法D来克服这个问题。  
$d_{in}(G_i)$表示子图$G_i$平均内部的度  
$d_{out}(G_i)$表示子图$G_i$平均外部的度  
$d(G_i)=\frac {L(V_i,V_i)-L(V_i,\overline {V_i})} {|V_i|}$  
$$D=\sum_i^m d(G_i)=\sum_{i=1}^2 \frac {L(V_i,V_i)-L(V_i,\overline {V_i})} {|V_i|}$$

${\{C_C\}}_{c=1}^k$表示 $C_i$的集合，i从1到k  
$Q_D^g{\{C_C\}}$表示多社区的多层网络的模块度  
$|V_c|$表示顶点数
