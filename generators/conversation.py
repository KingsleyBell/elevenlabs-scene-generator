import os

from elevenlabs import ElevenLabs

eleven_api_key = os.getenv("ELEVEN_LABS_API_KEY")

def generate_conversation(voice_id, text):
    client = ElevenLabs(api_key=eleven_api_key)
    result_generator = client.text_to_speech.convert(voice_id=voice_id, text=text)

    result_bytes = b""
    for piece in result_generator:
        result_bytes += piece

    return result_bytes


def get_voices():
    client = ElevenLabs(api_key=eleven_api_key)
    return client.voices.get_all()


