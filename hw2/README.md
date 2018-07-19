執行：./decision_stump_algorithm
畫圖：python draw.py
我是用C++先寫主程式並把 E_in E_out 分別輸出成檔案 data1 以及 data2 再用draw.py畫圖的
TUPLE_2 是記錄一組(x,y)的結構
H 是每個DATA的(s,theta)

一開始先Generate_Data 並製作 Noise 然後再將DATA按照x座標排序
接下來算error_rate_min並用min_h記錄最好的(s,theta)
接下來用min_h 計算 e_out
重複上述步驟1000次然後取平均
