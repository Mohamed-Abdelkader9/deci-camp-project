from codes import list

print("Welcome to VitaSync")
print("")
print("")

def chat_with_user():
    print("Welcome to the habit chatbot!")
    user_input = input("What's your bad habit? ")

    while True:
        # Tokenize user input
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
        model_name = "t5-base"
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        inputs = tokenizer.encode_plus(
            user_input,
            add_special_tokens=True,
            max_length=512,
            return_attention_mask=True,
            return_tensors="pt"
        )

        # Generate response
        outputs = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=128,
            num_beams=4,
            no_repeat_ngram_size=2,
            early_stopping=True
        )

        # Convert response to text
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Print response
        print("Chatbot:", response)

        # Ask user for next input
        user_input = input("You: ")

def program():
    while True:
        name = input("What's your name?")
        if name.isalpha():  # Check if the input contains only letters
            name = name.upper()
            break
        else:
            print("Invalid input. Please enter your name.")
    print(f"Hello {name}")

    while True:
        code = input("enter your cash code:")
        if code in list:
            print("all done")
            break
        elif code not in list:
            print("invalid code")

    print("Now, let's talk about your habits...")
    chat_with_user()

while True:
    try:
        age = int(input("Enter your age:"))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if age in range(13, 19):
    print("HI")
    program()
else:
    print("you are not in the age range (we target the teens)")