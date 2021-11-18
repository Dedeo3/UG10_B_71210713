#input
input_1 = input ("Masukkan angka : ")
input_2 = input ("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3?")
input_3 = input ("Bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10?")

#output
if input_1 == "10" and input_2:
    print ("IYA")
if input_1== "10" and input_3 :
    print ("IYA DONG")
if input_1 == "22" and input_2:
    print ("IYA")
if input_1== "22" and input_3 :
    print ("TIDAK")
if input_1== "9" :
    print ("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. progam dihentikan")