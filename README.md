# robosys_ROS1
課題②

## 使用したもの
・Raspberry Pi3 ModelB  
・Ubuntu 20.04  
・ROS Noetic

## 内容
count.pyにより0.5s毎に1~6の乱数を生成。 
omikuji.pyにより7を入力し生成された乱数との差分により表示されるおみくじの内容が変化。
なお7以外を入力した場合　(´・ω・`)  obey the rule.　と表示される。

## 使用方法
1.ubuntu20.04にROS Noetic のインストール、セットアップ。  
2.ワークスペースの作成、このリポジトリのclone  
3.端末1でroscore,端末2でrosrun mypkg count.py 端末3でrosrun mypkg omikuji.py  
  （必要であればrostopic echo/count_up でcount.py による乱数を確認）

## 動画


## ROSのインストールの際参考にしたもの
https://ryuichiueda.github.io/robosys2020/lesson10_ros.html   
https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server
