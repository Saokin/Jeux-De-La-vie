from environnement import Env
from display import Display

# env.focus_set(55, 54)
# env.focus_set(55, 55)
# env.focus_set(55, 56)
# env.focus_set(56, 53)
# env.focus_set(56, 54)
# env.focus_set(56, 56)
# env.focus_set(56, 57)
# env.focus_set(54, 55)

## Basique
env = Env(10)
env.adj_set(5, 5, True)
env.adj_set(5, 4, True)
env.adj_set(5, 6, True)
engine = Display(env)
engine.start()


## HARD
env = Env(100)
env.adj_set(55, 54, True)
env.adj_set(55, 55, True)
env.adj_set(55, 56, True)
env.adj_set(56, 53, True)
env.adj_set(56, 54, True)
env.adj_set(56, 56, True)
env.adj_set(56, 57, True)
env.adj_set(54, 55, True)
engine = Display(env)
engine.start()
