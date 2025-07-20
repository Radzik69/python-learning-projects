import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FlashCardApiResponse:
    def __init__(self):
        self.available_categories = {
            9: "General Knowledge",
            10: "Books",
            11: "Film",
            12: "Music",
            13: "Musicals & Theatres",
            14: "Television",
            15: "Video Games",
            16: "Board Games",
            17: "Science & Nature",
            18: "Computers",
            19: "Mathematics",
            20: "Mythology",
            21: "Sports",
            22: "Geography",
            23: "History",
            24: "Politics",
            25: "Art",
            26: "Celebrities",
            27: "Animals",
            28: "Vehicles",
            29: "Comics",
            30: "Gadgets",
            31: "Japanese Anime & Manga",
            32: "Cartoon & Animations"
        }
        self.available_difficulties = ["easy", "medium", "hard"]

    def run(self):
        category = self.get_category()
        difficulty = self.get_difficulty()
        self.get_flashcard(category, difficulty)

    def get_category(self):
        print("Available categories:")
        for number, name in self.available_categories.items():
            print(f"{number}: {name}")

        category = input("Choose a category number from the list above: ")
        try:
            category = int(category)
            if category in self.available_categories:
                return category
            else:
                print("Incorrect Category")
                return self.get_category()
        except ValueError:
            print("Please enter a valid number")
            return self.get_category()

    def get_difficulty(self):
        print("Available difficulties:", self.available_difficulties)
        difficulty = input("Choose a difficulty from the list above: ").lower()
        if difficulty in self.available_difficulties:
            return difficulty
        else:
            print("Incorrect Difficulty")
            return self.get_difficulty()

    def get_flashcard(self, category, difficulty):
        response = requests.get(
            f"https://opentdb.com/api.php?amount=1&category={category}&difficulty={difficulty}&type=multiple"
        )
        data = response.json()
        return data

class CreateGUI:
    def __init__(self):
        self.api = FlashCardApiResponse()
        self.root = tk.Tk()
        self.root.geometry("600x800")
        self.root.title("Flashcard App")

        self.label = tk.Label(
            self.root,
            text="Flashcard App",
            bg="grey",
            font=("Arial", 20),
            padx=15,
            pady=15,
        )
        self.label.pack()


        self.label_category = tk.Label(self.root, text="Select Category :", font=("Arial", 10))
        self.label_category.pack(padx=10, pady=25)
        self.category_var = tk.StringVar()
        self.category_chosen = ttk.Combobox(self.root, width=27, textvariable=self.category_var,state="readonly")
        self.category_chosen['values'] = list(self.api.available_categories.values())
        self.category_chosen.pack()
        self.category_chosen.current(0)

        self.label_difficulty = tk.Label(self.root, text="Select Difficulty :", font=("Arial", 10))
        self.label_difficulty.pack(padx=10, pady=25)
        self.difficulty_var = tk.StringVar()
        self.difficulty_chosen = ttk.Combobox(self.root, width=27, textvariable=self.difficulty_var,state="readonly")
        self.difficulty_chosen['values'] = list(self.api.available_difficulties)
        self.difficulty_chosen.pack()
        self.difficulty_chosen.current(0)

        self.start_button = tk.Button(
            self.root,
            command=self.start_flashcard_questions,
            text="Start with options above",
            activebackground="red",
            activeforeground="lightgrey",
            cursor="arrow",
        )
        self.start_button.pack(padx=20, pady=20)

        self.root.mainloop()

    def start_flashcard_questions(self):
        selected_category_name = self.category_chosen.get()
        global selected_difficulty
        selected_difficulty = self.difficulty_chosen.get()
        global category_number
        global api_response
        global past_questions
        global question_number

        for number, name in self.api.available_categories.items():
            if name == selected_category_name:
                category_number = number
                break

        if category_number is not None:
            past_questions = {}
            api_response = self.api.get_flashcard(category_number, selected_difficulty)
            question_number=1
            past_questions[f"{question_number}"] = [api_response['results'][0]['question'],api_response['results'][0]['correct_answer']]
        else:
            print("Error: Category not found.")

        self.label_category.destroy()
        self.label_difficulty.destroy()
        self.category_chosen.destroy()
        self.difficulty_chosen.destroy()
        self.start_button.destroy()

        self.questionanswer_button = tk.Button(
            self.root,
            command=self.reveal_answer,
            text=api_response['results'][0]['question'],
            activebackground="green",
            activeforeground="red",
            cursor="hand2",
            bd=40,
            height=10,
            width=25,
            font=("Arial",18),
            wraplength=200

        )
        self.questionanswer_button.pack(padx=10,pady=10)

        self.buttons_frame = tk.Frame(
            self.root,
            bg="grey",
            bd=10,
            cursor="arrow",
            height=10,
            width=30,
            highlightcolor="blue",
        )

        self.buttons_frame.pack(padx=10,pady=10)

        self.next_question_button = tk.Button(
            self.buttons_frame,
            bg="lightblue",
            height=10,
            width=18,
            text="Next question",
            font=("Arial",14),
            command=self.next_question
        )

        self.next_question_button.pack(side=tk.RIGHT,padx=10,pady=10)

        self.previous_question_button = tk.Button(
            self.buttons_frame,
            bg="lightblue",
            height=10,
            width=18,
            text="Previous question",
            font=("Arial", 14),
            command=self.previous_question
        )

        self.previous_question_button.pack(side=tk.LEFT,padx=10,pady=10)

        self.current_question = [api_response['results'][0]['question'], api_response['results'][0]['correct_answer']]


    def reveal_answer(self):
        self.questionanswer_button.config(text=self.current_question[1])
        self.questionanswer_button.config(command=self.go_back_to_question)

    def go_back_to_question(self):
        self.questionanswer_button.config(text=self.current_question[0])
        self.questionanswer_button.config(command=self.reveal_answer)

    def next_question(self):
        global api_response
        global question_number
        try:
            api_response = self.api.get_flashcard(category_number, selected_difficulty)
            self.current_question = [api_response['results'][0]['question'],
                                     api_response['results'][0]['correct_answer']]
            self.questionanswer_button.config(
                text=self.current_question[0],
                command=self.reveal_answer
            )
            question_number += 1
            past_questions[question_number] = self.current_question
        except Exception:
            messagebox.showinfo(title='Error',
                                message='You switched to next question too fast, and API didn\'t respond in time')

    def previous_question(self):
        global question_number
        if question_number > 1:
            question_number -= 1
            prev_q = past_questions[question_number]
            self.current_question = prev_q
            self.questionanswer_button.config(
                text=prev_q[0],
                command=lambda: self.show_previous_answer(prev_q)
            )
        else:
            messagebox.showinfo(title='Info', message='No previous questions.')

    def show_previous_answer(self, prev_q):
        self.questionanswer_button.config(text=prev_q[1])
        self.questionanswer_button.config(command=lambda: self.show_previous_question(prev_q))

    def show_previous_question(self, prev_q):
        self.questionanswer_button.config(text=prev_q[0])
        self.questionanswer_button.config(command=lambda: self.show_previous_answer(prev_q))


CreateGUI()

