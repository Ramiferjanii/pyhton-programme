import asyncio

from dotenv import load_dotenv 
from livekit.agents import AutoSubscribe , JobContext , WorkerOptions , cli , llm 
from livekit.agents.voice_assistant import VoiceAssistant 
from livekit.plugins import openai , silero 
from api import AssistantFnc 

load_dotenv()


async def entrypoint ( ctx : JobContext ) : 
    initial_ctx = llm.ChatContext().append(
        role= "system" , 
        text=(
            " you are a voice assistant created by LiveKit . you interface with users will  be voice . "
            " you should use short and concise reponses , and avoising usage of unpronouncable punctuation . "

        ) ,
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)  


    fnc_ctx = AssistantFnc()

    assitant = VoiceAssistant(
        vad = silero.VAD.load() , # voice assitant detection 
        stt=openai.STT() , 
        llm=openai.LLM() , 
        tts=openai.TTS() ,
        chat_ctx=initial_ctx , 
        fnc_ctx=fnc_ctx , 
    )
    
    assitant.start(ctx.room)
    await assitant.say(" Hey , How can help you today " , allow_interruptions=True) 




if __name__ == "__main__" : 
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
