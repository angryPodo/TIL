def get_user_input(prompt):
    return int(input(prompt))

def print_section_header(header):
    print(header.center(30, '-'))

month, date = map(int, input("달,일: ").split())

# POS 매출 입력
card = get_user_input("카드: ")
cash = get_user_input("현금: ")
kiosk = get_user_input("키오스크: ")

# 배달 매출 입력
baemin = get_user_input("배민: ")
yogio = get_user_input("요기요: ")
coupang = get_user_input("쿠팡: ")

# 총합 매출 계산
pos_total = card + cash + kiosk
delivery_total = baemin + yogio + coupang

# 배달 내용 입력
delivery_try = get_user_input("배달건수: ")
delivery_cash = get_user_input("배달현금: ")
delivary_pay = get_user_input("배달료: ")
delivary_remain = get_user_input("배달료 남은거: ")

# 계좌이체 입력
send_cash = get_user_input("계좌이체: ")

# 서초점 로스 입력
los_human = get_user_input("직원로스: ")
service_scon = get_user_input("배달스콘: ")
close_scon = get_user_input("마감스콘: ")
trash = get_user_input("폐기: ")
discount_part = get_user_input("직원할인: ")
using_point = get_user_input("포인트사용: ")

# 로스 총금액 계산
los_total = los_human + close_scon + service_scon + trash + using_point + discount_part

# 결과 출력
print_section_header("파운데이 서초점")
print(f"2024년 {month}월 {date}일")

# 1. 포스 매출
print_section_header("포스매출")
print(f"- 카드: {card}원\n- 현금: {cash}원\n- 키오스크: {kiosk}원\n- 기타: 0원")

# 2. 배달 매출
print_section_header("배달 매출")
print(f"- 배달의민족: {baemin}원\n- 요기요: {yogio}원\n- 쿠팡이츠: {coupang}원\n- 기타: 0원\n- 배달 Total: {delivery_total}원")

# 3. 총합 매출
print_section_header("총합 매출")
print(f"- {pos_total}원")

# 4. 배달 내용
print_section_header("배달 내용")
print(f"- 배달건수: {delivery_try}건\n- 배달현금: {delivery_cash}건\n- 배달료: {delivary_pay}원\n- 배달페이 남은 적립금: {delivary_remain}원")

# 5. 계좌이체
print_section_header("계좌이체")
print(f"- 메뉴&가격: {send_cash}원")

# 6. 서초점 로스
print_section_header("서초점 로스")
print(f"- 직원: {los_human}원\n- 배달 서비스 스콘: {service_scon}원\n- 리뷰&서비스: 0원\n- 마감스콘: {close_scon}원\n- 폐기: {trash}원\n- 기타: 0원\n- 직원할인: {discount_part}원\n- 포인트사용: {using_point}원")
print(f"서초점 로스 총금액: {los_total}원")
