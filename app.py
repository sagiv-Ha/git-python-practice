from datetime import datetime

def greet(name):
    current_time = datetime.now().strftime("%H:%M")
    return f"Hello, !!!{name}!!! The current time is {current_time}"


if __name__ == "__main__":
    user = "Devops2026"
    print(greet(user))
