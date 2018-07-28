import time

name = input("Beri nama monstermu : ")
monster = {"name": name, "power": 100}

def startGame():
    print("%s ingin apa hari ini ? " % (name))
    print("\n 1.Makan \n 2.Cek Status \n 3. Tidur")
    choice = input("pilih = ")
    if choice == "1":
        makan()
    elif choice == "2":
        status()
    else:
        tidur()


def makan():
    for i in range(0,3):
        monster['power']+=10
        time.sleep(1)
        print("Nyam ... ")
    time.sleep(2)
    startGame()
    
def status():
    print(monster['name'])
    print("Power hari ini : %d" % (monster['power']))
    time.sleep(2)
    startGame()

def tidur():
    print("Zzzzzz....")
    time.sleep(1)

startGame()