import sys
import os
import re
import subprocess
samplelist=sys.argv[1]
dir=sys.argv[2]
outdir=sys.argv[3]

infile=open(samplelist,'r')
sampleID={}
for line in infile:
    line=line.strip()
    array=line.split("\t")
    sampleID[array[0]]=1
cmd="scp "
for (root,dirs,files) in os.walk(dir):
    for name in files:
        file=os.path.join(root, name)
        p1=re.compile(r'SmallVariants.genome.vcf$')
        p2=re.compile(r'BJ19\S+smCounter.cut.vcf')
        a=p1.findall(file)
        b=p2.findall(file)
        if a!=[] or b!=[]:
            cmd+=" %s "%(file)
cmd+=" fanyucai@192.168.1.118:%s "%(outdir)
subprocess.check_call('echo %s >run.sh'%(cmd),shell=True)