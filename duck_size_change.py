from PIL import Image # pip install Pillow

# 이미지 열기
image_left = Image.open("duck-left.gif")

# 이미지 크기 조정
new_width = image_left.width * 2  # 기존 너비의 2배로 조정
new_height = image_left.height * 2 # 높이는 그대로 유지
resized_image_left = image_left.resize((new_width, new_height))

# 조정된 이미지 저장
resized_image_left.save("resized_duck-left.gif")


# 이미지 열기
image_right = Image.open("duck-right.gif")

# 이미지 크기 조정
new_width = image_right.width * 2  # 기존 너비의 2배로 조정
new_height = image_right.height * 2 # 높이는 그대로 유지
resized_image_right = image_right.resize((new_width, new_height))

# 조정된 이미지 저장
resized_image_right.save("resized_duck-left.gif")