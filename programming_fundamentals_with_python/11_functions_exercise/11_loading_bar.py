def loading_bar(percent):
    if percent == 100:
        return "100% Complete!\n[%%%%%%%%%%]"

    loaded_percent = percent // 10
    return f"{percent}% [{'%' * loaded_percent}{'.' * (10 - loaded_percent)}]\nStill loading..."


number = int(input())
print(loading_bar(number))
