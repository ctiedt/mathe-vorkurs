import os, sys

infile = sys.argv[1].replace("\\", "/")
outfile = sys.argv[2].replace("\\", "/")

os.system(f"python ./markdown-scripted.py \"{infile}\" \"{outfile[:30]+'mds/'+outfile[30:]}\"")
os.system(f"C:/pandoc-2.3-windows-x86_64/pandoc \"{outfile[:30]+'mds/'+outfile[30:]}\" -f markdown -t html -s -o \"{outfile[:30]+'html/'+outfile[30:]}.html\" --katex --css \"https://notes.zortax.de/css/retro.css\"")