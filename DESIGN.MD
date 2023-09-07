## Design

The example Azure PromptFlow chat application expects following format:
```json
{ "chat_history":
    [
    {
        "inputs": {
        "chat_input": "Hi"
        },
        "outputs": {
        "chat_output": "Hello! How can I assist you today?"
        }
    },
    {
        "inputs": {
        "chat_input": "what are good vegetables to farm on autum?"
        },
        "outputs": {
        "chat_output": "There are several vegetables that can be farmed during the autumn season. Some examples include broccoli, cauliflower, cabbage, kale, spinach, lettuce, radishes, turnips, carrots, beets, and Brussels sprouts. These vegetables are typically cold-tolerant and can withstand the cooler temperatures of the autumn season. It's important to note that the specific vegetables that can be grown during autumn may vary depending on your location and climate."
        }
    }
    ],
    "chat_input":"Ok my location is very north, does that change anything?"
}
```
The response is:
```json
{ "chat_output": "OAI Response .... "}
```
