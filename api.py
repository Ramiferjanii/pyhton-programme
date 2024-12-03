import enum 
from typing import Annotated 
from livekit.agents import llm 
import logging 


logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)

class Zone (enum.Enum) : 
    LIVING_ROOM = "living_room" 
    DERROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"



class AssistantFnc(llm.FunctionContext) : 
    def __init__(self) -> None:
        super().__init__()


        self.temperature = {
            Zone.LIVING_ROOM : 22, 
            Zone.BATHROOM : 20 ,
            Zone.KITCHEN : 24 , 
            Zone.BATHROOM : 23 , 
            Zone.OFFICE : 21 , 
        }
    
    @llm.ai_callable(description=" Get the temperature in a specific room") 
    def get_temperature(self , zone : Annotated[Zone , llm.TypeInfo(description=" the specific room")]
                        ) : 
        logger.info("get temp - zone %s" , zone) 
        temp = self._temperature [Zone(zone)] 
        return f" the temperature in the {zone} is {temp}C"