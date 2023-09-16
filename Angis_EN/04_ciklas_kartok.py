import lygis4

slibinas = lygis4.slibinas
slibinas.pirmyn()


def repeat_dragon_jump_and_then_turn_right(_times):
    for i in range(_times):
        slibinas.sok()
    slibinas.desinen()


times = 5
while times > 0:
    for j in range(2):
        repeat_dragon_jump_and_then_turn_right(times)
    times -= 1

# Another way:
# for times in range(5, 0, -1):
#     for j in range(2):
#         repeat_dragon_jump_and_then_turn_right(times)
