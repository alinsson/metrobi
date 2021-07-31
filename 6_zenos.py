import time

# the time is in geometric progression so the turtle is never reached 
# time      speed_achilles       speed_tortoise
#   0           100                 0
#   1           110                 100
#   1.1         111                 110
#   1.11        111,1               111
#    .           .                   .
#    .           .                   .
#    .           .                   .

distace = 50
speed_a = 8
speed_t = int(speed_a / 2)

for i in range(50):
    time.sleep(0.2)
    t = int(i % (distace / 4 + 1))
    print((t * speed_a * " ") + "A" + ((distace - (t * speed_a) + (t * speed_t)) * "-") + "T" + ((distace - (t * speed_t)) * " "))
