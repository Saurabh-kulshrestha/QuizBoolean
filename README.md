# ❓ QuizBoolean – A Python True/False Console Quiz Game

A fun and interactive terminal-based quiz game built with Python. The project tests your general knowledge with a series of **True/False** questions, tracks your score in real-time, and ends with a final result. Clean structure, object-oriented design, and a polished console UI make it both engaging and educational.

---

## 🚀 Features

- ✅ **True/False Questions** from a predefined question bank
- ⚖️ **Real-time Score Tracking** as you progress through each question
- ⚡ **Instant Feedback** on your answers
- 🔄 **Looped Game Flow** till all questions are answered
- ⚙️ **Object-Oriented Design** using `QuizBrain` and `Question` classes
- 🎨 ASCII Art logo for visual appeal in the terminal

---

## 🧰 Project Structure

```bash
QuizBoolean/
├── art.py              # Stores ASCII art/logo of the game
├── data.py             # Contains the quiz question data (text + answer)
├── main.py             # Entry point; game loop and orchestration logic
├── question_model.py   # Defines the Question class structure
├── quiz_brain.py       # Contains QuizBrain class to manage quiz logic
├── screenshot.png      # Console preview screenshot
└── README.md           # This file
```

---

## 📅 How It Works

1. **Run** the game:

   ```bash
   python main.py
   ```

2. **Answer** each question with `True` or `False`

3. **Get feedback** immediately: Right or Wrong

4. **Track your score** after each response

5. **See final score** when quiz ends

---

## 🗃️ Sample Output

```
Welcome to the QuizBoolean Game!
Q.1: Is a dog a mammal? (True/False): True
Correct! ✅
Current Score: 1/1
...
Q.10: The Lego Group was founded in 1932. (True/False): False
Wrong! ❌
Final Score: 7/10
```

---

## 🥇 What I Learned

- Implementing **Object-Oriented Programming** in Python
- Designing a **modular quiz system** with reusable classes
- Managing game flow with clear state transitions
- Structuring Python files for better project clarity
- Creating interactive **terminal UIs** with feedback and scoring

---

## 👨‍💼 Developer

**Saurabh Kulshrestha**\
*Python Learner | Terminal Game Builder | Focused on Logic Building*
---