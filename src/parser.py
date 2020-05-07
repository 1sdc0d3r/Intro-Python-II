from data import commands


def parser(command):
    parsedCommand = {"n": None, "v": None}
    if not command:
        print("Please enter a command...")
    else:
        for word in command.split(" "):
            for values in commands.values():
                if word in values:
                    parsedCommand["v"] = word
                    break
                elif len(command.split(" ")) > 1:
                    parsedCommand["n"] = word

    # print("parsed", parsedCommand)
    return parsedCommand
