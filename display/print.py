import time

def displayText(text: str, speed: float = 0.02):
    """Displays text with a typewriter effect."""
    for char in text:
        print(char, end="")
        time.sleep(speed)
    print("")


if __name__ == "__main__":
    displayText("Hello, this is a test")
