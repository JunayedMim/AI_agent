def main():
    #print("Hello from ai-agent!")
    import os
    import argparse
    from dotenv import load_dotenv
    from google import genai
    from google.genai import types 

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("Invalid API Key")

    

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="AI_agent")
    parser.add_argument("cli_prompt", type=str, help="CLI prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.cli_prompt)])]


    generated_content = client.models.generate_content(model="gemini-2.5-flash", contents=messages)

    if generated_content == None:
        raise RuntimeError("Failed API request")
    elif args.verbose is True:
        print(f"User prompt: {args.cli_prompt}")
        print(f"Prompt tokens: {generated_content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generated_content.usage_metadata.candidates_token_count}")
        print(generated_content.text)
    else:
        print(generated_content.text)



if __name__ == "__main__":
    main()
