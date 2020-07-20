#/usr/bin/python
## 016. Read "read_sample.txt"
import sys

if len(sys.argv) != 2 :
    print(f"# usage : python {sys.argv[0]} [fasta]")
    sys.exit()

f = sys.argv[1]
total = 0
d = {}

# Read file
with open(f, 'r') as  handle :
    for line in handle :
        if line.startswith(">") :
            continue
        
        # Count bases
        for s in line.strip() :
            if s in d :
                d[s] += 1
            else :
                d[s] = 1

# Print the number of bases        
for k, v in d.items() :
    total += v
    print(f"{k} : {v}")

print(f"Total : {total}")


# Write file
with open("write_sample.txt", 'w') as handle :
    handle.write(f"A : {d['A']}\n")
    handle.write(f"C : {d['C']}\n")
    handle.write(f"G : {d['G']}\n")
    handle.write(f"T : {d['T']}\n")
