# assignment-2026
### 概要  
ローレンツ方程式の数値的解法。半陰オイラー法を採用した。  
実行時にb, r, $\sigma$は可変である。  

### 動作環境  
Python 3.14  
使用ライブラリ: numpy, matplotlib

### 挙動  
Lorenz.pyを実行するとファイルが4つ追加される。  
calc.dat => 計算結果  
lorenz_x_y.pdf -> x,yのグラフ  
lorenz_y_z.pdf -> y,zのグラフ  
lorenz_3D.pdf -> x,y,zの三次元のグラフ　

### 数学的導出
微分方程式  

$$
\begin{aligned}
\dot{x} &= \sigma*(y-x) \\
\dot{y} &= r*x-y-x*z \\
\dot{x} &= x*y-b*z \\
\end{aligned}
$$

を導入する。  
ここで、  

$$
\begin{aligned}
x &= x_0 \cdot \tilde{x} \\
y &= y_0 \cdot \tilde{y} \\
z &= z_0 \cdot \tilde{z} \\
t &= t_0 \cdot \tilde{t}
\end{aligned}
$$

とおき、これを微分方程式に代入し整理すると

$$
\begin{aligned}
frac{d\tilde{x}}{d\tilde{t}} = /sigma*\t_0*\y_0/\x_0(\tilde{y}-(\x_0/\y_0)*\tilde{x} \\
\end{aligned}
$$
