from openai import OpenAI

client=OpenAI(
    api_key="#######################################kFJ4dHb8jILrNhT_u3Q-A7h3Azr2WWZikwSr0avfTyj9EYHKt5IIknjas6_OmIqrqOTxd16h1_a8A"

)

response = client.responses.create(
    model="gpt-5",
    input="You are a bot named jarvis which works like alexa and your command is {command}"
)

print(response.output_text)
