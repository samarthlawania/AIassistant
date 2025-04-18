def parse_command(user_input):
    user_input = user_input.lower()

    if "play music" in user_input or "play song" in user_input:
        return {"type": "music", "query": user_input.replace("play", "").strip()}
    elif "generate image" in user_input or "draw" in user_input:
        return {"type": "image", "prompt": user_input}
    elif "email" in user_input or "write mail" in user_input:
        return {"type": "email", "prompt": user_input, "tone": "formal"}
    else:
        return {"type": "chat", "prompt": user_input}
