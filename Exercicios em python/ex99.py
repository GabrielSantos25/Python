from time import sleep


def valores(* num):
    print('-='*20)
    print('Analisando os valores passados...')
    for c in num:
        print(f"{c}", end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.', end='')
    print()
    print(f'O maior valor informado foi {max(num)}.')
    

valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores(0)