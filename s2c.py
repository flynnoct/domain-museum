file_name = "AI.txt"

f1 = open("S/%s" % file_name, "r")
f2 = open("C/%s" % file_name, "w")

f2.write("payload:\n")
for line in f1:
    if line.startswith("DOMAIN-SUFFIX"):
        domain = line.split(",")[1]
        new_line = "  - DOMAIN-SUFFIX," + domain
        f2.write(new_line)
    elif line.startswith("DOMAIN-KEYWORD"):
        domain = line.split(",")[1]
        new_line = "  - DOMAIN-KEYWORD," + domain
        f2.write(new_line)
    elif line.startswith("DOMAIN"):
        domain = line.split(",")[1]
        new_line = "  - DOMAIN," + domain
        f2.write(new_line)
    elif line.startswith("IP-CIDR"):
        ip_range = line.split(",")[1]
        new_line = "  - IP-CIDR," + ip_range + "\n"
        f2.write(new_line)

    