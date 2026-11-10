import json
from pathlib import Path
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
        self.load_data()

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
                self.add_quiz()
            elif choice == "3":
                self.list_quizzes()
            elif choice == "4":
                print(f"🏆 최고 점수: {self.best_score}점")
            elif choice == "5":
                self.save_data()
                print("게임을 종료합니다.")
                break
            else:
                print("1~5 사이의 숫자를 입력하세요.")

    def play_quiz(self):
        score = 0

        for quiz in self.quizzes:
            quiz.display()
            answer = input("정답 번호 (1~4): ").strip()

            if answer.isdigit() and quiz.check_answer(int(answer)):
                print("정답입니다! 🎉")
                score += 1
            else:
                print("오답입니다!")

        print(f"\n최종 점수: {score}/{len(self.quizzes)}")

        if score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다! 🎉")
            self.save_data()


    def add_quiz(self):
        question = input("새로운 문제를 입력하세요: ").strip()

        if not question:
            print("문제를 입력해야 합니다.")
            return

        choices = []

        for i in range(1, 5):
            choice = input(f"{i}번 선택지: ").strip()

            if not choice:
                print("선택지는 비워둘 수 없습니다.")
                return

            choices.append(choice)

        answer = input("정답 번호 (1~4): ").strip()

        if answer not in ["1", "2", "3", "4"]:
            print("정답은 1~4 중에서 선택하세요.")
            return

        self.quizzes.append(Quiz(question, choices, int(answer)))
        print("퀴즈가 추가되었습니다! 🎉")
        self.save_data()

    def list_quizzes(self):
        print("\n===== 퀴즈 목록 =====")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for i, quiz in enumerate(self.quizzes, 1):
            print(f"\n{i}. {quiz.question}")

            for j, choice in enumerate(quiz.choices, 1):
                print(f"   {j}. {choice}")

            print(f"   정답: {quiz.answer}번") 


    def save_data(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score
        }

        try:
            path = Path(__file__).resolve().parent / "state.json"

            with open(path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("데이터 저장 완료!")

        except OSError as error:
            print(f"데이터 저장 실패: {error}")

    def load_data(self):
        path = Path(__file__).resolve().parent / "state.json"

        if not path.exists():
            return

        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)

            quizzes = [
                Quiz(item["question"], item["choices"], item["answer"])
                for item in data["quizzes"]
            ]

            best_score = data["best_score"]

            if not isinstance(best_score, int) or best_score < 0:
                raise ValueError("최고 점수 형식 오류")

            self.quizzes = quizzes
            self.best_score = best_score

            print("저장된 데이터를 불러왔습니다!")

        except (OSError, ValueError, TypeError, KeyError) as error:
            print(f"데이터 불러오기 실패: {error}")
            print("기본 퀴즈로 시작합니다.")