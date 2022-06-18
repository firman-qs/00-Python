
#? Operator Bitwise, Operasi Biner, Binary

print("\n------- ------- ------- -------")

a = 9
b = 5

## Bitwise Or (|)
print("\n======== OR ========")
c = a | b
print("nilai :", a, ", Binary  :", format(a, '08b'))
print("nilai :", b, ", Binary  :", format(b, '08b'))
print("--------------------------------(|) ")
print("nilai :", c, ", Binary :", format(c, '08b'))

## Bitwise and (&)
print("\n======== AND =======")
c = a & b
print("nilai :", a, ", Binary  :", format(a, '08b'))
print("nilai :", b, ", Binary  :", format(b, '08b'))
print("--------------------------------(&) ")
print("nilai :", c, ", Binary  :", format(c, '08b'))

## bitwise XOR (^)
print("\n======== XOR =======")
c = a ^ b
print("nilai :", a, ", Binary  :", format(a, '08b'))
print("nilai :", b, ", Binary  :", format(b, '08b'))
print("--------------------------------(^) ")
print("nilai :", c, ", Binary :", format(c, '08b'))

## bitwise NOT (~)
print("\n======== NOT =======")
c = ~a
print("nilai :", a, ", Binary   :", format(a, '08b'))
print("--------------------------------(~) ")
print("nilai :", c, ", Binary :", format(c, '08b'))
## flip
x = 0b11111111
c = a^x
print("nilai :", a, ", Binary   :", format(a, '08b'))
print("nilai :", x, ", Binary :", format(x, '08b'))
print("------------------------------FLIP ")
print("nilai :", c, ", Binary :", format(c, '08b'))


## Shifting
## Shift Right (>>)
print("\n======== >> =======")
c = a >> 2
print("nilai :", a, ", Binary   :", format(a, '08b'))
print("-----------------------------(>>) ")
print("nilai :", c, ", Binary   :", format(c, '08b'))

## Shitf left
print("\n======== << =======")
c = a << 2
print("nilai :", a, ", Binary   :", format(a, '08b'))
print("-----------------------------(>>) ")
print("nilai :", c, ", Binary   :", format(c, '08b'))




print("\n------- ------- ------- -------\n")
