text = ("On a quiet night, Sarah walked through the garden, gazing at the endless sky. "
        "The wind felt Soft as it brushed against her face, whispering Tales of distant galaxies. "
        "Along the path, a lantern flickered, reminding her of childhood Adventures spent wishing "
        "upon the glowing moon. In the stillness, she realized that among all the chaos of life, "
        "there will always be a Reason to look up — a shining reminder that hope never fades.")

pattern = "STAR"
positions = {ch: [] for ch in pattern}

for i, ch in enumerate(text):
    if ch in positions:
        positions[ch].append(i)

for ch in pattern:
    if positions[ch]:
        print(f"{ch} = {', '.join(map(str, positions[ch]))}")
    else:
        print(f"{ch} not found in text.")
