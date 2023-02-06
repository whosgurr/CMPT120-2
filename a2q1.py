def substring_finder1(rep, string, integer):
    result = []
    for i in range(integer + 1):
        if string[i] not in rep:
            result.append(string[i])
            rep.append(string[i])
        elif string[i] in rep:
            continue
    print("".join(result))


def main():
    rep_check = []
    valid = True
    while valid:
        try:
            source_str = str(input("Input string:\n"))

            if source_str == 'quit':
                exit()
            else:
                source_int = int(input("Input positive int:\n"))
                substring_finder1(rep_check, source_str, source_int)

        except ValueError:
            exit()


if __name__ == '__main__':
    main()
