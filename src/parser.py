from data import commands


def parser(command):
    parsedCommand = {"n": None, "v": None}
    if not command:
        print("Please enter a command...")
    else:
        for word in command.split(" "):
            if word in [cmd for values in commands.values() for cmd in values]:
                parsedCommand["v"] = word
            elif len(command.split(" ")) > 1:
                parsedCommand["n"] = word

    # print("parsed", parsedCommand)
    return parsedCommand
