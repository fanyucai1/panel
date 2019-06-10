#Email:fanyucai1@126.com
#2019.5.23
import os
import argparse
import subprocess
import sys
sub=os.path.abspath(__file__)
dir_name=os.path.dirname(sub)
sys.path.append(dir_name)
import core
import time

parser=argparse.ArgumentParser("Run 275 panel analysis.")
parser.add_argument("-p1","--pe1",help="tumor 5 reads",required=True)
parser.add_argument("-p2","--pe2",help="tumor 3 reads",required=True)
parser.add_argument("-p","--prefix",help="prefix output",required=True)
parser.add_argument("-o","--outdir",help="output directory",required=True)
parser.add_argument("-v","--VAF",help="VAF threshold",choices=[0.02,0.005],required=True,type=float)
args=parser.parse_args()
start=time.time()
if not os.path.exists(args.outdir):
    os.mkdir(args.outdir)
out=args.outdir+"/"+args.prefix
a=args.pe1
b=args.pe2
purity=0
if args.VAF==0.02:
    purity=0.1
else:
    purity=0.01
#####################################################################run docker
core.print_config.tumor_only(a, b, args.prefix, args.outdir,purity)
#####################################################################filter VAF and genelist
cmd = '%s %s/prefilter.py -i %s.smCounter.cut.vcf -p %s -v %s -o %s/result/'\
      % (config['par']['python3'], script, out,prefix, config['par']['vaf'],outdir)
subprocess.check_call(cmd, shell=True)










end=time.time()
print("Elapse time is %g seconds" %(end-start))
