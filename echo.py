#echo.py

def echo(text: str, repetitions: int = 6) -> str:
    """Imitate a real-world echo."""

    last_word = text.split()[-1]                        # Get the last word of the input text
    echo_part = last_word[-repetitions:]                # Get the last 'repetitions' characters of the last word
    
    result_lines = []
    
    while len(echo_part) > 0:
        result_lines.append(echo_part)                  # Append the current echo part to the result lines
        echo_part = echo_part[1:]                       # Remove the first character of the echo part for the next iteration
    
    result_lines.append(".")
    
    return "\n".join(result_lines)                      # Join the result lines with newline characters to create the final output


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))