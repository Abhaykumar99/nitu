import asyncio
import edge_tts

# Short, fast, and lively Indian English (Hinglish) female voice

PLAIN_TEXT = "Happy Birthday Bhabhi Ji! Aaj aapka bahut hi khaas din hai. Hum sab ki taraf se aapko dher saara pyar aur badhaai. Aap hamare ghar ki raunak hain, aur aapki muskaan se poora ghar khush rehta hai. Bhagwan aapko hamesha khush rakhe, healthy rakhe, aur aapki har dua poori kare. Happy Birthday Bhabhi Ji, we love you so much!"

async def main():
    print("Generating short and fast Hinglish birthday wish...")
    communicate = edge_tts.Communicate(
        text=PLAIN_TEXT, 
        voice="en-IN-NeerjaNeural",  
        rate="+15%",  # Increased speed significantly
        pitch="+4Hz"  # Lively pitch
    )
    await communicate.save("build/audio/wish.mp3")
    print("Done! Saved to build/audio/wish.mp3")

asyncio.run(main())
