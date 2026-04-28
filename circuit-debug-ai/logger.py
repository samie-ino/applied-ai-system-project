from agent import diagnose
from evaluator import verify
from formatter import format_output
from logger import log_interaction

def main():
    print("⚡ Circuit Debugging AI Assistant\n")

    user_input = input("Describe your circuit issue: ")

    diagnosis = diagnose(user_input)
    evaluation, confidence = verify(user_input, diagnosis)

    output = format_output(user_input, diagnosis, evaluation, confidence)

    print(output)

    log_interaction(user_input, diagnosis, evaluation, confidence)

if __name__ == "__main__":
    main()
