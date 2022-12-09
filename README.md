# ความคืบหน้าของโปรเจค

## **คำสั่งเพิ่มเติม** 
* cd + enter : ออกไป main base ของ dev 
* cd เป็นการเรียกใช้ folder 
* ls เป็นการเช็คไฟล์ภายในโฟลเดอร์
* rm -rf [ชื่อโฟลเดอร์ที่ต้องการลบข้อมูลออก]: ใช้ลบ Data Folder 
* pwd /home/supidchaya/prj/corenet ใช้เพื่อบอกว่า ทำงานอยู่ตรงไหนของโฟลเดอร์
* wget --no-check-certificate [link] 
> **ตัวอย่างเช่น** 
wget https://shapenet.cs.standford.edu/shapenet/obj-zip/ShapeNetCore.v2.zip 
--2022-12-09 10:10:02-- https://shapenet.cs.standford.edu 

# Screen ใช้เพื่อทำให้สามารถโหลดในอีกหน้าได้
## Install Screen Package

* sudo apt install screen

## สร้าง Screen 
* screen -S [ชื่อ Screen]
> **ตัวอย่างเช่น** 
screen -S loadData

## Open Screen
* screen -R

## ออกจาก Screen
* ctrl + a + d (พร้อมกัน)

# Nvidia driver + cuda + cudnn
## Install nvidia driver 
link: https://docs.google.com/document/d/1MQ35ZeMZupJQCz4pUmI2Z0j6yD5VaVRWYBtosGNK0p8/edit?fbclid=IwAR27aDKO4-YIc1EomyCkIiKYhQesJuA1HQ2q9j3Z6R2C5T-c26CSMaiYfuQ# 

### update driver nvidia 
* sudo apt update && sudo apt upgrade -y 

### check ว่ามี nvidia ภายในเครื่องหรือไม่ 
* ubuntu-drivers devices 
เลือกอันที่มีคำว่า recommend 

* sudo apt install nvidia-driver-515 [เลือก ที่เป็น recommend]

* sudo reboot

### check ดูว่ามีกรอบติดหรือไม่ 
* nvidia-smi


> Aternative way ทางเลือกอื่น
* link: https://www.murhabazi.com/install-nvidia-driver

## Install cuda

* sudo apt-get -y install nvidia-cuda-toolkit

### library (DNN), cuDNN library 

* sudo apt-get -y install nvidia-cudnn

### upgrage version
* sudo apt-get update && upgrade -y

## Install cudnn
* dpkg -l | grep cudnn

