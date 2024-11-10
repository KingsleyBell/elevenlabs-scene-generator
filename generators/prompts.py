import os

from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")


def generate_prompt(prompt: str):
    client = OpenAI(api_key=openai_api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a AI video generation assistant."},
            {
                "role": "user",
                "content": f"""
                Rewrite an AI video generatino prompt. Use the following examples as a guide. Return the raw enhanced prompt as output:
                
                Here are Examples
                1. Nature Scenes
                Create a serene forest landscape at dawn in a panoramic view, with mist rolling over the trees and soft sunlight breaking through the leaves.
                2. Urban Exploration
                Show a bustling city street with skycrappers at night, illuminated by neon lights, with people walking and cars passing by
                3. Fantasy Worlds
                Imagine a floating island in a sky filled with colorful clouds, palm trees and featuring waterfalls cascading into the abyss below.
                4. Historical Settings
                Depict a medieval marketplace, with vendors selling goods, townsfolk interacting, and a castle in the background.
                5. Underwater Adventure
                Visualize a vibrant coral reef teeming with diverse marine life, including colorful fish and gently swaying seaweed
                6. Space Exploration
                Create a scene of a spaceship traveling through a colorful nebula, with distant stars and planets in the background
                7. Dreamlike Landscapes
                Generate a surreal landscape with oversized flowers and whimsical creatures, under a starry night sky.
                8. Seasonal Changes
                Show the transition of a landscape through the four seasons, from blooming spring to snowy winter.
                9. Surreal Portrait
                Create a surreal video of a person with a clock head showing moving gears as eyes display landscapes. Their mouth is a drawer filled with memory symbols. The shifting background reflects changing thoughts and feelings in this surreal dream machine concept by Luma AI sparking personal reflections and discussions
                10. Natural Phenomena: Capturing Earth’s Beauty
                Show the Grand Canyon at sunrise, capturing its vastness and colorful rock layers as the light transitions from soft purple to bright yellow. A hawk gracefully flies overhead, casting a shadow on the canyon floor, showcasing the beauty of nature.
                
                Here is the prompt: {prompt}
                """
            }
        ]
    )
    return completion.choices[0].message.content
