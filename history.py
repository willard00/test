history = []

def record(operation, result):
    history.append({"operation": operation, "result": result})

def show_history():
    if not history:
        print("No history yet.")
        return
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry['operation']} = {entry['result']}")

def clear_history():
    history.clear()
    print("History cleared.")
