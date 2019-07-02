import rpyc
import math
conn=rpyc.classic.connect("localhost")
conn.execute('import math')

def piSayisiIleCarp(x):
    print(x*math.pi)

def ikiSayiCarp(sayi1,sayi2):
    print("sayi1*sayi2="+str(sayi1*sayi2))

#conn.teleport(piSayisiIleCarp)
fn=conn.teleport(piSayisiIleCarp)
fn(5)

sayi1=5
sayi2=15
cn=conn.teleport(ikiSayiCarp)
cn(sayi1,sayi2)

#conn.execute("ikiSayiCarp(3,5)")

