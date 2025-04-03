import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("벽돌깨기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 공, 패들, 벽돌 설정
BALL_RADIUS = 10
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BRICK_WIDTH = 75
BRICK_HEIGHT = 20

# 공 초기 위치와 속도
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = 4 * random.choice([-1, 1])
ball_dy = -4

# 패들 초기 위치
paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
paddle_y = SCREEN_HEIGHT - 30

# 벽돌 생성
bricks = []
for row in range(5):
    for col in range(10):
        bricks.append(pygame.Rect(col * (BRICK_WIDTH + 5) + 35, row * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT))

# 공 속도 증가율
SPEED_INCREMENT = 0.1

# 게임 루프
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 6
    if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - PADDLE_WIDTH:
        paddle_x += 6

    # 공 이동
    ball_x += ball_dx
    ball_y += ball_dy

    # 공 벽 충돌
    if ball_x <= BALL_RADIUS or ball_x >= SCREEN_WIDTH - BALL_RADIUS:
        ball_dx *= -1
    if ball_y <= BALL_RADIUS:
        ball_dy *= -1
    if ball_y >= SCREEN_HEIGHT:
        print("Game Over! 공이 화면 아래로 떨어졌습니다.")
        running = False

    # 공 패들 충돌
    paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    if paddle_rect.collidepoint(ball_x, ball_y + BALL_RADIUS):
        ball_dy *= -1

    # 공 벽돌 충돌
    for brick in bricks[:]:
        if brick.collidepoint(ball_x, ball_y):
            bricks.remove(brick)
            ball_dy *= -1
            # 공 속도 증가
            ball_dx += SPEED_INCREMENT if ball_dx > 0 else -SPEED_INCREMENT
            ball_dy += SPEED_INCREMENT if ball_dy > 0 else -SPEED_INCREMENT
            break

    # 벽돌이 모두 제거되었는지 확인
    if not bricks:
        print("축하합니다! 모든 벽돌을 깼습니다!")
        running = False

    # 벽돌 그리기
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)

    # 패들 그리기
    pygame.draw.rect(screen, WHITE, paddle_rect)

    # 공 그리기
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
