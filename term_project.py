import pymysql
from time import sleep
from datetime import datetime

con = pymysql.connect(host='192.168.113.3', user='yglee', password='1234',
                      database='daily_employment', port=4567, charset='utf8', autocommit=True)

cur = con.cursor()


def worker_regist():
    print("근무자 번호, 이름, 휴대폰 번호(010-XXXX-XXXX), 자격증 보유여부(O,X), 생년월일을 입력해주세요.")
    wknum, wkname, wkphone, license, birth = input("입력해주세요 : ").split()

    try:
        print(
            f'근무자 번호={wknum} 이름={wkname} 휴대폰 번호={wkphone} 자격증={license} 생년월일={birth}')
        print("정확히 입력하셨습니까? y/n")
        sel = input()
        if sel == 'y':
            sql = "insert into worker values(%s,%s,%s,%s,%s)"
            vals = (wknum, wkname, wkphone, license, birth,)
            cur.execute(sql, vals)
            print("[등록완료]")
        elif sel == 'n':
            print("등록취소")
        else:
            print("잘못입력하셨습니다.")
        sleep(5)
    except pymysql.err.IntegrityError as e:
        print(e)


def firstpage():
    print("-------------  DB 일용 근로 계약  -------------")
    print("                 1.근로자 전용                 ")
    print("                 2.관리자 전용                 ")
    print("                 99.사용 종료                  ")
    print("----------------------------------------------")
    menu = input("사용자 선택: ")
    return int(menu)


def workerpage():
    while (1):
        print("-------------  DB 일용 근로 계약  -------------")
        print(" [근무자 관리]                                 ")
        print(" 1. 근무자 등록  2. 근무자 삭제 3. 총 급여      ")
        print("\n")
        print(" [근무 관리]                                   ")
        print(" 4. 근무 등록    5. 근무 조회  6. 근무 삭제     ")
        print("\n")
        print(" [근무 예약 관리]                              ")
        print(" 7. 예약 등록    8. 예약 조회  9. 예약 삭제     ")
        print("\n")
        print("                  99.종료하기                  ")
        print("----------------------------------------------")
        w_menu = input("메뉴선택: ")

        if w_menu == '1':
            worker_regist()
        elif w_menu == '2':

            break
        elif w_menu == '3':
            break
        elif w_menu == '4':
            break
        elif w_menu == '5':
            break
        elif w_menu == '6':
            break
        elif w_menu == '7':
            break
        elif w_menu == '8':
            break
        elif w_menu == '99':
            break
    return 0


def managerpage():
    while (1):
        print("-------------  DB 일용 근로 계약  -------------")
        print(" [근무자 관리]                                 ")
        print(" 1. 전체 근무자 조회                            ")
        print(" 2. 전체 근무자별 급여 조회                     ")
        print("                                                ")
        print(" [근무 관리]                                   ")
        print(" 3. 날짜별 근무 조회                            ")
        print(" 4. 담당자 별 근무 조회                         ")
        print(" 5. 근무자 별 근무 조회                         ")
        print(" 6. 업무 별 근무 조회                          ")
        print(" 7. 예약된 근무 조회                          ")
        print("                                                ")
        print(" [담당자 관리]                              ")
        print(" 8.담당자 등록                                ")
        print(" 9.업무별 담당자 조회                          ")
        print(" 10.회사별 담당자 조회                          ")
        print("                                                ")
        print(" [회사 관리]                              ")
        print(" 11.회사 등록                          ")
        print(" 12.회사별 실적 조회                        ")
        print("                                                ")
        print(" [업무 관리]                              ")
        print(" 13.업무 종류 조희                            ")
        print(" 14.업무 가격 수정                            ")

        print("                  99.종료하기                  ")
        print("----------------------------------------------")
        m_menu = input("메뉴선택: ")

        if m_menu == '1':
            break
        elif m_menu == '2':
            break
        elif m_menu == '3':
            break
        elif m_menu == '4':
            break
        elif m_menu == '5':
            break
        elif m_menu == '6':
            break
        elif m_menu == '7':
            break
        elif m_menu == '8':
            break
        elif m_menu == '9':
            break
        elif m_menu == '10':
            break
        elif m_menu == '11':
            break
        elif m_menu == '12':
            break
        elif m_menu == '13':
            break
        elif m_menu == '14':
            break
        elif m_menu == '99':
            break
    return 0


def run():

    menu = firstpage()
    if menu == 1:
        workerpage()
    elif menu == 2:
        managerpage()
    elif menu == 99:
        print("사용을 종료합니다.")
        con.close()
        return 0


run()
