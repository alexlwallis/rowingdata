#! /usr/bin/python
import rowingdata
from sys import argv

def main():
    readFile=argv[1]

    try:
	rowerFile=argv[2]
    except IndexError:
	rowerFile="defaultrower.txt"

    rower=rowingdata.getrower(rowerFile)

    tcxFile=readFile
    csvoutput=readFile+"_o.CSV"

    tcx=rowingdata.TCXParser(tcxFile)
    tcx.write_nogeo_csv(csvoutput,window_size=20)

    res=rowingdata.rowingdata(csvoutput,rowtype="On-water",
				rower=rower)

    print(res.allstats())
    rowingdata.copytocb(res.allstats())


    res.plottime_otw()


    print("done "+readFile)
