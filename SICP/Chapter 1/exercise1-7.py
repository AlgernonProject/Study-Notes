if __name__ == "__main__":
    x = 2e50
    guess = 1.0
    for i in range(150):
        print("guess: {:.20} ; guess^2: {:.15} ; error: {:.15}".format(
            guess,
            guess*guess,
            abs(guess*guess - x)
        ))
        guess = (guess + (x / guess))/2