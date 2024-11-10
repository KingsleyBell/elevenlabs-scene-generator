import os

from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")


def generate_prompt(prompt: str, type):
    client = OpenAI(api_key=openai_api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a AI video generation assistant."},
            {
                "role": "user",
                "content": get_video_prompt(prompt) if type == "video" else get_audio_prompt(prompt)
            }
        ]
    )
    return completion.choices[0].message.content


def get_video_prompt(prompt: str):
    return f"""
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


def get_audio_prompt(prompt: str):
    return f"""
    Rewrite an low volume AI audio generatino prompt. Use the following examples as a guide. Return the raw enhanced prompt as output:
    
    1. Nature Soundscape
    Create an immersive forest soundscape at dawn, with birds chirping softly, leaves rustling in a gentle breeze, and a distant river flowing, capturing the serenity of early morning in the wilderness
    2. Urban Ambiance
    Generate the sounds of a bustling city street at night, with car engines, distant horns, people chatting, and the soft hum of neon signs, encapsulating the energy and vibrancy of urban life.
    3. Fantasy World Atmosphere
    Imagine the ethereal sounds of a floating island, with distant waterfalls, mystical chimes, and the soft rustle of leaves from otherworldly trees, creating a sense of wonder and magic.
    4. Historical Marketplace
    Depict the sounds of a medieval marketplace, with merchants calling out, townsfolk bartering, and the occasional neigh of a horse, transporting listeners to a lively historical setting.
    5. Underwater Scene
    Produce a vibrant underwater audio scene, with bubbling water, the swish of fish moving by, and the gentle crackle of coral, capturing the liveliness and diversity of marine life.
    6. Space Exploration Ambience
    Create an audio experience of a spaceship cruising through a nebula, with subtle hums, distant radio signals, and the faint whir of machinery, conveying the vastness and mystery of space.
    7. Dreamlike Soundscape
    Generate a surreal, dreamlike soundscape with soft, echoing chimes, distant laughter, and whimsical sounds that come and go, creating an atmosphere of wonder and mystery.
    8. Seasonal Transitions
    Craft an audio scene that transitions through the four seasons, from the sounds of birds and blossoms in spring, to the crunching of leaves in fall, and the hush of snow in winter.
    9. Surreal Portrait Soundscape
    Create a surreal audio piece of a ticking clock overlaid with shifting ambient sounds reflecting different emotions—gentle rainfall, echoing voices, and distant bells, representing changing thoughts and feelings.
    10. Natural Phenomena: Earth’s Wonders
    Capture the sound of a storm building over the Grand Canyon, with gusting winds, distant thunder, and the calls of birds taking flight, embodying the power and beauty of nature.
    
    Output prompt should include instruction to keep vilume low

    Here is the prompt: {prompt}
    """
