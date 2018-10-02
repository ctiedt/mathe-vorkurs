import random, subprocess, os, sys

if len(sys.argv) < 3:
    print("An input and output file must be specified")
    raise SystemExit

filename = sys.argv[1]
outfile = sys.argv[2]

profiles = {"python-exec":"python"}

to_replace = dict()

def batch_startswith(str_, subs):
    for sub in subs:
        if str_.startswith(sub):
            return sub
    return False

with open(filename) as file:
    contents = file.read()
    lines = [line + "\n" for line in contents.split("\n")]
    for i, line in enumerate(lines):
        s = batch_startswith(line, ["```" + k for k in profiles.keys()])
        if s:
            code = ""
            k = 1
            while not lines[i+k].startswith("```"):
                code += lines[i+k]
                k += 1
            tmp_name = "".join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(8))
            with open(tmp_name, "w") as tmp_file:
                tmp_file.write(code)
            to_replace[s+"\n"+code+"```"] = (tmp_name, s[3:])

for k in to_replace.keys():
    contents = contents.replace(k, subprocess.check_output([profiles[to_replace[k][1]], to_replace[k][0]]).decode().replace("\r", ""))
    os.remove(to_replace[k][0])

with open(outfile, "w+") as of:
    of.write(contents)