from data import commands


def parser(command):
    parsedCommand = {
        "verb": None,
        "noun": None
    }
    if not command:
        print("Please enter a command...")
    else:
        parsedCommand.clear()
        for word in command.split(" "):
            for values in commands.values():
                if word in values:
                    parsedCommand["verb"] = word
                    break
                elif len(command.split(" ")) > 1:
                    parsedCommand["noun"] = word
                else:
                    parsedCommand["noun"] = None
                    parsedCommand["verb"] = None
    # print("parsed", parsedCommand)
    return parsedCommand
