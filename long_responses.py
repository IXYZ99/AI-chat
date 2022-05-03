import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_NAME = "My name is The SYSTEM!"
R_FUCK = "Fuck you too!"

def why():
		response = ["Cause you are idiot! ",
		            "...",
		            "Why?"][
		    random.randrange(3)]
		return response
def unknown():
    response = ["Can You Say That Again! ",
                "...",
                "What does that mean?"][
        random.randrange(3)]
    return response
