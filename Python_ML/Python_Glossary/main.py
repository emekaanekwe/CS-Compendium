# TODO: what is the point of f in print? when is it necessary?
# TODO: what are sets used for?
# TODO: with for loops, range are for ints only?
from how_x_works.classes import Bot, BotList

if __name__ == '__main__':
    bot_1 = Bot("bipedaloid", 5, 10.10)
    print("model: " + bot_1.model)
    # required when printing string with nums
    print(f"energy:", bot_1.energy)
    print(f"version:", bot_1.version)

    bot_1.walk()
    bot_1.stop()

    bot_2 = BotList("qudrapedloid", ["arms", "legs", "head"], {"small", "blue", "fast"},
                    {"moveLeft": 1, "moveRight": 2, "moveForward": 3, "moveBackward": 4}, True)

    print("this bot's name is " + bot_2.name)
    print(f"set: ", bot_2.attribute_set)
    print(f"list: ", bot_2.part_list)
    print(f"dict: ", bot_2.action_sequence)
    print(bot_2.name, ", tell me what one of the parts that you have:", bot_2.part_list[2])

    print(bot_2.name, "'s set of attributes are:")
    attributes = bot_2.attribute_set
    for i in attributes:
        print(i)
        
    n = Node.init_node(2)
    print(n)