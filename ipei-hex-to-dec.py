hex = input("Enter IPEI to convert: ")

emc = hex[1:5]
emc = int(emc, 16)
emc = str(emc).zfill(5)

psn = hex[5:10]
psn = int(psn, 16)
psn = str(psn).zfill(7)

dec = emc + psn

checksum = 0
i = 1
for c in dec:
  checksum += int(c) * i
  i += 1

checksum = checksum % 11

dec += str(checksum)

print(dec)
