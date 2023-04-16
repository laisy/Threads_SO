
import threading

'Definindo funções que serão executadas como Threads'

def th1(m):
    while True:
        print(f'Thread {m}')

def th2(m):
    while True:
        print(f'Thread {m}')

if __name__ == "__main__":

    'Criando Threads '

    t1 = threading.Thread(target=th1,args=('Thread 1 ...',))
    t2 = threading.Thread(target=th1,args=('Thread 1 ...',))

    'Iniciando threads Threads t1 com th1 e Thread t2 com th2'
    t1.start()
    t2.start()

    'Thread Main espera por t1 e t2'
    t1.join(5)
    t2.join(5)
