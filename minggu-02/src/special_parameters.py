def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print('argument', pos1, 'and', pos2, 'is positional only argument')
    print('argument', pos_or_kwd, 'can be used as positional or keyword argument')
    print('argument', kwd1, 'and', kwd2, 'is keyword only argument')

f('positional 1', 'positional 2', pos_or_kwd='combine', kwd1='keyword 1', kwd2='keyword 2')