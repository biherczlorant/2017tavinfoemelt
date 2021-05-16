data = []
# 1. feladat
with open("valaszok.txt", "r") as f:
    helyesmegoldas = f.readline().strip()
    for line in f:
        bonto = line.strip().split(' ')
        read = {'kod': bonto[0],
                'megoldas': bonto[1]}
        data.append(read)
f.close()
# 2. feladat
print(f'2. feladat: A vetélkedőn {data.__len__()} versenyző indult.')
# 3. feladat
bekerid = input('3. feladat: A versenyző azonosítója = ')
harmasmegold = ""
for i in data:
    if i['kod'] == bekerid:
        harmasmegold = i['megoldas']
        print(f'{harmasmegold}\t(a versenyző válasza)')

# 4. feladat
print('4. feladat')
print(f'{helyesmegoldas}\t(a helyes megoldás)')
szamolo = 0
for i in harmasmegold:
    szamolo += 1
    if i == helyesmegoldas[szamolo-1]:
        print('+',end='')
    else:
        print(' ',end='')
print('\t(a versenyző helyes válaszai)')
# 5. feladat
bekerfeladat = int(input("5. feladat: A feladat sorszáma = "))
helyesvalaszok = 0
for i in data:
    if i['megoldas'][bekerfeladat-1] == helyesmegoldas[bekerfeladat-1]:
        helyesvalaszok += 1
print(f'A feladatra {helyesvalaszok} fő, a versenyzők {round(helyesvalaszok/data.__len__()*100, 2)}%-a adott helyes választ.')
# 6. feladat
egyot = 3
hattiz = 4
tizetizh = 5
tizn = 6


with open('pontok.txt', 'w') as f:
    for i in data:
        szamolo = 0
        pont = 0
        for j in i['megoldas']:
            szamolo+=1
            if j == helyesmegoldas[szamolo-1] and szamolo<6:
                pont += egyot
            if j == helyesmegoldas[szamolo-1] and szamolo>5 and szamolo<11:
                pont += hattiz
            if j == helyesmegoldas[szamolo-1] and (szamolo<14 and szamolo>10):
                pont += tizetizh
            if j == helyesmegoldas[szamolo-1] and szamolo==14:
                pont += tizn
        f.write(f'{i["kod"]} {pont}\n')
f.close()

# 7. feladat
adatok = []
top3 = []
pontszamok = set()
szamolo = 0
with open('pontok.txt') as f:
    for line in f:
        bonto = line.strip().split(' ')
        redd = {'kod': bonto[0],
                'pont': int(bonto[1])}
        adatok.append(redd)
for i in adatok:
    pontszamok.add(i['pont'])
for pont in reversed(sorted(pontszamok)):
    szamolo += 1
    pontozottak = [i for i in adatok if pont==i['pont']]
    top = {'adatok': pontozottak,
           'hely': szamolo}
    top3.append(top)
    if szamolo == 3:
        break

print('7. feladat: A verseny legjobbjai:')
ad = [i['adatok'] for i in top3]
for i in ad:
    for j in i:
        print(f'{ad.index(i)+1}. díj ({j["pont"]} pont) : {j["kod"]}')