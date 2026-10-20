from priorityqueue import PriorityQueue


def main():
    queue = PriorityQueue()

    while True:
        answer = input("How much you got? ")
        if answer == "":
            break

        bribe = int(answer)
        position = queue.push(-bribe)

        if bribe == 0:
            print("Go to the end of the queue, loser!")
        else:
            print("Excellent, you are now in position #" + str(position)
                  + " in the queue")


if __name__ == "__main__":
    main()
