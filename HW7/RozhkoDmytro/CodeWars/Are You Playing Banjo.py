def are_you_playing_banjo(name: str):
    return (
        f"{name} plays banjo"
        if name[0].lower() == "r"
        else f"{name} does not play banjo"
    )
