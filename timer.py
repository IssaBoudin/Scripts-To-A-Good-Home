import time

total = 60

def main():
    global total
    for _ in range(60):
        time.sleep(1)
        total -= 1
        print(total)

main()
