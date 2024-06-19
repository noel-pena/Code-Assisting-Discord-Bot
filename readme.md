# Discord Bot for Code Assistance

## Introduction

This Discord bot assists users with coding tasks using the OpenAI GPT-3.5 model. It can explain code snippets, debug issues, and provide coding suggestions based on user input.

## Features

- **Explain Command (`!explain`)**:

  - Use `!explain` followed by a code snippet to receive an explanation of the code's functionality.

- **Debug Command (`!debug`)**:

  - Use `!debug` followed by a code snippet to identify issues and receive explanations on how to fix them.

- **Code Command (`!code`)**:

  - Use `!code` followed by a task description to receive suggestions or code snippets to accomplish the task.

- **Stop Command (`stop`)**:
  - Use `stop` to command the bot to leave the server.

## Getting Started

To use this bot in your Discord server, follow these steps:

1. **Prerequisites**:

   - Python 3.6 or higher installed.
   - Discord.py library installed (`pip install discord.py`).
   - OpenAI API key. (Sign up at [OpenAI](https://beta.openai.com/docs/get-started) to get an API key.)

2. **Installation**:

   - Clone the repository:

     ```
     git clone https://github.com/noel-pena/Code-Assisting-Discord-Bot
     ```

   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```

3. **Setup Environment**:

   - Create a `.env` file in the root directory of your project and add your Discord bot token and OpenAI API key:
     ```
     TOKEN=your_discord_bot_token_here
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Running the Bot**:
   - Start the bot by running `main.py`:
     ```
     python main.py
     ```

## Usage

Once the bot is running and added to your Discord server, you can interact with it using the following commands:

- `!explain <code snippet>`: Explain the provided code snippet.
- `!debug <code snippet>`: Debug issues in the provided code snippet.
- `!code <task description>`: Get suggestions or code snippets to accomplish a task.
- `stop`: Command the bot to leave the server.

## Example

Here’s an example of interacting with the bot in a Discord channel:

User: !explain (Insert code)
Bot: Hmm... (response from openai API)

User: !code how can you print "Hello, world" in javascript
Bot: Hmm... the method to print "Hello, world" with javascript is with console.log("Hello, world")

User: stop
Bot: Snake, out
