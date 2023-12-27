from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
mouse.visible = False

# 복도의 벽, 바닥, 천장을 생성
main_floor = Entity(model = 'cube', position=(0,0,0), scale = (10,1,100), color=color.gray
                    ,collider= 'box')
main_ceiling = Entity(model = 'cube', position=(0,10,0), scale = (10,1,100), color=color.gray
                      ,collider= 'box') 
main_left_wall = Entity(model = 'cube', position=(-5,5,-5), scale = (1,10,110), collider= 'box', texture='assets/wall.jpg', texture_scale = (16,10)) 
main_right_wall = Entity(model = 'cube', position=(5,5,5), scale = (1,10,110), collider= 'box', texture='assets/wall.jpg', texture_scale = (16,10)) 


for i in range(-90, 90):
    tile = Entity(model='cube', position=(0,0.5,0.5*i), scale = (0.5,0,0.5), texture = 'assets/yellow_tile.jpg')



#앞쪽
front_floor = Entity(model='cube', position=(-25,0,55), scale=(60,1,10), color=color.gray, collider='box')
front_ceiling = Entity(model='cube', position=(-25,10,55), scale=(60,1,10), color=color.gray, collider='box')
front_left_wall = Entity(model='cube', position=(-30,5,50), scale=(50,10,1), collider= 'box', texture='assets/wall.jpg', texture_scale = (16,10)) 
front_right_wall = Entity(model='cube', position=(-20,5,60), scale=(50,10,1), collider= 'box', texture='assets/wall.jpg', texture_scale = (16,10)) 


front_floor_2 = Entity(model='cube', position=(-50, 0, 80), scale=(10, 1, 60), color=color.gray, collider='box')
front_ceiling_2 = Entity(model='cube', position=(-50, 10, 80), scale=(10, 1, 60), color=color.gray, collider='box')
front_left_wall_2 = Entity(model='cube', position=(-55, 5, 75), scale=(1, 10, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))
front_right_wall_2 = Entity(model='cube', position=(-45, 5, 85), scale=(1, 10, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))

#뒤쪽
back_floor = Entity(model='cube', position=(25, 0, -55), scale=(60, 1, 10), color=color.gray, collider='box')
back_ceiling = Entity(model='cube', position=(25, 10, -55), scale=(60, 1, 10), color=color.gray, collider='box')
back_left_wall = Entity(model='cube', position=(30, 5, -50), scale=(50, 10, 1), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))
back_right_wall = Entity(model='cube', position=(20, 5, -60), scale=(50, 10, 1), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))

back_floor_2 = Entity(model='cube', position=(50, 0, -80), scale=(10, 1, 60), color=color.gray, collider='box')
back_ceiling_2 = Entity(model='cube', position=(50, 10, -80), scale=(10, 1, 60), color=color.gray, collider='box')
back_left_wall_2 = Entity(model='cube', position=(55, 5, -75), scale=(1, 10, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))
back_right_wall_2 = Entity(model='cube', position=(45, 5, -85), scale=(1, 10, 50), collider='box', texture='assets/wall.jpg', texture_scale=(16, 10))

#EditorCamera()
player = FirstPersonController()
player.cursor.visible = False
player.gravity = 0.5
player.speed = 15


def update():
    print(player.position)
    if player.position.x < -25 and player.position.z > 50:
        player.set_position((
            50 + player.position.x,
            player.position.y,
            -110  + player.position.z
        ))
    elif player.position.x > 25 and player.position.z < -50:
        player.set_position((
            -50 + player.position.x,
            player.position.y,
            110 + player.position.z
        ))

app.run()