from rag_memory import JOHN_PROFILE

def retrieve_facts(message: str) -> list[str]:
    relevant = []

    for hobby in JOHN_PROFILE["hobbies"]:
        if hobby.lower() in message.lower():
            relevant.append(f"John loves {hobby}.")

    if "age" in message.lower():
        relevant.append(f"John is {JOHN_PROFILE['age']} years old.")

    if "UK" in message or "british" in message.lower():
        relevant.append("John is from the UK.")

    return relevant