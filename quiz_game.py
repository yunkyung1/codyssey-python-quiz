from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0

    def show_menu(self):
        print("\n===== 나만의 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def run(self):
        while True:
            self.show_menu()
            choice = input("메뉴 선택 (1~5): ").strip()

            if choice == "1":
                print("퀴즈 풀기 준비 중")
            elif choice == "2":
                print("퀴즈 추가 준비 중")
            elif choice == "3":
                print("퀴즈 목록 준비 중")
            elif choice == "4":
                print("점수 확인 준비 중")
            elif choice == "5":
                print("게임을 종료합니다.")
                break
            else:
                print("1~5 사이의 숫자를 입력하세요.")