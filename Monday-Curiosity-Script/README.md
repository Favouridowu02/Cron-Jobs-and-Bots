# Monday Curiosity Script

This project is designed to send weekly curiosity challenges via email. The challenges are tailored to explore various areas of interest, including engineering, cybersecurity, business, personal development, creativity, and spirituality. The script uses AI to generate personalized content and sends it to the specified email address.

## Features

- **AI-Generated Content**: Uses the `genai` library to generate curiosity challenges based on a detailed prompt.
- **Email Automation**: Sends the generated content via email using Gmail's SMTP server.
- **Personalized Challenges**: Challenges span multiple areas of interest, including engineering, cybersecurity, business, and spirituality.

## Project Structure

- `main.py`: The main script that generates and sends the email.
- `.env`: Stores sensitive information like the API key and email app password.
- `requirements.txt`: Lists the dependencies required for the project.

## Prerequisites

- Python 3.x installed on your system.
- A Gmail account with an app password enabled.
- Access to the Google GenAI API.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/Monday-Curiosity-Script.git
   cd Monday-Curiosity-Script
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the `.env` file with your credentials:
   ```plaintext
   API_KEY="your-google-genai-api-key"
   APP_PWD="your-gmail-app-password"
   ```

## Usage

1. Open the `main.py` file and review the `PROMPT` variable to ensure it aligns with your desired content.

2. Run the script to send the email:
   ```bash
   python3 main.py
   ```

3. The script will generate personalized curiosity challenges and send them to the specified email address.

## How It Works

1. **Content Generation**: The script uses the `genai` library to generate curiosity challenges based on a detailed prompt that spans multiple areas of interest.
2. **Email Sending**: The generated content is sent via email using Gmail's SMTP server. The sender's email and app password are securely retrieved from the `.env` file.
3. **Personalization**: The challenges are tailored to the recipient's interests, as defined in the `PROMPT` variable.

## Security

- Sensitive information such as API keys and email credentials are stored in the `.env` file and loaded using the `python-dotenv` library.
- Ensure that the `.env` file is not shared or committed to version control.

## Dependencies

The project requires the following Python libraries:

- `python-dotenv`: For managing environment variables.
- `smtplib`: For sending emails via Gmail's SMTP server.
- `email`: For constructing email messages.
- `google.genai`: For generating AI-based content.

## Example Output

When the script runs successfully, it generates and sends an email with the following structure:

- **Subject**: Weekly Curiosity Drop!
- **Body**: A personalized curiosity challenge spanning multiple areas of interest, including engineering, cybersecurity, business, creativity, and spirituality.

## Troubleshooting

- If the email fails to send, ensure that:
  - Your Gmail account has app passwords enabled.
  - The `.env` file contains the correct credentials.
  - You have an active internet connection.
- Check the error message printed in the console for more details.

## Future Improvements

- Add support for multiple recipients.
- Enhance the AI prompt for more diverse and engaging challenges.
- Implement logging for better debugging and monitoring.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Acknowledgments

- Google GenAI for powering the content generation.
- Python community for providing the tools and libraries used in this project.