def cna_play(fn):
    print('外部函数被调用了')

    def inner(name, game, **kwargs):  # kwargs = {'clock':22} kwargs['clock']
        clock = kwargs.get('clock', 21)
        if clock >= 21:
            print('太晚了，睡觉去')
        else:
            fn(name, game)

    return inner


@cna_play
def play_game(name, game):
    print(name + '正在玩儿' + game)


play_game('张三', '王者荣耀', clock=20)
