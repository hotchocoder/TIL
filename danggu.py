import socket
import time
import math

NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.scoket()

# - 1radian = 180 / PI (도)
# - 1도 = PI / 180 (radian)
# angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
radian = math.atan(width / height) if height > 0 else 0
angle = 90

# distance: 두 점(좌표) 사이의 거리를 계산
distance = math.sqrt(width**2 + height**2)

# power: 거리 distance에 따른 힘의 세기를 계산
power = 50

# 주어진 데이터(공의 조표)를 활용하여 두 개의 값을 최종 결정하고 나면,
# 나머지 코드에서 값을 보내 자동으로 플레이를 진행하게 합니다.
# - angle: 흰 공을 때려서 보낼 방향(각도)
# - power: 흰 공을 떄릴 힘의 세기