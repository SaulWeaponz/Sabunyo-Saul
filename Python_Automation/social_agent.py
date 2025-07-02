#Introduction Of the SaulBot
# The SaulBot performs the following main actions:

# 1. Configuration Loading: Reads API keys and secrets from a .env file for security.

# 2. API Initialization: Sets up connections to Twitter (X), Google Gemini, and Pexels APIs.

# 3. Content Generation:

# Uses Gemini AI to generate a motivational tweet text based on the day of the week.

# Uses the Pexels API to search for and download a relevant image based on keywords associated with the tweet's theme.

# 4. Tweet Posting: Composes and posts the tweet with both the generated text and the downloaded image to Twitter (X). Includes a fallback to text-only if image fetching fails.

# 5. Scheduling: Uses the schedule library to run this process automatically every day at a specific time.

# 6. Cleanup: Deletes the temporary image file after tweeting to keep the system tidy.


import tweepy # For interacting with Twitter (X) API
import schedule # For scheduling daily tasks
import time # For pausing execution (sleep)
from datetime import datetime # For getting current date/time (e.g., weekday)
import os # For interacting with the operating system (e.g., environment variables, file paths)
from dotenv import load_dotenv # To load environment variables from a .env file
import google.generativeai as genai # For Google Gemini AI integration
import requests # For making HTTP requests to external APIs (Pexels)
from PIL import Image # Pillow library for image manipulation (saving downloaded image)
from io import BytesIO # To handle image data in memory before saving
import random # To pick a random image from Pexels search results

# Load environment variables from .env file
load_dotenv()

# Twitter credentials from .env
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Gemini API key from .env (for text generation)
gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

# Pexels API Key from .env (for image search)
pexels_api_key = os.getenv("PEXELS_API_KEY")

# Authenticate to Twitter
#  Authenticates the bot with the Twitter (X) API using OAuth1UserHandler with the loaded credentials.
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Gemini AI model for text generation
gemini_text_model = genai.GenerativeModel('gemini-1.5-flash')

# Prompts for Gemini AI text generation
# Derive the image search query from the generated text or a related concept.
daily_prompts = [
    {
        "text_prompt": "Write an inspiring and motivational tweet about new beginnings and setting goals for a Monday. Keep it under 280 characters. Include relevant hashtags like #MondayMotivation #NewBeginnings. Also suggest 2-3 keywords for a related image search, e.g., 'sunrise, fresh start'.",
        "image_keywords_fallback": "sunrise, fresh start, new beginning" # Fallback keywords for Pexels
    },
    {
        "text_prompt": "Compose a tweet about persistence and small progress leading to big achievements for a Tuesday. Keep it under 280 characters. Include hashtags like #TuesdayThoughts #KeepGoing. Also suggest 2-3 keywords for a related image search, e.g., 'progress, journey, perseverance'.",
        "image_keywords_fallback": "progress, journey, perseverance, effort"
    },
    {
        "text_prompt": "Create a tweet about challenges as opportunities for growth and learning for a Wednesday. Keep it under 280 characters. Include hashtags like #WednesdayWisdom #GrowthMindset. Also suggest 2-3 keywords for a related image search, e.g., 'growth, challenge, strength'.",
        "image_keywords_fallback": "growth, challenge, strength, wisdom"
    },
    {
        "text_prompt": "Generate a tweet encouraging curiosity, learning, and exploring new ideas for a Thursday. Keep it under 280 characters. Include hashtags like #ThursdayThoughts #LifelongLearning. Also suggest 2-3 keywords for a related image search, e.g., 'curiosity, learning, discovery'.",
        "image_keywords_fallback": "curiosity, learning, discovery, ideas"
    },
    {
        "text_prompt": "Write a celebratory tweet for making it through the week, appreciating efforts, and recharging for a Friday. Keep it under 280 characters. Include hashtags like #FridayFeeling #Gratitude. Also suggest 2-3 keywords for a related image search, e.g., 'celebration, weekend, relax'.",
        "image_keywords_fallback": "celebration, weekend, relax, joy"
    },
    {
        "text_prompt": "Craft a tweet about enjoying the weekend, relaxing, and doing what brings joy for a Saturday. Keep it under 280 characters. Include hashtags like #SaturdayVibes #WeekendJoy. Also suggest 2-3 keywords for a related image search, e.g., 'relaxation, fun, adventure'.",
        "image_keywords_fallback": "relaxation, fun, adventure, happy"
    },
    {
        "text_prompt": "Develop a tweet about Sunday being a day for reflection, planning, and mindfulness. Keep it under 280 characters. Include hashtags like #SundayReflection #MindfulLiving. Also suggest 2-3 keywords for a related image search, e.g., 'reflection, peace, planning'.",
        "image_keywords_fallback": "reflection, peace, planning, calm"
    }
]

def search_pexels_image(query):
    """Searches Pexels for an image and returns the URL of a random image."""
    PEXELS_API_URL = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": pexels_api_key
    }
    params = {
        "query": query,
        "per_page": 15, # Request a few images to choose from
        "orientation": "landscape" # Prefer landscape images for Twitter
    }

    try:
        response = requests.get(PEXELS_API_URL, headers=headers, params=params)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        photos = data.get('photos', [])
        if photos:
            # Pick a random photo from the results
            selected_photo = random.choice(photos)
            # You can choose different sizes: original, large, medium, small, portrait, landscape, tiny
            # 'large' is usually good quality and size for Twitter
            return selected_photo['src']['large']
        else:
            print(f"No Pexels images found for query: '{query}'")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching image from Pexels API: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during Pexels search: {e}")
        return None


def download_image(image_url):
    """Downloads an image from a URL and saves it temporarily."""
    if not image_url:
        return None

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        
        image_filename = f"temp_pexels_image_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
        
        # Ensure the image data is actually an image
        if 'content-type' in response.headers and 'image' in response.headers['content-type']:
            with open(image_filename, 'wb') as out_file:
                for chunk in response.iter_content(chunk_size=8192):
                    out_file.write(chunk)
            print(f"Downloaded image to: {image_filename}")
            return image_filename
        else:
            print(f"URL did not return an image: {image_url}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image from URL {image_url}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during image download: {e}")
        return None

def generate_content_and_image_for_tweet(text_prompt, image_keywords_fallback):
    """Generates text with Gemini and finds an image from Pexels."""
    generated_text = None
    image_path = None
    image_search_query = image_keywords_fallback # Start with fallback

    try:
        # 1. Generate text with Gemini
        text_response = gemini_text_model.generate_content(text_prompt)
        generated_text = text_response.text

        # Attempt to extract image keywords from Gemini's response if the prompt format allows
        # This is an advanced step, requiring Gemini to *also* output keywords
        # For simplicity, we will stick to using the image_keywords_fallback for now.
        # If your Gemini prompt gets refined to output "Tweet: <text> | Keywords: <keywords>",
        # you'd parse that here.
        # For now, we'll just use the provided fallback keywords directly.
        print(f"Generated text: {generated_text[:50]}...")
        
    except Exception as e:
        print(f"Error generating text with Gemini: {e}")
        generated_text = None # Ensure text is None if generation fails

    if generated_text: # Only try to get an image if text generation was successful
        # Use the image_keywords_fallback directly for Pexels search
        image_url = search_pexels_image(image_search_query)
        if image_url:
            image_path = download_image(image_url)

    return generated_text, image_path

def send_daily_tweet():
    """Generates content with AI, posts to Twitter with an image, and cleans up."""
    weekday = datetime.now().weekday()
    current_day_prompts = daily_prompts[weekday % len(daily_prompts)]

    # Debugging print to confirm Pexels key is loaded
    if pexels_api_key:
        print(f"Pexels API Key loaded (first 5 chars): {pexels_api_key[:5]}*****")
    else:
        print("Pexels API Key NOT loaded. Check .env file.")

    text, image_path = generate_content_and_image_for_tweet(
        current_day_prompts["text_prompt"],
        current_day_prompts["image_keywords_fallback"]
    )

    if text and image_path:
        try:
            # Upload the image to Twitter
            media = api.media_upload(image_path)
            # Post the tweet with the generated text and attached image
            response = client.create_tweet(text=text, media_ids=[media.media_id])
            print(f"Tweet posted for {datetime.now().strftime('%A')}: {text}")
        except tweepy.TweepyException as e:
            print(f"Error posting tweet with image: {e}")
        finally:
            # Clean up the temporary image file
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Cleaned up temporary image: {image_path}")
    elif text: # Post text only if image generation failed but text succeeded
        try:
            response = client.create_tweet(text=text)
            print(f"Tweet posted (text only) for {datetime.now().strftime('%A')}: {text}")
        except tweepy.TweepyException as e:
            print(f"Error posting text-only tweet: {e}")
    else:
        print(f"Skipping tweet for {datetime.now().strftime('%A')} due to content generation failure.")

# Schedule the tweet to be sent every day at your specified time in EAT (Kampala timezone)
# This will run at 12:45 on the next day's schedule if current time is after that.
schedule.every().day.at("08:15").do(send_daily_tweet)

print(f"Saul_Bot is running and will tweet(X) every day at 08:15 AM EAT (current time: {datetime.now().strftime('%I:%M %p %Z')}).")
while True:
    schedule.run_pending()
    time.sleep(60)