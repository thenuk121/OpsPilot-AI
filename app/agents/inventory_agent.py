from ollama import chat

from tools.inventory_tools import check_low_stock


def ask_model(user_message):
    messages = [
        {
            "role": "system",
            "content": (
                "You are the inventory assistant for OpsPilot AI. "
                "Use the available tools whenever you need real inventory data. "
                "Never invent inventory information."
            )
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    # Ask the model what it wants to do
    response = chat(
        model="qwen3:4b",
        messages=messages,
        tools=[check_low_stock]
    )

    # Save the model's response in the conversation
    messages.append(response.message)

    # Check whether the model requested a tool
    if response.message.tool_calls:

        for tool_call in response.message.tool_calls:

            if tool_call.function.name == "check_low_stock":

                # Actually execute our Python function
                result = check_low_stock()

                # Give the result back to the model
                messages.append(
                    {
                        "role": "tool",
                        "tool_name": "check_low_stock",
                        "content": result
                    }
                )

        # Ask Qwen to interpret the tool result
        final_response = chat(
            model="qwen3:4b",
            messages=messages,
            tools=[check_low_stock]
        )

        return final_response.message.content

    # No tool was required
    return response.message.content