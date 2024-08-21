lemaara = float(input("kuinka monta leiviskää?\n"))
namaara = float(input("kuinka monta naulaa?\n"))
lumaara = float(input("kuinka monta luotia?\n"))
luoti = lumaara * 13.3
naula = namaara * 13.3 * 32
leiviska = lemaara * 13.3 * 32 * 20
yhteispaino = luoti + naula + leiviska
kgpaino = yhteispaino // 1000
gpaino = yhteispaino % 1000
print(f'massa nykymittojen mukaan: \n{kgpaino:.0f} kilogrammaa ja {gpaino:.0f} grammaa')