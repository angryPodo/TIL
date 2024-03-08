from PIL import Image
import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

# 사용자에게 파일 대화상자 표시
root = tk.Tk()
root.withdraw()  # 메인 창 숨기기

# 파일 대화상자를 통해 이미지 파일 선택
file_path = filedialog.askopenfilename(title="디지몬 선택")

if file_path:
    # 선택한 이미지 파일을 이용하여 프로그램을 실행

    # 바탕화면 경로 가져오기
    desktop_path = os.path.join(str(Path.home()), 'Desktop')

    # 원본 이미지 파일 이름 (확장자 제외)
    original_image_name = os.path.splitext(os.path.basename(file_path))[0]

    # 이미지 열기
    img = Image.open(file_path)

    # 이미지의 가로 길이와 높이 가져오기
    width, height = img.size

    # 가로와 세로 분할 수
    horizontal_divisions = 3
    vertical_divisions = 4

    # 가로와 세로 분할된 이미지의 너비와 높이 계산
    horizontal_segment_width = width // horizontal_divisions
    vertical_segment_height = height // vertical_divisions

    # 이미지를 가로로 3분할
    horizontal_images = []
    for i in range(horizontal_divisions):
        left = i * horizontal_segment_width
        right = (i + 1) * horizontal_segment_width
        segment = img.crop((left, 0, right, height))
        horizontal_images.append(segment)

    # 각 가로 분할 이미지를 세로로 4분할
    result_images = []
    for i, image in enumerate(horizontal_images):
        for j in range(vertical_divisions):
            top = j * vertical_segment_height
            bottom = (j + 1) * vertical_segment_height
            segment = image.crop((0, top, horizontal_segment_width, bottom))
            result_images.append(segment)

    # 이미지를 원하는 순서대로 재배열 (1, 5, 7, 11, 5, 12, 5, 12, 5, 9, 3, 10, 6, 4, 9)
    rearranged_images = [result_images[i-1] for i in [1, 5, 7, 11, 5, 12, 5, 12, 5, 9, 3, 10, 6, 4, 9]]

    # 이미지를 세로로 합치기
    merged_height = height * vertical_divisions
    merged_image = Image.new('RGB', (horizontal_segment_width, merged_height))

    y_offset = 0
    for segment in rearranged_images:
        merged_image.paste(segment, (0, y_offset))
        y_offset += segment.height

    # 마지막 이미지를 제거하여 최종 이미지의 크기를 조정
    cropped_image = merged_image.crop((0, 0, horizontal_segment_width, merged_height - segment.height))

    # 이미지를 바탕화면에 PNG 형식으로 저장
    save_path = os.path.join(desktop_path, f'{original_image_name}_cropped.png')
    cropped_image.save(save_path, 'PNG')
else:
    print("만들게 없네....")

