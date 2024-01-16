from pydantic import BaseModel

class RequestTxt2Wav(BaseModel):
    prompt: str
    negative_prompt: str    
    cfgscale: float
    seed: int
    steps: int
    length: float
    file_format: str = "wav"
    checkpoint: str = "cvssp/audioldm2"