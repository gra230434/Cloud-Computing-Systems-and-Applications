# CPU, Memory, Disk I/O 負載
Main.py 是程式最主要主程式，會讀取使用者的參數並呼叫 CPUload.py MEMload.py IOload.py<br>
程式如果使用者沒有規定最長執行時間，執行時間為 1200 sec

不可以中斷程式，因為中斷程式不會關閉子程式，必須等待子程式結束，系統資源才會返回給使用者

## 程式架構

* main.py
* CPUload.py 作 CPU 負載程式
  > utils 資料夾為 CPU 負載控制程式
  
* MEMload.py 作 Memory 負載程式
* IOload.py  作 Disk I/O 寫入負載程式

## 使用方式

程式碼無須編譯，直接使用 python 2.7 呼叫即可

    python main.py -l 20 -m 20 -i 20 -d 20

代表系統會形成
CPU 平均20%的系統負載，記憶體使用 20%，硬碟寫入 20%，持續時間 20 秒
同時也可以寫成下面這個樣式

    python main.py --load=20 --mem=20 --io=20 --time=20
