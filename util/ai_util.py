from openai import OpenAI
from os import getenv
from pydantic import BaseModel
from typing import Optional
from typing import Type

class ai_util:
    """
    ai_util is a utility class for interacting with the OpenAI API to generate chat completions.
    Note: Only compatible with gpt-4o-mini-2024-07-18 and later, gpt-4o-2024-08-06 and later
    Attributes:
        api_key (str): The API key for authenticating with the OpenAI API.
        model (str): The model to use for generating completions. Default is "gpt-4o-2024-08-06".
        temperature (float): The sampling temperature to use. Default is 0.7.
        max_response_len (int): The maximum length of the response in tokens. Default is None.
        frequency_penalty (float): The penalty for repeated tokens. Default is 0.
    Methods:
        __init__(self, api_key: Optional[str] = None, model: str = "gpt-4o-2024-08-06", temperature: float = 0.7, max_response_len: Optional[int] = None, frequency_penalty: float = 0):
            Initializes the ai_util instance with the provided parameters.
        chat(self, messages: list, output_model: Type[BaseModel]):
            Generates a chat completion based on the provided messages and returns the content of the first choice.
            Args:
                messages (list): A list of messages to send to the model.
                output_model (Type[BaseModel]): The model to use for formatting the response.
            Returns:
                str: The content of the first message choice from the completion.
    """
    
    def __init__(
            self, 
            api_key: Optional[str] = None,
            model: str = "gpt-4o-2024-08-06",
            temperature: float = 0.7,
            max_response_len: Optional[int] = None,
            frequency_penalty: float = 0
    ):
        if not api_key:
            self.api_key = getenv("OPENAI_API_KEY")
        self.model = model
        self.temperature = temperature
        self.max_response_len = max_response_len
        self.client = OpenAI()
        self.frequency_penalty = frequency_penalty

        

    def chat(self, messages: list, output_model: Type[BaseModel]):
        """
        Sends a list of messages to the chat model and returns the response.
        Args:
            messages (list): A list of messages to be sent to the chat model.
            output_model (Type[BaseModel]): The pydantic model type for the response format.
        Returns:
            str: The content of the response message.
        """

        completion = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_response_len,
            frequency_penalty=self.frequency_penalty,
            response_format=output_model
        )
        return completion.choices[0].message.content


if __name__ == "__main__":
    # Example usage:
    ai = ai_util()
    class joke(BaseModel):
        setup: str
        punchline: str

    class jokeList(BaseModel):
        jokes: list[joke]

    response = ai.chat(
        messages = [
            {"role": "system", "content": "You are a helpful chatbot"},
            {"role": "user", "content": "Give me 10 funny jokes"}
        ],
        output_model=jokeList
    )
    print(response)