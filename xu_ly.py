import csv 
import sys 
from collections import  defaultdict
def main():
   if len(sys.argv) !=3:
      print('cách dùng python3 <dữ liệu đầu vào> <dữ liệu đầu ra>') 
      sys.exit(1) 
   file_dau_vao=sys.argv[1]
   file_dau_ra=sys.argv[2]
   tong=defaultdict(float)
   so_dong=0
   with open(file_dau_vao,newline='',encoding='utf-8') as f:
       for dong in DictReader(f):
           tong[dong['san_pham']]+=int(dong['so_luong'])* float(dong['dong_gia'])
           so_dong +=1
   with open(file_dau_ra,'w', newline='',encoding='utf-8') as f: 
       w=csv.writer(f)
       w.writerow(['san_pham','doanh_thu'])
       for sp,dt in (tong.items()):
           w.writerow([sp,dt]) 
   print('đã xử lí xong {so_dong} dòng và {len(tong)}')
main()
    
