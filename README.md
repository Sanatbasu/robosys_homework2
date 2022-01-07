# 2021年ロボットシステム学課題2
## 動作環境
|  CPU |  Raspberry Pi 4 8GB  |
| ---- | ---- |
|  OS  |  Ubuntu20.4  |
|  ミドルウェア|  ROS  |
## インストール方法
  以下の順番でコマンドを実行しクローンします      
 `$ git clone https://github.com/Sanatbasu/robosys_homework2.git`   
  `$ cd ~/robosys_homework2/scripts`     
 ## 動作方法
 以下のコマンドでビルドし,`$ roscore`を起動します    
 `$ catkin_make`     
`$ roscore`    
新しいターミナルを２つ開きそれぞれのコマンドを実行します    
`$ rosrun mypkg pub.py`    
`$ rosrun mypkg sub.py`    
pub.pyで実行したターミナルから数字を入力するとsub.pyで掛け算した値がだされます
## 実行動画
https://www.youtube.com/watch?v=Fzon_MO8D_Y
## ライセンス
[BSD 3-Clause License](https://github.com/Sanatbasu/robosys_homework2/blob/add-license-1/LICENSE)
## 参考
https://ryuichiueda.github.io/robosys2020/lesson10_ros.html#/
