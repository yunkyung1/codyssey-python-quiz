from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = [
            Quiz("Python은 어떤 언어인가요?",
                 ["프로그래밍 언어", "운영체제", "웹 브라우저", "게임기"], 1),

            Quiz("Python에서 출력할 때 사용하는 함수는?",
                ["input()", "print()", "len()", "int()"], 2),

            Quiz("Python에서 목록을 저장하는 자료형은?",
                ["str", "int", "list", "bool"], 3),

            Quiz("Python에서 조건문에 사용하는 키워드는?",
                ["for", "while", "if", "def"], 3),

            Quiz("Python 파일의 확장자는?",
                [".txt", ".html", ".json", ".py"], 4)
        ]       
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
                self.play_quiz()
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

    def play_quiz(self):
        for quiz in self.quizzes:
            quiz.display()
            answer = input("정답 번호 (1~4): ").strip()

            if answer.isdigit() and quiz.check_answer(int(answer)):
                print("정답입니다! 🎉")
            else:
                print("오답입니다!")