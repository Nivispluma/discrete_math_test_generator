def progress(count, total):
    bar_length = 60
    filled_length = int(round(bar_length * count / float(total)))

    percents = round(100.0 * count / float(total))
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    print(f"[{bar}] - {percents}")
    return
