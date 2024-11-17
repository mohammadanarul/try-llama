from ollama import Client

client = Client(host="http://localhost:11434")

while True:
    text = input("Enter text: ")
    if text == "exit":
        break
    output = client.generate(
        model="llama3.2",
        prompt=text,
        stream=False,
    )
    print(f"output: {output['response']}")
