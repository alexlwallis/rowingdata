#!C:\Users\e408191\AppData\Local\Continuum\Anaconda\python.exe
import rowingdata
from sys import argv

readFile = argv[1]

try:
    rowerFile = argv[2]
except IndexError:
    rowerFile = "defaultrower.txt"

rower = rowingdata.getrower(rowerFile)

outfile = readFile+"_o.csv"

res = rowingdata.painsledDesktopParser(readFile)
res.write_csv(outfile)

row = rowingdata.rowingdata(outfile,rowtype="Indoor Rower",rower=rower)

row.plottime_erg()

print row.allstats()



print "done "+readFile
