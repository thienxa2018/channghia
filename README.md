# Pipeline xử lí doanh số bằng Bash và Python 

#Pipeline nhỏ Bash kiểm tra dữ liệu và ghi log,Python tính toán doanh thu theo sản phẩm 
 
## Cấu trúc 
```
pipeline/
├── chay_pipeline.sh
├── data
│   └── doanh_so.csv
├── logs
├── outline
├── output
│   └── thu.csv
└── xu_ly.py
```
## cách chạy cần dùng WSL,Linux,Python3
```bash 
git clone <địa chỉ repo> ~/pipeline 
cd ~/pipeline
mkdir -p logs output 
chmod +x chay_pipeline.sh 
./chay_pipeline.sh
cat ./output/doanh_thu_*.csv 
cat ./logs/pipeline.log 
## kết quả mẫu
san_pham,doanh_thu
but,150000.0
thuoc,24000.0
vo,60000.0
``` 
## cách hoạt động 
1.chạy file 'chay_pipeline.sh' để kiểm tra file đầu vào và in ra lỗi cần thiết 
2.gọi 'xu_ly.py' với 2 tham số file vào và file ra 
3.Python lỗi 


chanbomaydi
