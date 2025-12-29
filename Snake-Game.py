import time
import random
import functools
import turtle

MAX_X = 600
MAX_Y = 700
DEFAULT_SIZE = 20
SNAKE_SHAPE = 'square'
HIGH_SCORES_FILE_PATH = 'high_scores.txt'
# Controla a velocidade da cobra. Quanto menor o valor, mais rápido é o movimento da cobra.
SPEED = 0.4

def load_high_score(state):
    # se já existir um high score devem guardar o valor em state['high_score']
    
    with open(HIGH_SCORES_FILE_PATH, 'a+') as f_in_out:
        f_in_out.seek(0)
        dados = f_in_out.readlines()
        if dados == []:
            state['high_score'] = 0
        else:
            state['high_score'] = int(dados[-1])

    
def write_high_score_to_file(state):
    
    with open(HIGH_SCORES_FILE_PATH, 'w') as f_in_out:
        texto = str(state['new_high_score'])
        f_in_out.write(texto)
        f_in_out.close()
    

def create_score_board(state):
    score_board = turtle.Turtle()
    score_board.speed(0)
    score_board.shape("square")
    score_board.color("black")
    score_board.penup()
    score_board.hideturtle()
    score_board.goto(0, MAX_Y / 2.2)
    state['score_board'] = score_board
    load_high_score(state)
    update_score_board(state)

def update_score_board(state):
    state['score_board'].clear()
    state['score_board'].write("Score: {} High Score: {}".format(state['score'], state['high_score']), align="center", font=("Helvetica", 24, "normal"))

def go_up(state):
    if state['snake']['current_direction'] != 'down':
        state['snake']['current_direction'] = 'up'

def go_down(state):
    if state['snake']['current_direction'] != 'up':
        state['snake']['current_direction'] = 'down'

def go_left(state):
    if state['snake']['current_direction'] != 'right':
        state['snake']['current_direction'] = 'left'

def go_right(state):
    if state['snake']['current_direction'] != 'left':
        state['snake']['current_direction'] = 'right'

def init_state():
    state = {}
    # Informação necessária para a criação do score board
    state['score_board'] = None
    state['new_high_score'] = False
    state['high_score'] = 0
    state['score'] = 0
    # Para gerar a comida deverá criar um nova tartaruga e colocar a mesma numa posição aleatória do campo
    state['food'] = None
    state['speed'] = SPEED
    state['window'] = None
    state['fundo'] = None
    snake = {
        'head': None,                  # Variável que corresponde à cabeça da cobra
        'current_direction': None     # Indicação da direcção atual do movimento da cobra
    }
    state['snake'] = snake
    return state

def setup(state):
    window = turtle.Screen()
    window.setup(width=MAX_X, height=MAX_Y)
    window.listen()
    window.onkey(functools.partial(go_up, state), 'w')
    window.onkey(functools.partial(go_down, state), 's')
    window.onkey(functools.partial(go_left, state), 'a')
    window.onkey(functools.partial(go_right, state), 'd')
    window.tracer(0)   
    state['window'] = window
    snake = state['snake']
    snake['current_direction'] = 'stop'
    snake['head'] = turtle.Turtle()
    snake['head'].shape(SNAKE_SHAPE)
    snake['head'].showturtle()
    snake['head'].pu()
    snake['head'].color('green')
    create_score_board(state)
    create_food(state) 
    
corpo = []

def move(state):
    ''' 
    Função responsável pelo movimento da cobra no ambiente.
    '''

    snake = state['snake']
    for i in range(len(corpo)-1, 0, -1):
        x = corpo[i-1].xcor()
        y = corpo[i-1].ycor()
        corpo[i].goto(x,y)
    
    if len(corpo) > 0:
        x = snake['head'].xcor()
        y = snake['head'].ycor()
        corpo[0].goto(x,y)


    if snake['current_direction'] == "up":
        y = snake['head'].ycor()
        snake['head'].sety(y+15)
    if snake['current_direction'] == "down":
        y = snake['head'].ycor()
        snake['head'].sety(y-15)
    if snake['current_direction'] == "left":
        x = snake['head'].xcor()
        snake['head'].setx(x-15)
    if snake['current_direction'] == "right":
        x = snake['head'].xcor()
        snake['head'].setx(x+15)    

    snake =state['snake']

def create_food(state):
    ''' 
        Função responsável pela criação da comida. Note que elas deverão ser colocadas em posições aleatórias, mas dentro dos limites do ambiente.
    '''
    food = turtle.Turtle()
    food.speed(0) 
    food.shape('circle') 
    food.color('red') 
    food.penup() 
    x = random.randint((-MAX_X/2)+20, (MAX_X/2)-20)
    y = random.randint((-MAX_Y/2)+20, (MAX_Y/2)-20)
    food.goto(x, y) 
    state['food'] = food
    
    # a informação sobre a comida deve ser guardada em state['food']  

def check_if_food_to_eat(state):
    ''' 
        Função responsável por verificar se a cobra tem uma peça de comida para comer. Deverá considerar que se a comida estiver a uma distância inferior a 15 pixels a cobra pode comer a peça de comida. 
    '''  
    snake = state['snake']
    food = state['food'] 
    if snake['head'].distance(food) < 15:
        x = random.randint((-MAX_X/2)+20, (MAX_X/2)-20)
        y = random.randint((-MAX_Y/2)+20, (MAX_Y/2)-20)
        food.goto(x, y)  
        add_corpo(state)
        state['score'] += 10
        state['speed'] -= 0.02
        fundo(state)        
        if state['speed'] == 0.02:
            state['speed'] = 0.02
        update_score_board(state)
        if state['score'] > state['high_score']: 
            state['high_score'] = state['score'] 
            update_score_board(state)        
        state['new_high_score'] = state['high_score']
        
    # para ler ou escrever os valores de high score, score e new high score, devem usar os respetivos campos do state: state['high_score'], state['score'] e state['new_high_score'] 
        
def add_corpo(state):
    ''' 
    Função responsavel por fazer crescer o corpo da cobra.
    '''
    cauda = turtle.Turtle()
    cauda.speed(0) 
    cauda.shape(SNAKE_SHAPE) 
    cauda.color('black') 
    cauda.penup()
    corpo.append(cauda)
    state['cauda'] = cauda
    
def boundaries_collision(state):
    ''' 
        Função responsável por verificar se a cobra colidiu com os limites do ambiente. Sempre que isto acontecer a função deverá returnar o valor booleano True, caso contrário retorna False.
    '''
    snake = state['snake']
    if snake['head'].xcor()>(MAX_X/2)-10 or snake['head'].xcor()<(-MAX_X/2)+10 or snake['head'].ycor()>(MAX_Y/2)-10 or snake['head'].ycor()<(-MAX_Y/2)+10:
        time.sleep(1)
        snake['head'].goto(0,0) 
        snake['head'].direction = "stop"
        state['score'] = 0 
        update_score_board(state)        
        
        return True
    else:
        return False
    
def check_collisions(state):
    '''
        Função responsável por avaliar se há colisões. Atualmente apenas chama a função que verifica se há colisões com os limites do ambiente. No entanto deverá escrever o código para verificar quando é que a tartaruga choca com uma parede ou com o seu corpo.
    '''
    snake = state['snake']
    for corposnake in corpo:
        if corposnake.distance(snake['head']) < 15:
            time.sleep(1)
            snake['head'].goto(0,0) 
            state['score'] = 0 
            update_score_board(state)   
            snake['head'].direction = "stop"
            return True
             
    return boundaries_collision(state)
        
def fundo(state):
    '''
      Função que faz mudar a cor do fundo quando se atinge uma certa pontuação.
    '''
    fundo = turtle.Screen()
    if state['score'] == 100:
        fundo.bgcolor('pink')
    elif state['score'] == 300:
        fundo.bgcolor('pink')
    elif state['score'] == 500:
        fundo.bgcolor('pink')        
    else:
        fundo.bgcolor('white')
    state['fundo'] = fundo
        
def main():
    state = init_state()
    setup(state)
    while not check_collisions(state):
        state['window'].update()
        check_if_food_to_eat(state)
        move(state)
        time.sleep(state['speed']) 
    print("YOU LOSE!")
    if state['new_high_score']:
        write_high_score_to_file(state)
    turtle.done()

main()
