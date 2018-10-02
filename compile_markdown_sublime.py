import os, sys

infile = sys.argv[1].replace("\\", "/")

os.system(f"python ./markdown-scripted.py \"{infile}\" \"{infile[:30]+'mds/'+infile[30:]}s\"")
os.system(f"C:/pandoc-2.3-windows-x86_64/pandoc \"{infile[:30]+'mds/'+infile[30:]}s\" -f markdown -t html -s -o \"{infile[:30]+'html/'+infile[30:-3]}.html\" --katex --css \"https://notes.zortax.de/css/retro.css\"")