import tkinter as tk  # 파이썬의 표준 GUI 라이브러리입니다.
import time
import random

class Duck:
    def __init__(self):
        self.window = tk.Tk()  # Tk 클래스의 인스턴스를 생성하여 윈도우를 만듭니다.
        self.load_images()  # 이미지를 로드하는 메서드를 호출합니다.
        self.frame_index = 0 # 프렝미 인덱스
        self.img = self.move_left_images[self.frame_index]  # 왼쪽으로 이동하는 이미지를 기본 이미지로 설정합니다.
        self.timestamp = time.time() # 시간 초기화
        self.last_direction_change = time.time() # 시간 초기화
        self.initialize_window()  # 윈도우를 초기화하는 메서드를 호출합니다.
        self.dir = -1  # 오리의 초기 이동 방향을 설정합니다.
        self.move_pet()  # 오리를 이동시키는 메서드를 호출합니다.
        self.window.mainloop()  # Tkinter 이벤트 루프를 시작합니다.

    def load_images(self):
        # 왼쪽으로 이동하는 오리 이미지와 오른쪽으로 이동하는 오리 이미지를 리스트에 저장합니다.
        self.move_left_images = [tk.PhotoImage(file='duck-left.gif', format='gif -index %i' % i) for i in range(10)]
        self.move_right_images = [tk.PhotoImage(file='duck-right.gif', format='gif -index %i' % i) for i in range(10)]

    def initialize_window(self):
        self.window.config(background='black')  # 윈도우의 배경색을 검정색으로 설정합니다.
        # 윈도우를 검정색으로 투명하게 설정합니다. (macOS에서는 작동하지 않습니다.)
        self.window.wm_attributes('-transparentcolor', 'black')
        self.window.overrideredirect(True)  # 윈도우의 기본 동작을 무시하도록 설정합니다.
        self.window.attributes('-topmost', True)  # 윈도우를 최상위로 표시합니다.
        self.label = tk.Label(self.window, bd=0, bg='black')  # 라벨 위젯을 생성합니다.
        self.x = 1040  # 오리의 초기 x 좌표를 설정합니다.
        self.y = self.window.winfo_screenheight() - 126  # 오리의 초기 y 좌표를 설정합니다.
        self.label.configure(image=self.img)  # 라벨 위젯의 이미지를 설정합니다.
        self.label.pack()  # 라벨 위젯을 윈도우에 배치합니다.
        self.window.geometry('128x128+{}+{}'.format(self.x, self.y))  # 윈도우의 크기와 위치를 설정합니다.

    def change_frame(self, direction):
        # 프레임 변경 시간이 경과했는지 확인하여 이미지의 프레임을 변경합니다.
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
            self.frame_index = (self.frame_index + 1) % 5
            self.img = direction[self.frame_index]

    def change_direction(self):
        # 0과 1 사이의 무작위 수를 생성합니다.
        random_number = random.random()
        # 무작위 수가 0.5보다 작으면 오리의 이동 방향을 무작위로 변경합니다.
        if random_number < 0.5:
            self.dir = -self.dir

    def move_pet(self):
        # 마지막 방향 변경 이후 10초가 경과했는지 확인하여 오리의 이동 방향을 변경합니다.
        if time.time() > self.last_direction_change + 10:
            self.last_direction_change = time.time()
            self.change_direction()

        self.x = self.x + self.dir  # 오리의 x 좌표를 변경합니다.

        if self.dir < 0:
            direction = self.move_left_images  # 오리가 왼쪽으로 이동하는 경우 왼쪽으로 이동하는 이미지를 사용합니다.
        else:
            direction = self.move_right_images  # 오리가 오른쪽으로 이동하는 경우 오른쪽으로 이동하는 이미지를 사용합니다.

        self.change_frame(direction)  # 오리 이미지의 프레임을 변경합니다.

        # 오리가 화면을 벗어나면 이동 방향을 변경합니다.
        if self.x <= 0 or self.x >= (self.window.winfo_screenwidth() - 128):
            self.change_direction()

        self.window.geometry('128x128+{}+{}'.format(self.x, self.y))  # 윈도우의 위치를 변경합니다.
        self.label.configure(image=self.img)  # 라벨 위젯의 이미지를 변경합니다.
        self.label.pack() # 라벨 위젯 윈도우 배치
        self.window.after(10, self.move_pet)  # 주어진 시간(ms)이 지난 후에 move_pet 메서드를 호출합니다.
        self.window.lift()  # 윈도우를 최상위로 표시합니다.


if __name__ == "__main__":
    Duck()  # Duck 클래스의 인스턴스를 생성하여 오리를 만듭니다.
