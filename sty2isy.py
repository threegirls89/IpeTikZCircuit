inputfilename = 'ipetikzcircuit.sty'
outputfilename = 'ipetikzcircuit.isy'

fin = open(inputfilename, 'r',encoding='utf-8')
fout = open(outputfilename, 'w')

fout.write('<ipestyle name="ipetikzcircuit">\n<preamble>\n\\makeatletter\n')

i = 0
for line in fin:
    i += 1
    print(str(i))
    if line[0] == '%' or i <= 7:
        continue
    else:
        line = line.replace('RequirePackage', 'usepackage')
        fout.write(line)

fout.write('</preamble>\n</ipestyle>\n\\makeatletter\n')

fin.close()
fout.close()

print('finish!!')
