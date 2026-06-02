import tkinter as tk
from tkinter import scrolledtext
import random

root = tk.Tk()

root.title("Movie Recommendation Assistant")

root.geometry("600x700")

root.config(bg="#0f172a")

movie_descriptions = {

    "john wick":
    "John Wick is an action thriller about a retired assassin seeking revenge after a personal tragedy.",

    "avengers: endgame":
    "Avengers: Endgame follows Marvel superheroes as they attempt to reverse the destruction caused by Thanos.",

    "mad max: fury road":
    "Mad Max: Fury Road is a post-apocalyptic action film filled with intense chases and survival battles.",

    "mission impossible":
    "Mission Impossible follows Ethan Hunt and his team handling dangerous secret missions.",

    "the dark knight":
    "The Dark Knight features Batman facing the Joker in one of the most iconic superhero films.",

    "spider-man: no way home":
    "Spider-Man: No Way Home explores the multiverse as Peter Parker faces villains from different universes.",

    "the mask":
    "The Mask is a comedy film about a man who gains magical powers from a mysterious mask.",

    "jumanji":
    "Jumanji is an adventure comedy where players get trapped inside a dangerous game world.",

    "free guy":
    "Free Guy follows a bank worker who discovers he is actually a character inside a video game.",

    "deadpool":
    "Deadpool is a comedy action superhero movie known for humor and breaking the fourth wall.",

    "home alone":
    "Home Alone is a comedy film about a boy defending his house from burglars during Christmas.",

    "the conjuring":
    "The Conjuring is a supernatural horror film based on paranormal investigations.",

    "insidious":
    "Insidious follows a family trying to save their son from supernatural forces.",

    "it":
    "IT is a horror movie about a terrifying clown haunting a town.",

    "annabelle":
    "Annabelle tells the story of a haunted doll causing paranormal events.",

    "a quiet place":
    "A Quiet Place is a horror thriller where silence is necessary for survival.",

    "titanic":
    "Titanic is a romantic drama set during the tragic sinking of the Titanic ship.",

    "la la land":
    "La La Land is a musical romantic drama about dreams, love, and ambition.",

    "the notebook":
    "The Notebook is a romantic drama about lifelong love and memories.",

    "me before you":
    "Me Before You tells the emotional story of a caregiver and a disabled man.",

    "pride and prejudice":
    "Pride and Prejudice is a classic romance based on Jane Austen's novel.",

    "interstellar":
    "Interstellar is a science fiction movie exploring space travel and survival of humanity.",

    "inception":
    "Inception is a sci-fi thriller about entering and controlling dreams.",

    "the matrix":
    "The Matrix follows a hacker discovering the reality of a simulated world.",

    "arrival":
    "Arrival is a sci-fi film about communicating with alien life forms.",

    "blade runner 2049":
    "Blade Runner 2049 explores artificial intelligence and futuristic society.",

    "se7en":
    "Se7en is a crime thriller involving serial murders based on the seven deadly sins.",

    "gone girl":
    "Gone Girl is a psychological thriller about a mysterious disappearance.",

    "shutter island":
    "Shutter Island follows a detective investigating a psychiatric facility.",

    "prisoners":
    "Prisoners is a thriller about the search for missing children.",

    "fight club":
    "Fight Club explores identity, society, and underground fighting culture.",

    "your name":
    "Your Name is an anime film about two teenagers mysteriously swapping bodies.",

    "spirited away":
    "Spirited Away is a fantasy anime about a girl trapped in a magical world.",

    "weathering with you":
    "Weathering With You tells the story of a girl who can control weather.",

    "a silent voice":
    "A Silent Voice focuses on friendship, bullying, and redemption.",

    "suzume":
    "Suzume is an adventure fantasy anime involving mysterious doors and disasters.",

    "jurassic park":
    "Jurassic Park is a sci-fi adventure featuring cloned dinosaurs in a theme park.",

    "pirates of the caribbean":
    "Pirates of the Caribbean follows pirate adventures on dangerous seas.",

    "avatar":
    "Avatar explores the world of Pandora and the conflict between humans and nature.",

    "indiana jones":
    "Indiana Jones follows an archaeologist searching for ancient treasures.",

    "the jungle book":
    "The Jungle Book tells the story of a boy raised in the jungle.",

    "the pursuit of happyness":
    "The Pursuit of Happyness is an inspiring story about struggle and determination.",

    "rocky":
    "Rocky follows an underdog boxer fighting for success.",

    "3 idiots":
    "3 Idiots is an inspirational comedy-drama about engineering students and education.",

    "ford v ferrari":
    "Ford v Ferrari tells the story of building a race car to challenge Ferrari.",

    "the social network":
    "The Social Network shows the creation and rise of Facebook."
}

def get_reply(user_message):

    user_message = user_message.lower()

    for movie in movie_descriptions:

        if movie in user_message:

            return movie_descriptions[movie]

    if "hello" in user_message or "hi" in user_message:

        return (
            "Hello. I can recommend movies based on genres like "
            "Action, Comedy, Horror, Romance, Sci-Fi, Anime, Thriller, "
            "Adventure, and Motivational."
        )

    elif "action" in user_message:

        movies = [

            "John Wick",
            "Avengers: Endgame",
            "Spider-Man: No Way Home",
            "Mad Max: Fury Road",
            "Mission Impossible",
            "The Dark Knight"
        ]

        return "Recommended Action Movies:\n\n" + "\n".join(movies)

    elif "comedy" in user_message:

        movies = [

            "The Mask",
            "Jumanji",
            "Free Guy",
            "Deadpool",
            "Home Alone"
        ]

        return "Recommended Comedy Movies:\n\n" + "\n".join(movies)

    elif "horror" in user_message:

        movies = [

            "The Conjuring",
            "Insidious",
            "IT",
            "Annabelle",
            "A Quiet Place"
        ]

        return "Recommended Horror Movies:\n\n" + "\n".join(movies)

    elif "romance" in user_message:

        movies = [

            "Titanic",
            "La La Land",
            "The Notebook",
            "Me Before You",
            "Pride and Prejudice"
        ]

        return "Recommended Romance Movies:\n\n" + "\n".join(movies)

    elif "sci-fi" in user_message or "science fiction" in user_message:

        movies = [

            "Interstellar",
            "Inception",
            "The Matrix",
            "Arrival",
            "Blade Runner 2049"
        ]

        return "Recommended Sci-Fi Movies:\n\n" + "\n".join(movies)

    elif "thriller" in user_message:

        movies = [

            "Se7en",
            "Gone Girl",
            "Shutter Island",
            "Prisoners",
            "Fight Club"
        ]

        return "Recommended Thriller Movies:\n\n" + "\n".join(movies)

    elif "anime" in user_message:

        movies = [

            "Your Name",
            "Spirited Away",
            "Weathering With You",
            "A Silent Voice",
            "Suzume"
        ]

        return "Recommended Anime Movies:\n\n" + "\n".join(movies)

    elif "adventure" in user_message:

        movies = [

            "Jurassic Park",
            "Pirates of the Caribbean",
            "Avatar",
            "Indiana Jones",
            "The Jungle Book"
        ]

        return "Recommended Adventure Movies:\n\n" + "\n".join(movies)

    elif "motivational" in user_message or "inspiring" in user_message:

        movies = [

            "The Pursuit of Happyness",
            "Rocky",
            "3 Idiots",
            "Ford v Ferrari",
            "The Social Network"
        ]

        return "Recommended Motivational Movies:\n\n" + "\n".join(movies)

    elif "bye" in user_message:

        return "Goodbye. Enjoy your movies."

    else:

        return (
            "I can recommend movies from genres like:\n\n"
            "Action\n"
            "Comedy\n"
            "Horror\n"
            "Romance\n"
            "Sci-Fi\n"
            "Thriller\n"
            "Anime\n"
            "Adventure\n"
            "Motivational"
        )

def send_message():

    message = user_input.get().strip()

    if message == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(
        tk.END,
        f"\nYou: {message}\n"
    )

    reply = get_reply(message)

    chat_area.insert(
        tk.END,
        f"Bot: {reply}\n"
    )

    chat_area.config(state=tk.DISABLED)

    chat_area.yview(tk.END)

    user_input.delete(0, tk.END)

title = tk.Label(

    root,

    text="Movie Recommendation Assistant",

    font=("Arial", 22, "bold"),

    bg="#0f172a",

    fg="white"
)

title.pack(pady=20)

chat_area = scrolledtext.ScrolledText(

    root,

    wrap=tk.WORD,

    font=("Arial", 12),

    bg="#1e293b",

    fg="white",

    insertbackground="white",

    relief="flat"
)

chat_area.pack(

    padx=20,

    pady=10,

    fill=tk.BOTH,

    expand=True
)

chat_area.insert(

    tk.END,

    "Bot: Hello. Ask me for movie recommendations based on genres or ask about a specific movie.\n"
)

chat_area.config(state=tk.DISABLED)

input_frame = tk.Frame(

    root,

    bg="#0f172a"
)

input_frame.pack(

    fill=tk.X,

    padx=20,

    pady=20
)

user_input = tk.Entry(

    input_frame,

    font=("Arial", 13),

    bg="#1e293b",

    fg="white",

    insertbackground="white",

    relief="flat"
)

user_input.pack(

    side=tk.LEFT,

    fill=tk.X,

    expand=True,

    ipady=12,

    padx=(0,10)
)

send_button = tk.Button(

    input_frame,

    text="Send",

    font=("Arial", 12, "bold"),

    bg="#2563eb",

    fg="white",

    relief="flat",

    padx=20,

    pady=10,

    cursor="hand2",

    command=send_message
)

send_button.pack(side=tk.RIGHT)

root.bind(

    "<Return>",

    lambda event: send_message()
)

root.mainloop()