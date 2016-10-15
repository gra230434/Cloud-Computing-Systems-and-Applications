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

程式碼無須編譯，直接使用 python 2.7 呼叫即可<br>
-l CPU     的平均負載比率，20 代表 20%<br>
-m Memory  的平均負載比率，20 代表 20%<br>
-i Disk I/O的平均負載比率，20 代表 20%<br>
-d 執行程式時間，20 代表 20 sec

    python main.py -l 20 -m 20 -i 20 -d 20

代表系統會形成<br>
CPU 平均20%的系統負載，記憶體使用 20%，硬碟寫入 20%，持續時間 20 秒<br>
同時也可以寫成下面這個樣式

    python main.py --load=20 --mem=20 --io=20 --time=20

如果要操控 CPU 負載量，可以用下指令<br>
-l 代表 CPU core 的比率<br>
-d 不設定，預設是 20 秒<br>
-c 代表要在哪一個core上執行，假設是一顆四核心的處理器，只能填入 0-3

    python CPUload.py -l 0.20 -d 20 -c 0

如果要操控 Memory 負載量，可以用下指令<br>
-m 代表 Memory 的使用率<br>
-d 不設定，預設是 20 秒

    python MEMload.py -m 0.20 -d 20

如果要操控 Disl I/O 負載量，可以用下指令<br>
-i 代表 Disl I/O 的寫入使用率<br>
-d 不設定，預設是 20 秒

    python IOload.py -i 0.20 -d 20

## 使用結果
