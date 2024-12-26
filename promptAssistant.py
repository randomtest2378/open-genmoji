import requests
import json
import os


def get_prompt_response(user_prompt: str) -> str:
    # The URL where the local server is running
    url = "http://localhost:1234/v1/chat/completions"

    # The headers to indicate that we are sending JSON data
    headers = {"Content-Type": "application/json"}

    # The JSON data payload
    # Read the content from PROMPT.md
    with open(f"{os.path.abspath(os.path.dirname(__file__))}/PROMPT.md", "r") as file:
        prompt_content = file.read()

    # Append the user prompt
    full_prompt = prompt_content + f'\n\nUSER PROMPT: "{user_prompt}"'

    data = {
        "messages": [
            {"role": "user", "content": full_prompt},
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False,
    }

    # Making the POST request to the local server
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Checking if the request was successful
    if response.status_code == 200:
        # Returning the response content
        return (
            response.json()
            .get("choices")[0]
            .get("message")
            .get("content")
            .replace("```", "")
            .replace("\n", "")
        )
    else:
        raise Exception(
            f"Failed to get response: {response.status_code}, {response.text}"
        )
