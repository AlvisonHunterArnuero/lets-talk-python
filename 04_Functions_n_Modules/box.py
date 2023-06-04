def boxed_menu(options_lst: list, box_title: str, sub_title: str = "Please select an option:"):
    lng = len(box_title)+8 if len(box_title) > len(sub_title) else len(sub_title)+8
    box_title = box_title.center(lng)
    horiz = "═"*lng
    horiz_light = "─"*lng
    print("╔"+horiz+"╗")
    print(f"║{box_title}║")
    print("╠"+horiz+"╣")
    print(f"║ {sub_title.ljust(lng-1)}║")
    print(f"║{horiz_light}║")
    for i, e in enumerate(options_lst):
        print(f"║ {i+1}. {e.ljust(lng-4)}║")
    print("╚"+horiz+"╝")


    # Special ASCII CHARACTERS THAT I USE TO DRAW THIS BOX
    # ╝ ═ ╔╚ ╗║≡╠╣