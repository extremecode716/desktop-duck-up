import tkinter as tk  # 파이썬의 표준 GUI 라이브러리
import time
import random

class Duck:
    def __init__(self):
        self.window = tk.Tk()
        self.load_images()
        self.frame_index = 0
        self.img = self.move_left_images[self.frame_index]
        self.timestamp = time.time()
        self.last_direction_change = time.time()
        self.next_direction_change = random.uniform(3, 10)  # 다음 방향 변경까지의 시간 
        self.initialize_window()
        self.dir_x = -1  # 오리의 x축 방향
        self.dir_y = -1  # 오리의 y축 방향
        self.speed_x = 1  # x축 속도
        self.speed_y = 1  # y축 속도
        self.isClick = False
        self.mouse_click_x = 0  # 마우스 클릭 시작 x 위치
        self.mouse_click_y = 0  # 마우스 클릭 시작 y 위치
        self.move_pet()
        self.window.mainloop()

    def load_images(self):
        # 오리의 이미지를 로드합니다.
        self.move_left_images = [tk.PhotoImage(file='duck-left.gif', format='gif -index %i' % i) for i in range(10)]
        self.move_right_images = [tk.PhotoImage(file='duck-right.gif', format='gif -index %i' % i) for i in range(10)]

    def initialize_window(self):
        self.window.config(background='black')  # 윈도우 배경색을 검정색으로 설정합니다.
        # 윈도우를 투명하게 설정합니다. (macOS에서는 동작하지 않습니다.)
        self.window.wm_attributes('-transparentcolor', 'black')
        # 윈도우의 기본 동작을 무시하도록 설정합니다.
        self.window.overrideredirect(True)
        # 윈도우를 다른 모든 윈도우 위에 표시하도록 설정합니다.
        self.window.attributes('-topmost', True)
        # 마우스로 윈도우를 드래그하여 이동할 수 있도록 이벤트 바인딩을 설정합니다.
        self.window.bind("<ButtonPress-1>", self.start_move)
        self.window.bind("<B1-Motion>", self.on_move)
        self.window.bind("<ButtonRelease-1>", self.stop_move)
        # 라벨 위젯을 생성하고 배경색을 검정색으로 설정합니다.
        self.label = tk.Label(self.window, bd=0, bg='black', width=self.img.width(), height=self.img.height())
        # 오리의 초기 위치를 설정합니다.
        self.x = 1040
        self.y = random.randint(0, self.window.winfo_screenheight() - 128)
        # 라벨 위젯의 이미지를 설정합니다.
        self.label.configure(image=self.img)
        # 라벨 위젯을 윈도우에 배치합니다.
        self.label.pack()
        # 윈도우의 크기를 윈도우의 높이를 기준으로 동적으로 설정합니다.
        window_height = self.window.winfo_screenheight()
        self.window.geometry('256x256+{}+{}'.format(self.x, self.y))

    def change_frame(self, direction):
        # 오리의 프레임을 변경합니다.
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            self.frame_index = (self.frame_index + 1) % 5
            self.img = direction[self.frame_index]

    def change_direction(self):
        old_dir_x, old_dir_y = self.dir_x, self.dir_y
        # x축 방향을 변경합니다.
        self.dir_x = random.choice([-1, 1])
        # y축 방향을 변경합니다.
        self.dir_y = random.choice([-1, 1])
        print(f"방향 변경: ({old_dir_x}, {old_dir_y}) -> ({self.dir_x}, {self.dir_y})")

    def move_pet(self):
        if time.time() - self.last_direction_change > self.next_direction_change:
            self.last_direction_change = time.time()
            self.next_direction_change = random.uniform(3, 10)
            # 방향을 변경합니다.
            self.change_direction()
            # 속도를 빠르게 합니다.
            self.speed_x = random.choice([1, 2])  # x축 속도를 랜덤하게 설정합니다.
            self.speed_y = random.choice([1, 2])  # y축 속도를 랜덤하게 설정합니다.

        if(self.isClick == False):
            # x축 이동
            self.x += self.dir_x * self.speed_x
            # y축 이동
            self.y += self.dir_y * self.speed_y
        # 오리의 방향에 따라 이미지를 변경합니다.
        if self.dir_x < 0:
            direction = self.move_left_images
        else:
            direction = self.move_right_images

        # 오리의 프레임을 변경합니다.
        self.change_frame(direction)

        # 오리가 화면 밖으로 나가지 않도록 합니다.
        if self.x <= 0 or self.x >= (self.window.winfo_screenwidth() - 128):
            self.dir_x *= -1  # x축 방향을 반전시킵니다.
        if self.y <= 0 or self.y >= (self.window.winfo_screenheight() - 128):
            self.dir_y *= -1  # y축 방향을 반전시킵니다.

        # 윈도우의 위치를 설정합니다.
        self.window.geometry('128x128+{}+{}'.format(self.x, self.y))
        # 라벨 위젯의 이미지를 설정합니다.
        self.label.configure(image=self.img)
        self.label.pack()
        # 이동을 반복합니다.
        self.window.after(10, self.move_pet)
        # 윈도우를 최상위로 올립니다.
        self.window.lift()
        
    def start_move(self, event):
        self.isClick = True

    def on_move(self, event):
        if self.isClick:  # 마우스가 클릭된 상태에서만 이동을 처리
            self.x = event.x_root - 64
            self.y = event.y_root - 64
            self.window.geometry(f'+{ self.x}+{self.y}')
            self.isClick = True


    def stop_move(self, event):
        # 마우스 버튼을 놓았을 때 실행될 로직
        # 3초 후에 isClick을 False로 설정
        self.window.after(500, self.set_isClick_false)

    def set_isClick_false(self):
        # isClick을 False로 설정하는 메소드
        self.isClick = False

if __name__ == "__main__":
    Duck()
