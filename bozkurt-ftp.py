import os
import time

os.system("clear")

print("################################")
print("                                ")
print("     Bozkurt Ftp Bf Toolu       ")
print("                                ")
print("################################")
print()

print("1.Ftp Brute Force")
print("2.Kullanım Kılavuzu")

işlem = input("İşlem =")

if işlem =="1":
    x = input("Bu işlemi Yapmadan önce Lütfen Kullanım kılavuzunu okuyunuz Devam etmek için enter'a basınız")
    time.sleep(2)
    os.system("hydra")

if işlem =="2":
    x  = input("Toolu indirdiniz indirdiğiniz tool klasörunu açınız içinde user.txt ve pass.txt olcaktır o ikisini tutup masaüstune atınız klasörden cıkarıp sonra toolu python3 ile çalıştırın kolay gelsin")
    
