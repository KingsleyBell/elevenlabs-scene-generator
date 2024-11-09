import os

from elevenlabs import ElevenLabs

eleven_api_key = os.getenv("ELEVEN_LABS_API_KEY")


def generate_sound_effect(prompt, duration):
    client = ElevenLabs(api_key=eleven_api_key)
    result_generator = client.text_to_sound_effects.convert(
        text=prompt,
        duration_seconds=duration,
        prompt_influence=0.5,
    )

    result_bytes = b""
    for piece in result_generator:
        result_bytes += piece

    return result_bytes


