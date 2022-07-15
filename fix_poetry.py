fn = 'poetry.lock'
# Read the file.
with open(f"{fn}", 'r') as f:
    lines = f.readlines()
# Do the modification.
collecting = False
breaker = None
i_drop = []
for i, line in enumerate(lines):
    if collecting:
        if line.startswith(breaker):
            collecting = False
        else:
            i_drop.append(i)
            continue
    if line == "[package.dependencies]\n" and lines[i+1].startswith("setuptools"):
        i_drop.append(i-1)
        i_drop.append(i)
        collecting = True
        breaker = "\n"
    if line == "[[package]]\n" and lines[i + 1] == "name = \"setuptools\"\n":
        i_drop.append(i-1)
        i_drop.append(i)
        collecting = True
        breaker = "[["
    if line.startswith("setuptools = ["):
        i_drop.append(i-1)
        i_drop.append(i)
        collecting = True
        breaker = "]"
# Write result.
with open(f"{fn}", 'w') as f:
    f.writelines([line for i, line in enumerate(lines) if i not in i_drop])
