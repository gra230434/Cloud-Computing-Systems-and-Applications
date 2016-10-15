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

## 事情準備

安裝 psutil

    sudo apt-get install python-pip
    sudo apt-get build-dep python-lxml
    sudo pip psutil

## 使用方式

程式碼無須編譯，直接使用 python 2.7 呼叫即可<br>
-l CPU     的平均負載比率，20 代表 20%<br>
-m Memory  的平均負載比率，20 代表 20%<br>
-i Disk I/O的平均負載比率，20 代表 20%<br>
-d 執行程式時間，20 代表 20 sec，預設為 1200 sec<br>

    python main.py -l 20 -m 20 -i 20 -d 40

代表系統會形成<br>
CPU 平均20%的系統負載，記憶體使用 20%，硬碟寫入 20%，持續時間 20 秒<br>
同時也可以寫成下面這個樣式

    python main.py --load=20 --mem=20 --io=20 --time=40

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

    python main.py --load=40 --mem=60 --io=30 --time=90

    ![Alt text](https://github.com/gra230434/Cloud-Computing-Systems-and-Applications/blob/master/Lab1/Lab1-2/workload/img/cpuandram.PNG)
    ![Alt text](https://github.com/gra230434/Cloud-Computing-Systems-and-Applications/blob/master/Lab1/Lab1-2/workload/img/io.PNG)

## 提醒

記憶體:<br>
程式裡面拿到的記憶體跟 top 的記憶體量不同<br>
所以程式跑出來的百分比會在 top 中顯示比預計的較少<br>
4 GB 記憶體大概會少 0.5% 在負載 20%，會少 2% 在負載 60%<br>
8 GB 記憶體大概會少 1.0% 在負載 20%，會少 5% 在負載 60%<br>

因為程式是先做記憶體負載然後做硬碟寫入負載，前後大概需要 10-15 秒左右的時間<br>
所以在設置程式運行時間不要低過20秒較好<br>
程式大概會在20秒左右開始穩定，負載的量也會開始收斂到使用者寫入的參數數值<br>
個人認為 40 秒會是一個好的最短時間，在記憶體 4 GB 的情況下<br>
個人認為 80 秒會是一個好的最短時間，在記憶體 8 GB 的情況下<br>
