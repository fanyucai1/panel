import argparse
import re

def run(anno_vcf,low_vcf,outdir,prefix):
    infile1=open(anno_vcf,"r")
    infile2=open(low_vcf,"r")
    outfile=open("%s/%s.final.vcf"%(outdir,prefix),"w")
    outfile.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n")
    for line in infile1:
        line=line.strip()
        if not line.startswith("#"):
            array=line.split("\t")
            info=array[-1].split(":")
            GT=info[0]
            AD=info[1].split(",")
            VF=info[2].split(",")
            ALT=array[4].split(",")
            Ref_Reads =AD[0]
            if len(VF)==1:
                Alt_Reads=AD[1]
                Var=VF[0]
                outfile.write("%s\t%s\t%s\t%s\t%s\t.\t.\tRef_Reads=%s;Alt_Reads=%s;GT=%s;Var=%s\n"%(array[0],array[1],array[2],array[3],array[4],Ref_Reads,Alt_Reads,GT,Var))
            else:
                for i in range(1,len(AD)):
                    Alt_Reads=AD[i]
                    Var=VF[i-1]
                    outfile.write("%s\t%s\t%s\t%s\t%s\t.\t.\tRef_Reads=%s;Alt_Reads=%s;GT=%s;Var=%s\n" % (array[0], array[1], array[2], array[3], ALT[i-1], Ref_Reads, Alt_Reads, GT, Var))
    infile1.close()
    dict={}
    for line in infile2:
        line = line.strip()
        array=line.split("\t")
        if line.startswith("READ_SET"):
            for i in range(len(array)):
                if array[i] in('CHROM', 'POS','ID','REF','ALT','QUAL','FILTER','UMT','VMT','VMF'):
                    dict[array[i]]=array[i]
        else:
            Total_reads,Ref_Reads,Alt_Reads,Var="","","",""
            for i in range(len(array)):
                if dict[array[i]]=="CHROM":
                    outfile.write("%s"%(array[i]))
                elif dict[array[i]]=="UMT":
                    Total_reads=array[i]
                elif dict[array[i]]=="VMT":
                    ALT_Reads=array[i]
                elif dict[array[i]] == "VMF":
                    Var=array[i]
                else:
                    outfile.write("\t%s" % (array[i]))
                Ref_Reads=int(Total_reads)-int(Alt_Reads)
                outfile.write("\tRef_Reads=%s;Alt_Reads=%s;GT=.;Var=%s\n"%(Ref_Reads,Alt_Reads,Var))
            outfile.write()