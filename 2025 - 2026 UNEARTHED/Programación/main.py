from pybricks.tools import hub_menu

# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3","4","5","6","7")

# Based on the selection, run a program.
if selected == "1":
    import corrida_1
elif selected == "2":
    import corrida_2
elif selected == "3":
    import corrida_3
elif selected == "4":
    import corrida_4
elif selected == "5":
    import corrida_5
elif selected == "6":
    import corrida_6
elif selected == "7":
    import corrida_7