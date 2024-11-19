def calculate_ideal_weight(gender, height_cm):
    # Validacija unosa za visinu
    if not isinstance(height_cm, (int, float)) or height_cm <= 0:
        raise ValueError("Height must be a positive number.")

    # Validacija unosa za pol
    if gender not in ["male", "female"]:
        raise ValueError("Gender must be 'male' or 'female'.")

    # Izračunavanje korekcije
    correction = height_cm - 152

    # Idealna težina za muškarce i žene
    if gender == "male":
        ideal_weight = 48
        if correction > 0:
            ideal_weight += correction * 1.1
    elif gender == "female":
        ideal_weight = 45.5
        if correction > 0:
            ideal_weight += correction * 0.9

    # Zaokruživanje rezultata na 2 decimale
    return round(ideal_weight, 2)
