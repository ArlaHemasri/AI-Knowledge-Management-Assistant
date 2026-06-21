from workflows.knowledge_manager import generate_knowledge

def main():
    topic = input("Enter knowledge topic: ")
    content = generate_knowledge(topic)

    print("\n--- Generated Knowledge Content ---\n")
    print(content)

if __name__ == "__main__":
    main()