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
\dot{x} &= \sigma (y-x) \\
\dot{y} &= r x-y-x z \\
\dot{z} &= x y-b z \\
\end{aligned}
$$

を導入する。  
ここで、  

$$
\begin{aligned}
x &= x_0 \tilde{x} \\
y &= y_0 \tilde{y} \\
z &= z_0 \tilde{z} \\
t &= t_0 \tilde{t} \\
\end{aligned}
$$

とおき、これを微分方程式に代入し整理すると

$$
\begin{aligned}
\frac{d\tilde{x}}{d\tilde{t}} &= \sigma \frac{t_0 y_0}{x_0} \left( \tilde{y} - \frac{x_0}{y_0} \tilde{x} \right) \\
\frac{d\tilde{y}}{d\tilde{t}} &= \frac{x_0 t_0}{y_0} \left( r\tilde{x} - \frac{y_0}{x_0} \tilde{y} - z_0 \tilde{x} \tilde{z} \right) \\
\frac{d\tilde{z}}{d\tilde{t}} &= \frac{x_0 y_0 t_0}{z_0} \left( \tilde{x} \tilde{y} - \frac{b z_0}{x_0 y_0} \tilde{z} \right) \\
\end{aligned}
$$

となる。

$$
\begin{aligned}
x_o &= y_0 &= z_0 &= t_0 &= 1 \\
\end{aligned}
$$

と単位系を設定し代入すると

$$
\begin{aligned}
\frac{d\tilde{x}}{d\tilde{t}} &= \sigma t_0 (\tilde{y} - \tilde{x}) \\
\frac{d\tilde{y}}{d\tilde{t}} &= r\tilde{x} - \tilde{y} - \tilde{x} \tilde{z} \\
\frac{d\tilde{z}}{d\tilde{t}} &= \tilde{x} \tilde{y} - b\tilde{z} \\
\end{aligned}
$$

と導かれる。  
ここで半陰オイラー法を用いて離散化を行う。　

$$
\begin{aligned}
\tilde{x}(\tilde{t}+\delta \tilde[t}) = \tilde{x}(\tilde{t})
\end{aligned}
$$
