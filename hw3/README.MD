Q15(作業的Q7):
執行：在command line 輸入 python Q15.py 
np.linalg.pinv 是算psuedo inverse 用的
add_noise(n,f) 是加10%的noise
preprocess_data(X1,X2,n) 是在串接 X1 x2 並加上第0維
make_Data(n) 就是在生 training data 跟 testing data 用的
trans(X) 是把 (1,x1,x2)轉成(1,x1,x2,x1x2,x1^2,x2^2)

Q8_0.01:
執行：在command line 輸入 python Q8_0.01.py
會出現 eta = 0.01 的兩條 Ein 曲線
藍色曲線是GD 黑色曲線是SGD

Q8_0.001:
執行：在command line 輸入 python Q8_0.001.py
會出現 eta = 0.001 的兩條 Ein 曲線
藍色曲線是GD 黑色曲線是SGD

Q9_0.01:
執行：在command line 輸入 python Q9_0.01.py
會出現 eta = 0.01 的兩條 Eout 曲線
藍色曲線是GD 黑色曲線是SGD

Q9_0.001:
執行：在command line 輸入 python Q9_0.001.py
會出現 eta = 0.01 的兩條 Eout 曲線
藍色曲線是GD 黑色曲線是SGD

get_Data(filename)是在讀取資料
do_logistic_regression(X, Y, eta, T, type) 是在進行logistic regression的過程
	type == 0 時是用 GD
	type == 1 時是用 SGD
cal_E_in(X, Y, w) 是在算錯誤率
h(x)是 theta(s)






