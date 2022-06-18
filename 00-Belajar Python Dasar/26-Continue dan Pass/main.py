
# source: docs.python.org


#continue
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

#pass
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
