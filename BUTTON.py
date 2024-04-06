import RPi.GPIO as A
A.setwarnings(False)
A.setmode(A.BOARD)
A.setup(18,A.OUT)
A.setup(32,A.IN,pull_up_down = A.PUD_UP)
while (True):
    input_state=A.input(32)
    if(input_state==0):
        A.output(18,1)
        print('LED ON')
    else:
        A.output(18,0)
        print('LED OFF')
    