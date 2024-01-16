from fastapi import FastAPI, HTTPException, Request
from audio_gen import make_audio_sample
from model import RequestTxt2Wav
from fastapi.responses import StreamingResponse
from io import BytesIO
import scipy

app = FastAPI()

@app.post("/make_soundfile")
async def process_data(request: Request):
    try:
        data = await request.json()
        request_data = RequestTxt2Wav(**data)        
        audio_sample = make_audio_sample(request_data=request_data)
        audio_bytes_io = BytesIO()        
        scipy.io.wavfile.write(audio_bytes_io, rate=32000, data=audio_sample)
        file_format = request_data.file_format
        content_type = f"audio/{file_format}"
        return StreamingResponse(audio_bytes_io, media_type=content_type)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn    
    uvicorn.run(app, host="127.0.0.1", port=8000)
