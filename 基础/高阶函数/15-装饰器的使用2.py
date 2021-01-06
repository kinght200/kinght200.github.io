# 产品经理：提需求/该需求
# 如果超过22点不让玩游戏，如果不告诉时间，默认让玩游戏
# 开放封闭原则
def can_play(fn):
    def inner(x, y, *args, **kwargs):
        # print(args)
        # if args[0] <= 22:
        clock = kwargs.get('clock', 20)
        if clock <= 22:
            fn(x, y)
        else:
            print('太晚了，睡觉')

    return inner


@can_play
def play_game(name, game):
    print('{}正在玩{}'.format(name, game))


# play_game('张三', '王者荣耀', 12)
play_game('李四', '绝地求生', m='hello', n='world', clock=18)
